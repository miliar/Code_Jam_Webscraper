#include<iostream>
//#include<conio.h>
using namespace std;
char a[51][51];
int checkh(char c,int i,int j,int n,int k)
{
    int x,y;
    int min=(j+k)<n?j+k:n;
    if(min!=(j+k))return 0;
    int flag=1; 
    for(y=j;y<min;y++)
    {
        if(a[i][y]!=c)
            flag=0;
    }
    return flag;
}
int checkv(char c,int i,int j,int n,int k)
{
    int x,y;
    int min=(i+k)<n?i+k:n;
    if(min!=(i+k))return 0;
    int flag=1; 
    for(x=i;x<min;x++)
    {
        if(a[x][j]!=c)
            flag=0;
    }
    return flag;
}
int checkd1(char c,int i,int j,int n,int k)
{
    int x,y;
    if(i+k>n)return 0;
    if(j+k>n)return 0;
    for(x=i,y=j;x<i+k;x++,y++)
    {

        if(a[x][y]!=c)
            return 0;
    }
    return 1;    
}
int checkd2(char c,int i,int j,int n,int k)
{
    int x,y;
    if(i-k+1<0)return 0;
    if(j-k+1<0)return 0;
    for(x=i,y=j;x>=(i-k+1);x--,y--)
    {

        if(a[x][y]!=c)
            return 0;
    }
    return 1;    
}
int checkd3(char c,int i,int j,int n,int k)
{
    int x,y;
    if(i-k+1<0)return 0;
    if(j+k>n)return 0;
    for(x=i,y=j;x>=(i-k+1);x--,y++)
    {

        if(a[x][y]!=c)
            return 0;
    }
    return 1;    
}
int checkd4(char c,int i,int j,int n,int k)
{
    int x,y;
    if(i+k>n)return 0;
    if(j-k+1<0)return 0;
    for(x=i,y=j;x<i+k;x++,y--)
    {
        //cout<<x<<" "<<y<<endl;
        if(a[x][y]!=c)
            return 0;
    }
    return 1;    
}

int main(void)
{
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int t;
    int u=1;
    cin>>t;
    while(t-->0)
    {
        int n,k;

        int i,j;
        cin>>n>>k;
        for(i=0;i<n;i++)
        {
            scanf("%s",&a[i]);
        }
        for(j=n-2;j>=0;j--)
        {
            for(i=0;i<n;i++)
            {
                if(a[i][j]=='.')continue;
                int x=j;
                while((x+1)<n&&a[i][x+1]=='.')
                {
                    a[i][x+1]=a[i][x];
                    a[i][x]='.';
                    x++;
                }
            }
        }
        int flagR=0,flagB=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
            if(!flagR)flagR=checkh('R',i,j,n,k);
            if(!flagB)flagB=checkh('B',i,j,n,k);
            if(!flagR)flagR=checkv('R',i,j,n,k);
            if(!flagB)flagB=checkv('B',i,j,n,k);
            if(!flagR)flagR=checkd1('R',i,j,n,k);
            if(!flagB)flagB=checkd1('B',i,j,n,k);
            if(!flagR)flagR=checkd2('R',i,j,n,k);
            if(!flagB)flagB=checkd2('B',i,j,n,k);
            if(!flagR)flagR=checkd3('R',i,j,n,k);
            if(!flagB)flagB=checkd3('B',i,j,n,k);
            if(!flagR)flagR=checkd4('R',i,j,n,k);
            if(!flagB)flagB=checkd4('B',i,j,n,k);
            if(flagR==1 && flagB==1)
                    break;
    
            }
            if(flagR==1 &&flagB==1)
                    break;

        }
        if(flagR==1 && flagB==1)
            cout<<"Case #"<<u<<": "<<"Both"<<endl;
        else if(flagR==1)
            cout<<"Case #"<<u<<": "<<"Red"<<endl;
        else if(flagB==1)
            cout<<"Case #"<<u<<": "<<"Blue"<<endl;
        else
            cout<<"Case #"<<u<<": "<<"Neither"<<endl;
        u++;
    }
    
/*        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                cout<<a[i][j];
            }
            cout<<endl;
        }
    }*/
}    
