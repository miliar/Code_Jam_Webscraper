#include<iostream>
#include<cstring>
using namespace std;

int p[200];
bool v[200];
char a[200];
int main()
{
   int t,i,j,k,m;
  freopen("A-large.in","r",stdin);
   freopen("aa.out","w",stdout);
   scanf("%d",&t);
   for(k=1;k<=t;k++)
   {
	   scanf("%s",a);
	   int l=strlen(a);
	   memset(v,false,sizeof(v));
	   int cnt=0;
	   for(i=0;i<l;i++)
	   {
     if(!v[a[i]-'0'])
	 {
	//	 printf("i=%d\n",i);
		 cnt++;
		 v[a[i]-'0']=true;
	 }
	   }
	   if(cnt==1) cnt++;
//	   printf("%d\n",cnt);
	   memset(p,-1,sizeof(p));
	   m=1;
	   p[0]=1;
	   for(i=1;i<l;i++) if(a[i]==a[0]) p[i]=1;
	   m=0;
	   for(i=1;i<l;i++) if(p[i]==-1)
	   {

		   p[i]=0;
		   break;
	   }
	   for(j=0;j<l;j++) if(a[j]==a[i]) p[j]=0;
	   m=2;
	   while(m<cnt)
	   {
	   for(i=0;i<l;i++)
	     if(p[i]==-1)
		 {
			 p[i]=m;
			 break;
		 }
		 for(j=0;j<l;j++) if(a[j]==a[i]) p[j]=m;
		 m++;
	   }
	   long long s=0;
	   for(i=0;i<l;i++) s=s*cnt+p[i];
	   printf("Case #%d: %lld\n",k,s);
   }
   return 0;
}
		   