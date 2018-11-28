#include <cstdio>
#include <cstdlib>
#include <iostream>

#define ll long long
using namespace std;

ll st[40];

int main()
{
	freopen("test.in","r", stdin);
	freopen("test.out","w", stdout);

	st[0]=1;
	for (int i=1; i<=31; ++i) st[i]=st[i-1]*2;

	int t; scanf("%d", &t);
	for (int i=1; i<=t; ++i) {
		int n,k;
		scanf("%d%d",&n,&k);
		ll c=st[n];
		printf("Case #%d: %s\n", i,  ((k+1)%c) ? ("OFF") : ("ON")  );
	}

	return 0;
}
