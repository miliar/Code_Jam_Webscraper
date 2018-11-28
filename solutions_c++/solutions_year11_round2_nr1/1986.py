#include<iostream>
#include<stdio.h>
#include<cmath>

using namespace std;


int t,tt,n,i,j,k,l,op[100][100];
double wptmp,wpsum,owpsum,suma,sumb,sumc,wp[100],owp[100],oowp[100],rpi[100];
char mat[100][100];

FILE *in,*out;

int main()
{
    in=freopen("A-large.in","r",stdin);
    out=freopen("A-large.out","w",stdout);
    cin>>t;
    tt=t;
    while (tt)
    {
        cin>>n;
        for (i=0;i<n;i++)
            scanf("%s",mat[i]);
        for (i=0;i<n;i++)
            for (j=0;j<n;j++)
            {
                if (mat[i][j]=='.')
                    op[i][j]=-1;
                else if (mat[i][j]=='1')
                    op[i][j]=1;
                else
                    op[i][j]=0;
            }
        for (i=0;i<n;i++)
        {
            suma=0;
            sumb=0;
            for (j=0;j<n;j++)
            {
                if (op[i][j]!=-1)
                    suma++;
                if (op[i][j]==1)
                    sumb++;
            }
            wp[i]=(double)sumb/(double)suma;
        }
        //wp counting

        for (i=0;i<n;i++)
        {
            suma=0;
            wpsum=0;
            for (j=0;j<n;j++)
            {
                if (op[i][j]!=-1)//one opponent
                {
                    suma++;
                    sumb=0;
                    sumc=0;
                        for (k=0;k<n;k++)//non-i opponent of j
                        {
                            if (op[k][j]!=-1 && k!=i)//non-i opponent of j
                            {
                                sumb++;
                                sumc+=op[j][k];
                            }

                        }
                    wptmp=(double)sumc/(double)sumb;
                    wpsum+=wptmp;
                }

            }
            owp[i]=wpsum/(double)suma;
        }
        //owp counting
        cout<<"Case #"<<t-tt+1<<":"<<endl;
        for (i=0;i<n;i++)
        {
            suma=0;
            owpsum=0;
            for (j=0;j<n;j++)
            {
                if (op[i][j]!=-1)
                {
                    suma++;
                    owpsum+=owp[j];
                }
            }
            oowp[i]=owpsum/(double)suma;
            rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
            cout<<rpi[i]<<endl;
        }
        tt--;
    }
    return 0;
}
