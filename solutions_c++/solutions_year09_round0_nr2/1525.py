#include <iostream>
using namespace std;
int dr[4]={-1,0,0,1};
int dc[4]={0,-1,1,0};
int basins;
int a[100][100];
int id[100][100];
int R,C;
int calc_basin(int r,int c)
{
	if (id[r][c])
		return id[r][c];
	int bestr=r; int bestc=c; int i;
	for (i=0; i<4; i++)
	{
		int r2=r+dr[i];
		int c2=c+dc[i];
		if (r2>=0&&r2<R&&c2>=0&&c2<C&&a[r2][c2]<a[bestr][bestc])
			bestr=r2,bestc=c2;
	}
	if (bestr==r&&bestc==c) //this is a previously unknown sink
		return id[r][c]=basins++;
	return id[r][c]=calc_basin(bestr,bestc);
}
int main()
{
	int i,T,j,k;
	cin.sync_with_stdio(false);
	cin >> T;
	for (i=1; i<=T; i++)
	{
		basins='a';
		cin >> R >> C;
		for (j=0; j<R; j++)
			for (k=0; k<C; k++)
			{
				cin >> a[j][k];
				id[j][k]=0;
			}
		cout << "Case #" << i << ":" << endl;
		for (j=0; j<R; j++)
		{
			for (k=0; k<C; k++)
				cout << char(calc_basin(j,k)) << ' ';
			cout << endl;
		}
	}
	return 0;
}