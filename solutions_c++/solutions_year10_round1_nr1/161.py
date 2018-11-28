#include <iostream>
using namespace std;
int n,i,j,t,k,d,ncase,cases;
int dis[4][2] = {{0,1},{1,0},{1,1},{1,-1}};
bool br,bb;
char a[60][60];
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	cin >> cases;
	for (ncase=1; ncase<=cases; ncase++)
	{
		memset(a,0,sizeof(a));
		cin >> n >> k;
		for (i=1; i<=n; i++)
			for (j=1; j<=n; j++)
				cin >> a[i][j];
		for (t=1; t<=n; t++)
			for (i=1; i<=n; i++)
				for (j=n; j>=1; j--)
					if (a[i][j]=='.' && (a[i][j-1]=='R' || a[i][j-1]=='B'))
					{
						a[i][j] = a[i][j-1];
						a[i][j-1] = '.';
					}
		br = bb = false;
		for (i=1; i<=n; i++)
			for (j=1; j<=n; j++)
				for (d=0; d<4; d++)
				{
					for (t=0; t<k; t++)
						if (a[i+t*dis[d][0]][j+t*dis[d][1]]!='R')
							break;
					if (t>=k)
						br = true;
					for (t=0; t<k; t++)
						if (a[i+t*dis[d][0]][j+t*dis[d][1]]!='B')
							break;
					if (t>=k)
						bb = true;
				}
		cout << "Case #" << ncase << ": ";
		if (br && bb)
			cout << "Both" << endl;
		if (br && !bb)
			cout << "Red" << endl;
		if (!br && bb)
			cout << "Blue" << endl;
		if (!br && !bb)
			cout << "Neither" << endl;
	}
	return 0;
}