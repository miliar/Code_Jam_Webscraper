#include <cstdio>
#include <iostream>
#include <memory.h>
#include <vector>
using namespace std;

const int MAX_N = 1024;

int n, l, h;
int f[MAX_N];

void input()
{
	scanf("%d%d%d", &n, &l, &h);

	for(int i=0; i<n; i++)
		scanf("%d", &f[i]);
}

bool can(int i)
{
	for(int j=0; j<n; j++)
		if (f[j] % i && i % f[j])
			return 0;
			
	return 1;
}

int solve()
{
	for(int i=l; i<=h; i++)
		if(can(i))
			return i;
			
	return -1;
}

void output(int t, int ans)
{
	printf("Case #%d: ", t);
	
	if(ans==-1) printf("NO\n");
	else printf("%d\n", ans);
}

int main()
{
	int i, t;
	scanf("%d", &t);

	for(i=1; i<=t; i++) {
		input();
		output(i, solve());
	}
	
	return 0;
}
