#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000*1000*1000;
#define CL(x,a) memset(x,a,sizeof(x));
typedef long long LL;

int C;
LL gcd(LL a, LL b)
{
	return b ? gcd(b,a%b):a;
}
int  main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&C);
	for (int i=0;i<C;i++)
	{
		int n;
		scanf("%d",&n);
		vector<LL> v;
		v.resize(n);
		for (int j=0;j<n;j++)
		{
			scanf("%lld",&v[j]);
		}
		stack<LL> st;
		for (int j=0;j<n-1;j++)
		{
			st.push(abs(v[j]-v[j+1]));
		}
		while (st.size() > 1)
		{
			LL t1 = st.top(); st.pop();
			LL t2 = st.top(); st.pop();
			st.push(gcd(t2,t1));
		}
		LL res = st.top();
		if (res == 1)
			printf("Case #%d: 0",i+1);
		else
			printf("Case #%d: %lld",i+1,(res-(v[0]%res))%res);
		printf("\n");
	}
}
