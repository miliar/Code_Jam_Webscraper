#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int n,k;

int p[200][50];

int smaller(int r1,int r2)
{
	for (int j = 0;j<k;j++)
		if (p[r1][j] >= p[r2][j]) return 0;
	return 1;
}

bool vis[100];

int best = 0;

void search(int step,int take)
{
	if (take > best) return;
	if (step == n)
	{
		if (take <best) best = take;
	}

	for (int j = 0;j<step;j++) if (!vis[j])
			{
				if (smaller(j,step)) { 
					vis[j] = true; 
					search(step + 1 ,take);
					vis[j] = false;
				}
			}
	search(step + 1, take+1);
}

int main()
{
	int C;

	cin >> C ;
	for (int cc = 1; cc <= C ;cc ++)
	{
		cin >> n >> k;
		for (int i = 0;i<n;i++) 
			 for (int j = 0;j<k;j++)cin >> p[i][j];

		for (int i = 0;i<n;i++) 
			 for (int j = i+1;j<n;j++)
				 if (smaller(j,i))
					 for (int t = 0;t<k;t++)
						 swap(p[i][t],p[j][t]);


		int ans = 0;
		bool used[200];
		memset(used,0,sizeof(used));
		for (int i = 0;i<n;i++)
		{
			bool flag = false;
			for (int j = 0;j<i;j++) if (!used[j])
			{
				if (smaller(j,i)) { used[j] = true; flag = true; break;}
			}
			if (!flag) ans++;
		}

		best = 1 << 30;
		memset(vis,0,sizeof(vis));
		search(0 , 0 );
		ans = best;
		printf("Case #%d: %d\n", cc, ans);

	}
	return 0;
}