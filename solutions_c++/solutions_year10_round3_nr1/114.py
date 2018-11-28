#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
using namespace std;

int a[2000],b[2000];
void solve()
{
	int n;
	scanf("%d",&n);
	int count = 0;
	for(int i=0;i<n;i++)
	{
		scanf("%d%d",&a[i],&b[i]);
		for(int j=0;j<i;j++)
		{
			if((a[j]>a[i] && b[j]<b[i]) || (a[j]<a[i] && b[j]>b[i]))
				count ++;
		}
	}
	printf("%d\n",count);

}

int main()
{


	int Ti,T;
	scanf("%d",&T);
	for(Ti = 1; Ti <= T; Ti++)
	{
		printf("Case #%d: ",Ti);
		solve();
	}
}
