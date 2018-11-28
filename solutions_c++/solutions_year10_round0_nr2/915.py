#include<iostream>
#include<algorithm>
using namespace std;
typedef long long LL;
const int maxn=1001;
int a[maxn];
int gcd(int x,int y)
{
	int r;
	if(x<y){r=x;x=y;y=r;}
	while(y)
	{
		  r=x%y;
		  x=y;
		  y=r;
		  }
    return x;		  
	}
int main()
{
	int i,j,k,c,test,count=1,n;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&test);
	while(test--)
	{
		  scanf("%d",&n);
		  for(i=0;i<n;i++)scanf("%d",&a[i]);
		  sort(a,a+n);
		  k=a[1]-a[0];
		  for(i=1;i<n;i++)k=gcd(k,a[i]-a[i-1]);
		  a[0]%=k;
		  a[0]=(k-a[0])%k;
		  printf("Case #%d: %d\n",count++,a[0]);	  			  
		  }
	return 0;
	}











