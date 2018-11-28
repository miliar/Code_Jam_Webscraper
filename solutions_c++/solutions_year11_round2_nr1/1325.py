#include<stdio.h>
#include<string.h>
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int n;
char grid[200][200];

double wp[200],owp[200],oowp[200];

int main()
{
    freopen("A1.in","rt",stdin);
    freopen("A.out","wt",stdout);
    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++)
    {
        scanf("%d",&n);
        int cntp,cntw,cnt;
        for(int i=0;i<n;i++) {
            cntp=0;cntw=0;
            scanf("%s",&grid[i]);
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]!='.')
                {
                    cntp++;
                    if(grid[i][j]=='1') cntw++;
                }
            }
            wp[i]=(double)(cntw)/(double)(cntp);
        }
        printf("Case #%d:\n",cas);

        for(int i=0;i<n;i++)
        {
            cnt=0;
            owp[i]=0;
            for(int j=0;j<n;j++)
            {

                if(i!=j&&grid[i][j]!='.')
                {
                    cnt++;
                    cntp=0;cntw=0;
                    for(int l=0;l<n;l++)
                    {
                        if(grid[j][l]!='.'&&l!=i)
                        {
                            cntp++;
                            if(grid[j][l]=='1') cntw++;
                        }
                    }
                    owp[i]+=(double)(cntw)/(double)(cntp);

                }
            }
            owp[i]=owp[i]/(double)(cnt);
            //printf("%lf\n",owp[i]);
        }

        for(int i=0;i<n;i++)
        {
            cnt=0;oowp[i]=0;
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]!='.'&&i!=j)
                {
                    cnt++;
                    oowp[i]+=owp[j];
                }
            }
            oowp[i]/=(double)(cnt);
        }


        for(int i=0;i<n;i++)
        {
            printf("%.10lf\n",0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]);
        }



    }
    return 0;
}
