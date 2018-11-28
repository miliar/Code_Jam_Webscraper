#include<stdio.h>
#include<string.h>
using namespace std;
char ch;
int a,b,c,d,e,f,g;
int zz[105][105];
int jml[105][3];
double wp[105],owp[105][105],owp2[105],oowp[105];
int main()
{
    //freopen("rpi.in","r",stdin);
    //freopen("rpi.out","w",stdout);
    scanf("%d",&a);
    for (b=1;b<=a;b++)
    {
        memset(zz,0,sizeof(zz));
        memset(jml,0,sizeof(jml));
        memset(wp,0,sizeof(wp));
        memset(owp,0,sizeof(owp));
        memset(owp2,0,sizeof(owp2));
        memset(oowp,0,sizeof(oowp));
        scanf("%d",&c);
        for (d=1;d<=c;d++)
        {
            f=0; g=0;
            scanf("%c",&ch);
            for (e=1;e<=c;e++)
            {
                scanf("%c",&ch);
                //printf("%c\n",ch);
                if (ch=='0')
                {
                   zz[d][e]=1;
                   f++;
                }
                else
                    if (ch=='1')
                    {
                       zz[d][e]=2;
                       g++;
                    }
            }
            jml[d][1]=f;
            jml[d][2]=g;
            wp[d]=(double)g/(f+g);
            //printf("%.12lf\n",wp[d]);
        }
        for (d=1;d<=c;d++)
        {   
            for (e=1;e<=c;e++)
            {
                if (zz[d][e]!=0)
                {
                   if (zz[d][e]==2)
                   {
                      if (jml[d][2]>1 && jml[d][2]+jml[d][1]>1)
                      owp[d][e]=(double)(jml[d][2]-1)/(jml[d][2]+jml[d][1]-1);
                      else
                      owp[d][e]=0;                   
                   }
                   else
                   {
                       if (jml[d][2]+jml[d][1]>1 && jml[d][2]>0)
                       owp[d][e]=(double)jml[d][2]/(jml[d][2]+jml[d][1]-1);
                       else
                       owp[d][e]=0;
                   }                
                }
                //printf("%lf ",owp[d][e]);
            }
           // printf("\n");
        }
        double sum;
        int co;
        for (d=1;d<=c;d++)
        {
            sum=0; co=0;
            for (e=1;e<=c;e++)
            {
                if (zz[d][e]!=0)
                {
                   co++;
                   sum+=owp[e][d];                  
                }    
            }
            owp2[d]=sum/(double)co;
        }
        for (d=1;d<=c;d++)
        {
            sum=0; co=0;
            for (e=1;e<=c;e++)
            {
                if (zz[d][e]!=0)
                {
                    co++;
                    sum+=owp2[e];               
                }    
            }
            oowp[d]=sum/(double)co;
        }
        printf("Case #%d:\n",b);
        for (d=1;d<=c;d++)
        {
            //printf("%lf\n",oowp[d]);
            printf("%.12lf\n",0.25*wp[d]+0.5*owp2[d]+0.25*oowp[d]);    
        }
    }
    //scanf("%d\n",a);
}
