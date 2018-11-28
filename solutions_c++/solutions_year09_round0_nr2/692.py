#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

int T, H, W;

int lat[104][104];
int a[104][104];
int cnt;
int dx[4] = {-1, 0, 0, 1};
int dy[4] = { 0, -1, 1, 0 };
int dfs(int i, int j)
{
	if(a[i][j]!=-1)
		return a[i][j];

	int p, best = -1, value = lat[i][j];
	int nexti, nextj;

	for( p = 0; p < 4; p++)
	{
		nexti = i + dx[p];
		nextj = j + dy[p];

		if(nexti >= H || nexti < 0 || nextj >= W || nextj < 0)
			continue;

		int tmp = lat[nexti][nextj];

		if( tmp < value)
		{
			best = p;
			value = tmp;
		}
	}

	if(best == -1)
		a[i][j] = cnt++;
	else
		a[i][j] = dfs(i + dx[best], j + dy[best]);

//	cout << " i = " << i << " j= " << j << " " << best << endl;

	return a[i][j];
}

int main()
{
	ifstream is("1.txt");
	ofstream os("2.txt");

	is >> T;

	int i, j, k;

	for(i=1; i<=T; i++)
	{
		is >> H >> W;

		for(j=0; j<H; j++)
			for(k=0; k<W; k++)
				is >> lat[j][k];
         
	    cnt = 0;
		
		memset(a, -1, sizeof(a));

		for(j=0; j<H; j++)
			for(k=0; k<W; k++){
					dfs(j, k);
			//		cout << endl;
			}


		os << "Case #" << i << ": " << endl;

		for(j=0; j<H; j++)
		{
			for(k=0; k<W; k++)
				os << char(a[j][k] + 'a') << " ";
			os << endl;
		}
		
	}

	os.close();
	is.close();

	return 0;
}



