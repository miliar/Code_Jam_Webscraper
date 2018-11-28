#include<stdio.h>
#include<math.h>
int main()
{
    int count,i,j,k,m,n,s,p,a,div;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    while(scanf("%d",&n)==1)
    {
        for(i=1;i<=n;i++)
        {
            scanf("%d %d %d",&m,&s,&p);
            count=0;
            for(j=0;j<m;j++)
            {
                scanf("%d",&a);
                div=a/3;
                if(div*3==a&&div>=p)
                {
                    count++;
                }
                else if(div+((div+1)*2)==a&&(div+1)>=p)
                {
                    count++;
                }
                else if(div*2+(div+1)==a&&(div+1)>=p)
                {
                    count++;
                }
                else if(div*2+(div-1)==a&&(div+1)>=p&&div!=0)
                {
                    count++;
                }
                else if(div+((div-1)*2)==a&&div>=p&&div!=0)
                {
                    count++;
                }
                else if(s>0&&(div+(div+1)+(div-1))==a&&(div+1)>=p&&div!=0)
                {
                    count++;
                    s--;
                }
                else if(div*2+(div+2)==a&&(div+2)>=p&&s>0)
                {
                    count++;
                    s--;
                }
                else if(div*2+(div-2)==a&&div>=p&&s>0&&div>1)
                {
                    count++;
                    s--;
                }
            }
            printf("Case #%d: %d\n",i,count);
        }
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
