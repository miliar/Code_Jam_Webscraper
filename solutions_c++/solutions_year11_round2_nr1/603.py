#include<iostream>
using namespace std;
#define maxn 200
long n,m,i,j,k,x,t,ss;
long a[maxn][maxn],cas,tst;
double wp1[maxn],wp2[maxn],owp[maxn],oowp[maxn];
string s;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.txt","w",stdout);
    for (scanf("%ld",&cas),tst=1;tst<=cas;tst++)
    {
        scanf("%ld",&n);
        for (i=0;i<n;i++)
        {
            cin>>s;
            x=t=0;
            for (j=0;j<n;j++)
            {
                if (s[j]=='.') a[i][j]=0;
                if (s[j]=='1') {a[i][j]=1;x++;t++;}
                if (s[j]=='0') {a[i][j]=-1;t++;}
            }
            wp1[i]=(double)x/(double)t;
//            cout<<wp1[i]<<endl;
        }
        for (i=0;i<n;i++)
        {
            owp[i]=0;
            ss=0;
            for (j=0;j<n;j++) if (a[i][j]!=0)
            {
                x=t=0;
                for (k=0;k<n;k++) if (a[j][k]!=0 && k!=i)
                {
                    if (a[j][k]==1) {x++;t++;}
                       else t++;
                }
                wp2[i]=(double)x/(double)t;
                owp[i]+=wp2[i];
                ss++;
            }
            owp[i]/=(double)ss;
        }
        for (i=0;i<n;i++)
        {
            oowp[i]=0;
            ss=0;
            for (j=0;j<n;j++) if (a[i][j]!=0)
            {
                oowp[i]+=owp[j];
                ss++;
            }
            oowp[i]/=(double)ss;
        }
        printf("Case #%ld:\n",tst);
        for (i=0;i<n;i++) printf("%.12f\n",0.25*wp1[i]+0.5*owp[i]+0.25*oowp[i]);
    }
//    system("PAUSE");
    return 0;
}
