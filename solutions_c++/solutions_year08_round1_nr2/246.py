#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
#include <iostream>
using namespace std;

#define M 110

int n,m;

vector<pair<int,int> > data[M];

int ans,cnt = 10000;
void read_data()
{
	cin >> n >> m;
	int i,d,X,Y;
	for (i=0;i<m;i++)
	{
		data[i].clear();
		cin >> d;
		while (d--)
		{
			cin >> X >> Y;
			X--;
			data[i].push_back(make_pair(X,Y));
		}
	}
	cnt = 10000;
}

void show_ans()
{
	int i;
	if (cnt == 10000) printf("IMPOSSIBLE\n");
	else
	{
		for (i=0;i<n;i++)
		{
			if (i) printf(" ");
			if ((1 << i) & ans) printf("1");
			else printf("0");
		}
		printf("\n");
	}
}

int Cnt(int s)
{
	int i,res = 0;
	for (i=0;i<n;i++) if (s & (1 << i)) res++;
	return res;
}

bool ok(int p,int s)
{
	int i,temp;
	for (i=0;i<data[p].size();i++)
	{
		temp = data[p][i].first;
		if (s & (1 << temp))
		{
			if (data[p][i].second == 1) return true;
		}
		else
		{
			if (data[p][i].second == 0) return true;
		}
	}
	return false;
}
bool check(int s)
{
	int i;
	for (i=0;i<m;i++) if (!ok(i,s)) return false;
	return true;
}

void work_ans()
{
	int i;
	for (i=0;i<(1 << n);i++)
	{
		if (check(i))
		{
			if (Cnt(i) < cnt)
			{
				ans = i;
				cnt = Cnt(i);
			}
		}
	}
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t,i;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		read_data();
		work_ans();
		show_ans();
	}
	return 0;
}
