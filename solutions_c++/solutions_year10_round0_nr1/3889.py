#include<iostream>
using namespace std;
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
typedef long long lld;
#define FF(i,a)				for( int i = 0 ; i < a ; i ++ )
#define PP(n,m,a)			puts("---");FF(i,n){FF(j,m)cout << a[i][j] << ' ';puts("");}
#define N 40
int a[N];
int main()
{
	freopen("b.txt","w",stdout);
	int t;
	scanf("%d",&t);
	a[1]=2;
	for(int i=2;i<=30;i++)
	a[i]=a[i-1]*2;
	int n,k;
	int csn=1;
	while(t--)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",csn++);
		if(k%a[n]==a[n]-1)
		{
			printf("ON\n");
		}
		else
		{
			printf("OFF\n");
		}
	}
	
	return 0;
}
