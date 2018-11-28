#include <iostream>
#include <string>
#include<map>

using namespace std;

typedef long long ll;

map<int,double> wp2,wp,owp,oowp,rpi;

int T,n,X[100][100],cnt;
char c[100];


void cal_wp()
{
    int win=0,loss=0;
    for (int i=0;i<n;i++)
    {
        win=0;
        loss=0;
        for (int j=0;j<n;j++)
        {
            if(X[i][j]==1)
                win++;
            else if(X[i][j]==0)
                loss++;
        }
        wp[i]=(double)win/(win+loss);
    }
    
}

void cal_wp2(int x)
{
    wp2.clear();
    int win=0,loss=0;
    for (int i=0;i<n;i++)
    {
        win=0;
        loss=0;
        for (int j=0;j<n;j++)
        {
            if(j!=x)
            if(X[i][j]==1)
                win++;
            else if(X[i][j]==0)
                loss++;
        }
        wp2[i]=(double)win/(win+loss);
    }
    
}

void cal_owp()
{
    
    double winp;
    int count=0;
    for (int i=0;i<n;i++)
    {
        winp=0;
        count=0;
        cal_wp2(i);
        for (int j=0;j<n;j++)
        {
            if(X[i][j]!=2&&j!=i)
            {
                winp+=wp2[j];
                count++;
            }
        }
        owp[i]=(double)winp/count;
    }    
    
}

void cal_oowp()
{
    
    double owinp;
    int count=0;
    for (int i=0;i<n;i++)
    {
        owinp=0;
        count=0;
        cal_wp2(i);
        for (int j=0;j<n;j++)
        {
            if(X[i][j]!=2)
            {
                owinp+=owp[j];
                count++;
            }
        }
        oowp[i]=(double)owinp/count;
    }    
    
}


void cal_rpi()
{
    for (int i=0; i<n; i++)
    rpi[i]= 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
    
    
}

int main ()
{
    scanf("%d",&T);
    cnt=0;
    while(cnt<T)
    {
        cnt++;
        scanf("%d",&n);
        int i=0;
        while(i<n)
        {
            
            cin>>c;
            for (int j=0;j<n;j++)
            {
                if(c[j]=='1')
                    X[i][j]=1;
                else if(c[j]=='0')
                    X[i][j]=0;
                else
                    X[i][j]=2;
                    //cout<<X[i][j];
            }
            i++;
        }
        
        /*i=0;
        while(i<n)
        {
            for (int j=0;j<n;j++)
            {
                cout<<X[i][j];
            }
            
            i++;
            cout<<endl;
        }*/
        cal_wp();
        cal_owp();
        cal_oowp();
        cal_oowp();
        cal_rpi();
        
        printf ("Case #%d: \n", cnt);
        for (int i=0; i<n; i++)
        printf("%.10f\n",rpi[i]);
        
    }
    
    
    return 0;
}
