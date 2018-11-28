#include<iostream>
#include<cstdlib>
#include<fstream>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    const int lxx=100+5;
    int ts;
    cin>>ts;
    int a[lxx][lxx];
    for (int ti=0; ti<ts; ti++)
    {
        int n;
        cin>>n;
        getchar();
        for (int i=0; i<n; i++)
        {
            string s;
            cin>>s;
            for (int j=0; j<n; j++)
            {
                char ch=s[j];
                if (ch=='.')
                    ch='2';
                a[i][j]=int(ch)-int('0');
            }
        }
        double w[lxx], t[lxx], wp[lxx], wp2[lxx], owp[lxx], oowp[lxx];
        for (int i=0; i<n; i++)
        {
            w[i]=0;
            t[i]=0;
            for (int j=0; j<n; j++)
            {
                if (a[i][j]==2)
                    continue;
                if (a[i][j]==1)
                    w[i]++;
                t[i]++;
            }
            wp[i]=double(w[i])/t[i];
        }
        for (int i=0; i<n; i++)
        {
            double k=0;
            for (int j=0; j<n; j++)
            {
                if (a[i][j]==2)
                    continue;
                k+=double(w[j]-a[j][i])/(t[j]-1);
            }
            owp[i]=k/t[i];
        }
        for (int i=0; i<n; i++)
        {
            double k=0;
            for (int j=0; j<n; j++)
                if (a[i][j]!=2)
                    k+=owp[j];
            oowp[i]=k/t[i];
        }
        cout<<"Case #"<<ti+1<<":"<<endl;
        for (int i=0; i<n; i++)
        {
            double rpi=0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
            printf("%.8lf\n",rpi);
        }
    }
    return 0;
}
                
            
