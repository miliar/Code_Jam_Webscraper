#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main()
{
        long long int q,Q;
        long long int sol,sol1;
        long long int x,y,x1,x2,x3,y1,y2,y3,n,A,B,C,D,M,a,b,c,d;
        long long int mapa[3][3];

        scanf(" %lld",&Q);
        for(q=1;q<=Q;q++)
        {
                memset(mapa,0,sizeof(long long int)*9);
                scanf(" %lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x,&y,&M);

                mapa[x%3][y%3]++;
                for(a=1;a<=n-1;a++)
                {
                        x=(A*x+B)%M;
                        y=(C*y+D)%M;
                        mapa[x%3][y%3]++;
                }

                sol=0;
                sol1=1;
                for(a=0;a<9;a++)
                {
                        x1=a%3;
                        y1=a/3;
                        if(mapa[x1][y1]>0)
                        {
                                sol1*=mapa[x1][y1];
                                mapa[x1][y1]--;
                                for(b=0;b<9;b++)
                                {
                                        x2=b%3;
                                        y2=b/3;
                                        if(mapa[x2][y2]>0)
                                        {
                                                sol1*=mapa[x2][y2];
                                                mapa[x2][y2]--;
                                                for(c=0;c<9;c++)
                                                {
                                                        x3=c%3;
                                                        y3=c/3;
                                                        if(((x1+x2+x3)%3)==0 && ((y1+y2+y3)%3)==0)
                                                                sol+=sol1*mapa[x3][y3];
                                                }
                                                mapa[x2][y2]++;
                                                sol1/=mapa[x2][y2];
                                        }
                                }
                                mapa[x1][y1]++;
                                sol1/=mapa[x1][y1];
                        }
                }

                printf("Case #%lld: %lld\n",q,sol/6);
        }

        return(0);
}
