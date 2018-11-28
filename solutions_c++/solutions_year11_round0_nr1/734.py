#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;
#define M 1100

int n;
pair<char,int> data[M];
void read_data()
{
	cin >> n;
	int i;
	for (i=1;i<=n;i++) cin >> data[i].first >> data[i].second;
}

inline int iabs(int s)
{
	if (s < 0) return -s; else return s;
}

int meet[M];
int work_ans()
{
	int i,j;
	memset(meet,0,sizeof(0));
	meet[1] = data[1].second;
	for (i=1;i<n;i++)
	{
		if (data[i + 1].first == data[i].first) meet[i + 1] = meet[i] + iabs(data[i + 1].second - data[i].second) + 1;
		else
		{
			for (j=i;j>=1;j--) if (data[j].first == data[i + 1].first) break;
			if (j == 0)
			{
				meet[i + 1] = max(data[i + 1].second - 1, meet[i]) + 1;
			}
			else
			{
				meet[i + 1] = max(iabs(data[i + 1].second - data[j].second) + meet[j], meet[i]) + 1;
			}
		}
	}
	return meet[n];
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
		ans = work_ans();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}