#include <iostream>
#include <algorithm>
using namespace std;
#define M 110

const int hh[4] = {-1,0,0,1};
const int ll[4] = {0,-1,1,0};

int n,m;
int data[M][M];
int ans[M][M];
void read_data()
{
	cin >> n >> m;
	int i,j;
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++) cin >> data[i][j];
}

void show_ans()
{
	int i,j;
	for (i=1;i<=n;i++)
	{
		for (j=1;j<m;j++) printf("%c ",ans[i][j] + 'a');
		printf("%c\n",ans[i][m] + 'a');
	}
}

int cnt;
void Fill(int a,int b)
{
	int tempa,tempb;
	int i;
		tempa = tempb = -1;
		for (i=0;i<4;i++)
		{
			if (a + hh[i] > n || a + hh[i] < 1 || b + ll[i] > m || b + ll[i] < 1) continue;
			if (data[a + hh[i]][b + ll[i]] >= data[a][b]) continue;
			if (tempa == -1 || data[a + hh[i]][b + ll[i]] < data[tempa][tempb])
			{
				tempa = a + hh[i];
				tempb = b + ll[i];
			}
		}
		if (tempa == -1)
		{
			ans[a][b] = cnt++;
			return;
		}
		if (ans[tempa][tempb] != -1)
		{
			ans[a][b] = ans[tempa][tempb];
			return;
		}
		Fill(tempa,tempb);
		ans[a][b] = ans[tempa][tempb];
}

void work_ans()
{
	memset(ans,-1,sizeof(ans));
	int i,j;
	cnt = 0;
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++) if (ans[i][j] == -1)
			Fill(i,j);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B_large.out","w",stdout);
	int t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		read_data();
		work_ans();
		printf("Case #%d:\n",i);
		show_ans();
	}
	return 0;
}
