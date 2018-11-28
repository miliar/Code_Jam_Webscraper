#include <iostream>
#define maxn 150
using namespace std;
int tn,r,num,ans,maxx,maxy;
bool map[2][maxn][maxn];

bool check(int x)
{
	for (int i=1;i<=maxx;i++)
		for (int j=1;j<=maxy;j++)
			if (map[x][i][j]) return true;
	return false;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C_small.out","w",stdout);
	int i,j,k;
	cin >> tn;
	for (int t=1;t<=tn;t++)
	{
		cin >> r;
		int x1,y1,x2,y2;
		num=maxx=maxy=0;
		memset(map,0,sizeof map);
		for (i=1;i<=r;i++)
		{
			cin >> x1 >> y1 >> x2 >> y2;
			maxx=max(max(x1,x2),maxx);
			maxy=max(max(y1,y2),maxy);
			for (j=x1;j<=x2;j++)
				for (k=y1;k<=y2;k++)
				{
					//if (!map[0][j][k]) num++;
					map[0][j][k]=true;
				}
		}
		if (!check(0))
		{
			cout << "Case #" << t << ": " << 0 << endl;
			continue;
		}
		for (ans=0;;ans++)
		{
			memset(map[(ans+1)%2],0,sizeof map[(ans+1)%2]);
			for (i=1;i<=maxx;i++)
				for (j=1;j<=maxy;j++)
				{
					if (map[ans%2][i][j])
					{
						if (map[ans%2][i-1][j] || map[ans%2][i][j-1])
							map[(ans+1)%2][i][j]=true;
					}
					else if (map[ans%2][i-1][j] && map[ans%2][i][j-1])
						map[(ans+1)%2][i][j]=true;
				}
			if (!check((ans+1)%2)) break;
		}
		cout << "Case #" << t << ": " << ans+1 << endl;
	}
}
