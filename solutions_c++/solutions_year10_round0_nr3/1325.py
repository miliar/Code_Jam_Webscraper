#include <stdio.h>
#include <string.h>
long long judge[1010];
long long xhjvalue[1010];
long long a[1010];
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	bool small;
	long long r,k,n,i,v,j,num,sum,total,x,value,zuihoucha,ans,xunhuanjie,xhjzhi;
	scanf("%I64d",&T);
	for(v=1;v<=T;v++)
	{
	    scanf("%I64d%I64d%I64d",&r,&k,&n);
	    if(n==1)
        {
            scanf("%I64d",&a[i]);
           printf("Case #%I64d: %I64d\n",v,r);
            continue;
        }
	    small=true;
	    num=0,sum=0,total=0,ans=0;
        value=0;
	    memset(judge,0,sizeof(judge));
	    memset(xhjvalue,0,sizeof(xhjvalue));
	    for(i=0;i<n;i++)
	    {
            scanf("%I64d",&a[i]);
            value+=a[i];
        }
        if(value<=k)
        {
            printf("Case #%I64d: %I64d\n",v,value*r);
            continue;
        }
        j=0;
        while(1)
        {
            if(sum==0&&judge[j])
            {
     //            printf("j==%I64d\n",j);
     //            printf("judge[j]==%I64d\n",judge[j]);
                small=false;
                break;
            }
            if(sum==0&&!judge[j])
            {
                judge[j]=num;
                xhjvalue[j]=total;
      //          printf("j==%I64d num==%I64d\n",j,num);
            }
            sum+=a[j];
    //        printf("a[j]==%I64d\n",a[j]);
            if(sum>k)
            {
                num++;
                total+=sum-a[j];
                if(num==r)
                {
                small=true;
                break;
                }
                sum=0;
                j--;
            }
            j++;
            if(j==n)
            j=0;
        }
       if(!small)
       {
                               xunhuanjie=num-judge[j];
                        //       printf("xunhuanjie==%I64d\n",xunhuanjie);
                       //        printf("judge[j]==%I64d\n",judge[j]);
                               zuihoucha=(r-num)%xunhuanjie;
                               xhjzhi=total-xhjvalue[j];
                       //        printf("xhjzhi==%I64d\n",xhjzhi);
                         //      printf("total==%I64d\n",total);
                               ans+=total;
                               ans+=(((r-judge[j])-(r-judge[j])%xunhuanjie)/xunhuanjie-1)*xhjzhi;
                               sum=0;
                        //       printf("ans==%I64d\n",ans);
                        //       printf("zuihoucha==%I64d\n",zuihoucha);
                               while(zuihoucha)
                                {
                                    sum+=a[j];
                                    if(sum>k)
                                    {
                                        zuihoucha--;
                                        ans+=sum-a[j];
                                        sum=0;
                                        j--;
                                    }
                                    j++;
                                    if(j==n)
                                    j=0;
                                }
                                printf("Case #%I64d: %I64d\n",v,ans);
                           }

        else
    printf("Case #%I64d: %I64d\n",v,total);
   }
	return 0;
}
