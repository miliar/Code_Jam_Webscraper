#include<stdio.h>

char mat[101][101];
double wp[101],owp[101],oowp[101],p,s;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,kcase=0,ct,tt,i,j,n,c,k;
    scanf("%d",&t);
    while(t--)
    {
        kcase++;
        scanf("%d ",&n);
        for(i=0;i<n;i++)
        {
            ct=0;
            tt=0;
            for(j=0;j<n;j++)
            {
                scanf(" %c",&mat[i][j]);
                if(mat[i][j]=='1')
                {
                    ct++;
                    tt++;
                }
                if(mat[i][j]=='0')
                    tt++;
            }

            wp[i]=(double)ct/tt;
            //printf("%lf\n",wp[i]);
        }

//        printf("sss\n");
//        for(i=0;i<n;i++)
//        {    for(j=0;j<n;j++)
//                printf("%c",mat[i][j]);
//            printf("\n");
//        }
//             for(i=0;i<n;i++)
//                printf("%lf ",wp[i]);
//            printf("\n");


        for(i=0;i<n;i++)
        {
            c=0;
            s=0;
            for(j=0;j<n;j++)
            {

                if(mat[i][j]=='1'||mat[i][j]=='0')
                {
                    c++;
                     ct=0;
                    tt=0;
                    for(k=0;k<n;k++)
                    {
                        if(i==k)
                            continue;
                        if(mat[j][k]=='0')
                                tt++;
                        if(mat[j][k]=='1')
                        {
                            ct++;
                            tt++;
                        }
                    }
                    s+=(double)ct/tt;
                }
                owp[i]=(double) s/c;

            }
        }



        for(i=0;i<n;i++)
        {
            s=0;
            tt=0;
            for(j=0;j<n;j++)
            {
                if(mat[i][j]=='1'||mat[i][j]=='0')
                {
                    s+=owp[j];
                    tt++;
                }
            }
            oowp[i]=(double)s/tt;
        }
//        for(i=0;i<n;i++)
//                printf("%lf ",oowp[i]);
//            printf("\n");

        printf("Case #%d:\n",kcase);
        for(i=0;i<n;i++)
        {
            p= 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
            printf("%lf\n",p);
        }
    }
    return 0;
}








