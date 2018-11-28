#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<functional>
using namespace std;

int n;
int a[1000];
int b[1000];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		scanf("%d", &n);
		for(int i=0; i<n; i++)
			scanf("%d",a+i);
		for(int i=0; i<n; i++)
			scanf("%d", b+i);

		sort(a, a+n);
		sort(b, b+n, greater<int>());
		
		long long sum=0;
		for(int i=0; i<n; ++i)
		{
			sum+=(long long)a[i]*(long long)b[i];
		}
		//printf("Case #%d: %d\n", c, sum);
		cout << "Case #" << c <<": " << sum << endl; 
	}
	return 0;
}