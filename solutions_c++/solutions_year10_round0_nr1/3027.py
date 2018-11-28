#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstring>
using namespace std;

int a[200];
int n,k;

bool check()
{
	int i;
	for(i=0;i<n;i++) if(!a[i]) return false;
	return true;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("2.out","w",stdout);
   int t;
   int i;
   scanf("%d",&t);
   int cs=0;
   while(t--)
   {
	   scanf("%d%d",&n,&k);
	   int len=0;
	   memset(a,0,sizeof(a));
		   while(k>0)
		   {
			   a[len++]=k%2;
			   k/=2;
		   }
	   printf("Case #%d: ",++cs);

	   if(check()) printf("ON\n");
	   else printf("OFF\n");
   }
   return 0;
}


        
