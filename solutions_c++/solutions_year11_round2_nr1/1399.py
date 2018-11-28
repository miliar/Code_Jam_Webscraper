#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int a[200][200];
double wp[200],owp[200],oowp[200];

int main()
{
    int t,q,i,j,n,g,w,k,kol;
    double tmp,s;
    char c;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>n;
        for (i=0;i<n;i++)
          for (j=0;j<n;j++)
          {
              cin>>c;
              if (c=='.')
                a[i][j]=-1;
              else
                a[i][j]=c-'0';
          }
        for (i=0;i<n;i++)
        {
            w=0;
            g=0;
            for (j=0;j<n;j++)
            {
                if (a[i][j]>=0)
                  g++;
                if (a[i][j]>0)
                  w++;
            }
            wp[i]=(double)w/g;
        }
        for (i=0;i<n;i++)
        {
            s=0;
            kol=0;
            for (j=0;j<n;j++)
              if (a[i][j]>=0)
              {
                    w=0;
                    g=0;
                    for (k=0;k<n;k++)
                    {
                        if (a[j][k]>=0 && k!=i)
                            g++;
                        if (a[j][k]>0 && k!=i)
                            w++;
                    }
                    kol++;
                    //cout<<"@@@"<<g<<endl;
                    s+=(double)w/g;
              }
            //cout<<s<<'/'<<kol<<endl;
            owp[i]=s/kol;
        }
        for (i=0;i<n;i++)
        {
            kol=0;
            s=0;
            for (j=0;j<n;j++)
              if (a[i][j]>=0)
              {
                  kol++;
                  s+=owp[j];
              }
            oowp[i]=s/kol;
        }
        /*for (i=0;i<n;i++)
          cout<<owp[i]<<" ";
        cout<<endl;*/
        printf("Case #%d:\n",q+1);
        for (i=0;i<n;i++)
          printf("%.8lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
    return 0;
}
