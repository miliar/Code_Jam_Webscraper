#include<stdio.h>
#include<string.h>
int t[10];
int main()
{
    freopen("ci","r",stdin);
    freopen("co","w",stdout);
    int T=0;
    scanf("%d",&T);
    int n=1;
    while(T--)
    {
        int ans=0;
        memset(t,0,sizeof(t));
        int A=0,B=0;
        scanf("%d%d",&A,&B);
        for(int x=A;x<=B;x++)
        {
            int i=0;
            int y=x;
            while(y/10!=0)
            {
                t[i]=y%10;
                i++;
                y=y/10;
            }
            t[i]=y;
          /*  for(int k=0;k<=i;k++)
            {
                printf("%d",t[k]);
            }
            printf("\n");*/

            for(int j=1;j<=i;j++)
            {

                y=0;
                if(t[j-1]==0 || x<=10)
                {
                     continue;
                }
                for(int k=j-1;k>=0;k--)
                {
                    y=y*10+t[k];
                }
                for(int k=i;k>=j;k--)
                {
                    y=y*10+t[k];
                }

               if( x<y && y<=B)
               {

                  ans+=1;
                 // printf("x= %d  y = %d\n",x,y);
               }



             }
          //  printf("ans = %d\n",ans);
        }

        printf("Case #%d: %d\n",n,ans);
        n++;
    }
}
