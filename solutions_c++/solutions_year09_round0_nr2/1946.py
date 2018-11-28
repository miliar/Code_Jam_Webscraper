#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

int fill(VVI& alt, VVI& ans, int r, int c, int& cnt)
{
	int dr[] = {
		-1, 0, 0, 1
	};
	int dc[] = {
		0, -1, 1, 0
	};
	if( ans[r][c] != -1 )
		return ans[r][c];
	
	int a = alt[r][c];
	int da = a;
	int ar, ac;
	// cout << r << ", " << c << endl;
	for(int i=0;i<4;i++)
	{
		int nr = dr[i] + r;
		int nc = dc[i] + c;
		if( nr < 0 || nr >= alt.size() || nc < 0 || nc >= alt[0].size() )
			continue;

		int na = alt[nr][nc];
		if( a > na ){
			a = na;
			ar = nr;
			ac = nc;
		}
	}
	if( a == da ){
		ans[r][c] = cnt;
		cnt++;
	} else {
		ans[r][c] = fill(alt, ans, ar, ac, cnt);
	}
	return ans[r][c];
}


int main()
{
	int ds;
	cin >> ds;

	for(int i=0;i<ds;i++)
	{
		int r, c;
		cin >> r >> c;
		VVI alt(r, VI(c));
		VVI ans(r, VI(c, -1));
		for(int ir=0;ir<r;ir++)
		{
			for(int ic=0;ic<c;ic++)
			{
				cin >> alt[ir][ic];
				// cout << alt[ir][ic] << " ";
			}
			// cout << endl;
		}
		int cnt = 0;
		cout << "Case #" << (i+1) << ":" << endl;
		for(int ir=0;ir<r;ir++)
		{
			for(int ic=0;ic<c;ic++)
			{
				fill(alt, ans, ir, ic, cnt);
				cout << (char)('a' + ans[ir][ic]) << " ";
				
			}
			cout << endl;
		}
		
	}
	return 0;
}

