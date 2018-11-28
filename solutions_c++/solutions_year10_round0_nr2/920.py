#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int n;
int b[100];
int a[110];
int cmp(int a,int b)
{
	return a>b;
}

int gcd(int a,int b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}

int main()
{
	int t,i;
	int cs=0;
	freopen("1.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
  scanf("%d",&n);
   for(i=0;i<n;i++)
   {
	   scanf("%d",&a[i]);
   }
   sort(a,a+n,cmp);
   for(i=1;i<n;i++) b[i]=a[i-1]-a[i];
   int d;
   d=b[1];
   for(i=2;i<n;i++) d=gcd(d,b[i]);
   printf("Case #%d: ",++cs);
   int ys=a[0]%d;
   if(ys==0)
   {
	   printf("0\n");
	   continue;
   }
   else printf("%d\n",d-ys);
	}
	return 0;
}


