#include <stdio.h>
#include <string.h>
#include<map>
using namespace std;
char h[64];
__int64 h1[64];
map<char,__int64> m;
int main()
{
	freopen("A-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
  __int64 n,i,j,k,t,t1,t2,t3,cnt,cnt2,cnt3,len,now,res;
  scanf("%I64d",&t);
  t1=1;
  while (t--)
  {
	  m.clear();
	  scanf(" %s",h);
	  len=strlen(h);
      m[h[0]]=1;
      cnt=1;
	  now=0;
	  h1[0]=1;
	  for(i=1;i<len;i++)
	  {
         if(m.find(h[i])==m.end())
		 {
			 cnt++;
			 h1[i]=now;
			 m[h[i]]=now;
			 if(now==0)
				 now+=2;
			 else
				 now++;
		 }
		 else
		 {
			 h1[i]=m[h[i]];
		 }
	  }
	  if(cnt==1)
		  cnt=2;
       res=0;
	   for(i=0;i<len;i++)
		   res=res*cnt+h1[i];
	   printf("Case #%I64d: %I64d\n",t1,res);
	   t1++;
  }
  return 0;
}
