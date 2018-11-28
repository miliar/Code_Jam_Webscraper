#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
void Solve(int);

int main()
{
	int n;
scanf("%d",&n);
	for(int i=0;i<n;i++) Solve(i+1);
	return 0;
}
void Solve(int x)
{
	int p,k,l;
	long long r=0;
	vector <long long> Fr;
	scanf("%d %d %d\n",&p,&k,&l);
	for(int i=0;i<l;i++)
	{
		long long t;
		scanf("%lld ",&t);
		Fr.push_back(t);
	}
	sort(Fr.begin(),Fr.end(),greater<long long>());
	for(int i=0;i<l;i++)
	{
//		printf("%d ",Fr[i]);
		r+=Fr[i]*(i/k + 1);
	}
	printf("Case #%d: %lld\n",x,r);
}
