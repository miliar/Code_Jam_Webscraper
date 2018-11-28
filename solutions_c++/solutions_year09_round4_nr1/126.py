#include <cstdio>
#include <cstring>
#include <iostream>
#include <utility>
#include <set>
using namespace std;
#define M 50

char data[M][M];
int n;

set<pair<int,int> > table;
void read_data()
{
	cin >> n;
	int i,j;
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++) cin >> data[i][j];
}

void init()
{
	int i,j;
	int place;
	for (i=1;i<=n;i++)
	{
		place = -1;
		for (j=n;j>=1;j--) if (data[i][j] == '1')
		{
			place = j;
			break;
		}
		if (place == -1) table.insert(make_pair(i,0));
		else table.insert(make_pair(i,place));
	}
}

int work_ans()
{
	int res = 0,i,cnt;
	set<pair<int,int> > ::iterator it;
	for (i=1;i<=n;i++)
	{
		cnt = 0;
		for (it = table.begin();it != table.end();it++)
		{
			cnt++;
			if (it->second <= i)
			{
				res += cnt - 1;
				table.erase(it);
				break;
			}
		}
	}
	return res;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int ans,t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		read_data();
		init();
		ans = work_ans();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
