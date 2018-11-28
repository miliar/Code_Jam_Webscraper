#include<cstdio>
#include<set>
#include<algorithm>
using namespace std;
struct datatype
{
	int begin,end;
	char start;
} data[200];
multiset<int> train[2];
int n[2],ans[2];
int rest;
bool cmp(datatype a, datatype b)
{
	if (a.begin == b.begin) return a.end < b.end; else return a.begin < b.begin;
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ca;
	scanf("%d\n",&ca);
	for (int cases = 1; cases <= ca; ++cases)
	{
		scanf("%d%d%d",&rest, n , n + 1);
		for (int i = 0; i < n[0] + n[1]; ++i)
		{
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			data[i].begin = h1 * 60 + m1;
			data[i].end = h2 * 60 + m2;
			if (i < n[0]) data[i].start = 'A'; else data[i].start = 'B';
		}
		train[0].clear(); train[0].insert(-1);
		train[1].clear(); train[1].insert(-1);
		ans[0] = ans[1] = 0;
		sort(data, data + n[0] + n[1], cmp);
		for (int i = 0; i < n[0] + n[1]; ++i)
		{
			int now = data[i].start - 'A';
			multiset<int>::iterator p = train[now].upper_bound(data[i].begin);
			--p;
			if (*p == -1) ++ans[now]; else train[now].erase(p);
			train[1 - now].insert(data[i].end + rest);
		}
		printf("Case #%d: %d %d\n",cases,ans[0],ans[1]);
	}
}
