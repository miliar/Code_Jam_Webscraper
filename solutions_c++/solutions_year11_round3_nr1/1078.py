#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iterator>
#include <map>
#include <list>
#include <string>
#include <sstream>
using namespace std;

#define ALL(X) X.begin(), X.end()
char pic[51][51];

int main()
{
	if( freopen("A-large.in", "rt", stdin) ) {
		freopen("A-large.out", "wt", stdout);
	} else 	if( freopen("A-small.in", "rt", stdin) ) {
		freopen("A-small.out", "wt", stdout);
	} else ( freopen("test.txt", "rt", stdin) );

	int T;
	cin >> T;

	for(int case_num = 1; case_num <= T; ++case_num)
	{
		int R, C;
		cin >> R >> C;
		for(int r = 0; r < R; ++r)
		for(int c = 0; c < C; ++c)
		{
			cin >> pic[r][c];
		}
		bool impossbile = false;
		for(int r = 0; !impossbile && r < R; ++r) {
			for(int c = 0; !impossbile && c < C; ++c)
			{
				if(pic[r][c] == '#') {
					if(pic[r+1][c] == '#' && pic[r][c+1] == '#' && pic[r+1][c+1] == '#')
						pic[r][c] = '/', pic[r+1][c+1] = '/', pic[r+1][c] = '\\', pic[r][c+1] = '\\';
					else impossbile = true;
				}
			}
			//impossbile = (pic[r][C-1] == '#');
		}
		//impossbile = (pic[R-1][C-1] == '#');
		cout << "Case #" << case_num << ":"<< endl;
		if(impossbile) cout << "Impossible" << endl;
		else {
				for(int r = 0; r < R; ++r) {
					for(int c = 0; c < C; ++c)
					{
						cout << pic[r][c];
					}
					cout << endl;
				}
		}
	}
	return 0;
}