#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int a[1005];
FILE*out=fopen("D://out.txt","w");
struct node
{
 int id;
 int qu;
 int num;
};
bool mask[1005];
node tt[1005];
void work()
{
 int r,k,n;
 int i,j;
 int temp; 
 __int64 sum,sum1,ans,t;
 __int64 total;
 total=0;
 scanf("%d%d%d",&r,&k,&n);
 for(i=0;i<n;i++){scanf("%d",&a[i]);total+=a[i];}
 if(total<=k){ans=total*r;}
 else
 {
 memset(mask,false,sizeof(mask));
 temp=0; 
 tt[temp].num=0;

 sum1=0;
 int te=0;
 bool flag=false;
 while(!mask[temp]&&!flag)
 {
      mask[temp]=true;
	  printf("%I64d %d %d\n",sum1,temp,te);
      i=temp;
	  sum=0;
	  sum+=a[i];
	  sum1+=a[i];
	  while(sum<=k)
	  {
		  i++;
		  if(i>=n)i=0;
		  sum+=a[i];
		  sum1+=a[i];
	  }
	  sum1-=a[i];
	  te++;
	  if(te>=r){ans=sum1;flag=true;break;}
	  else
	  {
		 if(!mask[i])
		 {
		  tt[i].num=sum1;
		  tt[i].qu=te;
		  tt[temp].id=i;
		 }
		  temp=i;
	  }
 }
 if(!flag)
 {
	 printf("%I64d %d\n",sum1,temp);
	 int cur_num=sum1-tt[temp].num;
	 int cur_qu=te-tt[temp].qu;
	 printf("%d %d\n",cur_num,cur_qu);
	 r=r-tt[temp].qu;
	 ans=tt[temp].num;
	 printf("%I64d ",ans);
	 t=r/cur_qu;
	 ans+=(t*cur_num);
	 printf("%I64d\n",ans);
	 t=r%cur_qu;
	 printf("%d\n",t);
	 while(t>0)
	 {
		 t--;
		 sum=0;
		 i=temp;
		 sum+=a[i];
		 ans+=a[i];
		 while(sum<=k)
		 {
			 i++;
			 if(i>=n)i=0;
			 sum+=a[i];
			 ans+=a[i];
			 printf("%I64d\n",ans);
		 }
		 //te++;
		 ans-=a[i];
		 temp=i;
	 }
 }
 }
 fprintf(out,"%I64d\n",ans);
}
int main()
{
	int test;
	scanf("%d",&test);
     for(int cas=1;cas<=test;cas++)
	 {
		 fprintf(out,"Case #%d: ",cas);
		work();
	}
	return 0;
}
		  
