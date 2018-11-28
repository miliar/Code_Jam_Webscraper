#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<string>

using namespace std;

const int inf = 2147483647;
const double eps = 1e-8;
const double pi = acos(-1.0);

const int maxn = 2000;

map<int,int> a;
int N,P,C;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int ntest;
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d",&N);
		a.clear();
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",&P,&C);
			a[P+maxn/2] = C;
		}
		int ans = 0;
		bool changed = true;
		while(changed)
		{
			changed = false;
			for(map<int,int>::iterator it=a.begin();it!=a.end();it++)
			{
				int i = it->first;
				while(it->second>=2)
				{
					changed = true;
					a[i-1]++;
					a[i+1]++;
					it->second-=2;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
