#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>
using namespace std;
int T;
int R,k,N;
char C;
int main()
{
	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);
	scanf("%d",&T);

	for(int t = 1;t <= T;t++)
	{
		char da[4][5];
		for(int i = 0;i < 4; ++i) {
			scanf("%s", da[i]);
		}
		string res = "";
		bool isfin = true;
		for(int i = 0;i < 4;++i) {
			if ((da[i][0] == 'X' ||  da[i][0] == 'T') && 
				(da[i][1] == 'X' ||  da[i][1] == 'T') && 
				(da[i][2] == 'X' ||  da[i][2] == 'T') && 
				(da[i][3] == 'X' ||  da[i][3] == 'T')) {
				res = "X won";
				break;
			}
			if ((da[i][0] == 'O' ||  da[i][0] == 'T') && 
				(da[i][1] == 'O' ||  da[i][1] == 'T') && 
				(da[i][2] == 'O' ||  da[i][2] == 'T') && 
				(da[i][3] == 'O' ||  da[i][3] == 'T')) {
				res = "O won";
				break;
			}
			if ((da[0][i] == 'X' ||  da[0][i] == 'T') && 
				(da[1][i] == 'X' ||  da[1][i] == 'T') && 
				(da[2][i] == 'X' ||  da[2][i] == 'T') && 
				(da[3][i] == 'X' ||  da[3][i] == 'T')) {
				res = "X won";
				break;
			}
			if ((da[0][i] == 'O' ||  da[0][i] == 'T') && 
				(da[1][i] == 'O' ||  da[1][i] == 'T') && 
				(da[2][i] == 'O' ||  da[2][i] == 'T') && 
				(da[3][i] == 'O' ||  da[3][i] == 'T')) {
				res = "O won";
				break;
			}
			for(int j = 0; j < 4; ++j) {
				if (da[i][j] == '.') {
					isfin = false;
				}
			}
		}
		if (res == "") {
			if ((da[0][0] == 'X' ||  da[0][0] == 'T') && 
			(da[1][1] == 'X' ||  da[1][1] == 'T') && 
			(da[2][2] == 'X' ||  da[2][2] == 'T') && 
			(da[3][3] == 'X' ||  da[3][3] == 'T')) {
				res = "X won";
			}
		if ((da[0][0] == 'O' ||  da[0][0] == 'T') && 
			(da[1][1] == 'O' ||  da[1][1] == 'T') && 
			(da[2][2] == 'O' ||  da[2][2] == 'T') && 
			(da[3][3] == 'O' ||  da[3][3] == 'T')) {
				res = "O won";
		}
		if ((da[0][3] == 'X' ||  da[0][3] == 'T') && 
			(da[1][2] == 'X' ||  da[1][2] == 'T') && 
			(da[2][1] == 'X' ||  da[2][1] == 'T') && 
			(da[3][0] == 'X' ||  da[3][0] == 'T')) {
				res = "X won";
		}
		if ((da[0][3] == 'O' ||  da[0][3] == 'T') && 
			(da[1][2] == 'O' ||  da[1][2] == 'T') && 
			(da[2][1] == 'O' ||  da[2][1] == 'T') && 
			(da[3][0] == 'O' ||  da[3][0] == 'T')) {
				res = "O won";
		}
		}
		if (res != "") {
			printf("Case #%d: %s\n", t, res.c_str());
		} else if(!isfin) {
			printf("Case #%d: Game has not completed\n", t);
		} else {
			printf("Case #%d: Draw\n", t);
		}
	}
	return 0;
}