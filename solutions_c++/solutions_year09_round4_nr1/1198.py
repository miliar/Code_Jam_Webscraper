#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
#include<fstream>
#include<cmath>

using namespace std;

typedef long long int64;

vector<int64> v;
set<vector<int64> > done;
int n;
int64 mod[100];

int check(const vector<int64> & c)
{
	for(int i=0; i<n; ++i)
	{
		if(c[i] & mod[i])
			return false;
		//for(int j=i+1; j<n; j++)
		//{
		//	if(c[i] & (1LL<<(63-j)))
		//		return false;
		//}
	}
	return true;
}

typedef pair<vector<int64>, int> pr;

int bfs(const vector<int64>& c)
{
	queue<pr> q;

	q.push(pr(c, 0));
	
	while(!q.empty())
	{
		vector<int64> cur (q.front().first);
		int dist = q.front().second;
		q.pop();

		if(check(cur))
			return dist;
		
		vector<int64> tmp;
		for(int i=0; i+1<n; ++i)
		{
			tmp = cur;
			swap(tmp[i], tmp[i+1]);
			if(done.find(tmp) == done.end())
			{
				q.push(pr(tmp, dist+1));
				done.insert(tmp);
			}
		}
	}
	return -1;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		v.clear();
		done.clear();
		scanf("%d", &n);
		v.resize(n, 0);

		for(int i=0; i<n; ++i)
		{
			int tmp;
			char buf[102];
			scanf("%s", buf);
			for(int j=0; j<n; j++)
			{
				if(buf[j]=='1')
					v[i] |= (1LL<<(63-j));
			}
		}

		mod[n-1]=0;
		for(int i=n-2; i>=0; i--)
		{
		//	if(i==0)
		//		mod[i] = (1LL << 62);
		//	else		
			mod[i] = mod[i+1] | (1LL << (63-(i+1)));
		}

		int ans = bfs(v);
		printf("Case #%d: %d\n", c, ans);
	}

	return 0;
}
