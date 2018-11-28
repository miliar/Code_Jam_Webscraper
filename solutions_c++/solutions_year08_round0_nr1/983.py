#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(a,n) for(a=0;a<n;a++)
#define memset0(v) memset(v,0,sizeof(v))
typedef vector<string> vs;
typedef vector<int> vi;


int switches[1002][102];

int main()
{
	int a,b,c,d,tests;
	int S,Q;
	char buf[200];
	string query;
	vs engines;

	freopen("a2.in", "rt", stdin);
	freopen("a2.out", "wt", stdout);

	scanf("%d", &tests);

for(int test=0;test<tests;test++)
{

	engines.clear();
	memset0(switches);

	scanf("%d\n",&S);
	fo(a,S)
	{
		gets(buf);
		engines.push_back(string(buf));
	}

	scanf("%d\n",&Q);
	for(a=1;a<=Q;a++)
	{
		gets(buf);
		query = string(buf);
		
		fo(b,S)
		if(query!=engines[b])
		{
			d=1000000;
			fo(c,S)
			if(switches[a-1][c]>=0)
			{
				if(c!=b && switches[a-1][c]+1<d || c==b && switches[a-1][c]<d)
				{
					d=(c!=b ? switches[a-1][c]+1 : switches[a-1][c]);
				}
			}

			if (d<1000000) switches[a][b]=d; else switches[a][b]=-1;
		}
		else
			switches[a][b]=-1;
	}

	c=1000000;
	if(Q==0)
		c=0;
	else
	{
		fo(a,S)
		if(switches[Q][a]>=0)
			c=min(c,switches[Q][a]);
	}
	printf("Case #%d: %d\n", test+1, c);

}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
