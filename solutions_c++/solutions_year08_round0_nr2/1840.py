#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <math.h>
#include <string.h>
#include <string>


using namespace std;

#define CL(x) memset(x, 0, sizeof(x))

typedef long long LL;  

int readT()
{
	int h,m;
	scanf("%d:%d", &h, &m);
	return h * 60 + m;
}

struct node
{
	char f;
	char st;
	int t1,t2;
};

int c[2];
int ct[2];

int C(int g)
{
	if (c[g])
	{
		c[g]--;
	}
	else ct[g]++;
}

bool operator < (node a, node b)
{
	if (a.t1 != b.t1)
		return a.t1 < b.t1;
	if (a.f != b.f)
		return a.f < b.f;
}

int Solve()
{       
	ct[0] = ct[1] = c[0] = c[1] = 0;
	int T;
	scanf("%d", &T);
	int ca, cb;
	scanf("%d %d", &ca, &cb);
	multiset<node> st; 
	for (int i = 0; i < ca; i++)
	{
		node nd;
		nd.f = 1;
		nd.t1 = readT();
		nd.t2 = readT();
		nd.st = 0;
		st.insert(nd);
	}

	for (int i = 0; i < cb; i++)
	{
		node nd;
		nd.f = 1;
		nd.t1 = readT();
		nd.t2 = readT();
		nd.st = 1;
		st.insert(nd);
	}
	while (st.size() != 0)
	{
		node nd = *st.begin();
	//	printf("%d %d %d %d\n", nd.f, nd.st, nd.t1, nd.t2);
		st.erase(st.begin());
		if (!nd.f)
			c[nd.st]++;
		else
		{
			nd.f = 0;
			nd.t1 = nd.t2 + T;
			C(nd.st);
			nd.st = !nd.st;
			st.insert(nd);
		}
	}
	printf("%d %d\n", ct[0], ct[1]);
}

int main()
{ 	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
