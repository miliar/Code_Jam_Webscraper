#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define ALL(x) (x).begin(),(x).end()
#define TWO(X) (1<<(X))
#define EPS 1e-10
const double PI = acos(-1.0);

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }

////////////////////////////////////////////////////////////////////////////////////////////////////////

char a[4][4];
char temp[100];

bool judge(char xo)
{
	bool xwon(false);

	int xo_cnt(0), t_cnt(0);
	for(int i=0; i<4; i++) {
		xo_cnt = 0, t_cnt = 0;
		for(int j=0; j<4; j++) {
			if(a[i][j]==xo)		xo_cnt++;
			if(a[i][j]=='T')	t_cnt++;
		}
		if(xo_cnt==4 || (xo_cnt==3&&t_cnt==1))	xwon = true;
		xo_cnt = 0, t_cnt = 0;
		for(int j=0; j<4; j++) {
			if(a[j][i]==xo)		xo_cnt++;
			if(a[j][i]=='T')	t_cnt++;
		}
		if(xo_cnt==4 || (xo_cnt==3&&t_cnt==1))	xwon = true;
	}
	xo_cnt = 0, t_cnt = 0;
	for(int i=0; i<4; i++) {
		if(a[i][i]==xo)		xo_cnt++;
		if(a[i][i]=='T')	t_cnt++;
	}
	if(xo_cnt==4 || (xo_cnt==3&&t_cnt==1))	xwon = true;
	xo_cnt = 0, t_cnt = 0;
	for(int i=0; i<4; i++) {
		if(a[i][3-i]==xo)	xo_cnt++;
		if(a[i][3-i]=='T')	t_cnt++;
	}
	if(xo_cnt==4 || (xo_cnt==3&&t_cnt==1))	xwon = true;

	return xwon;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	for(int tc=1; tc<=T; tc++) {
		printf("Case #%d: ", tc);

		bool isDotThere = false;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				scanf("%c", &a[i][j]);
				if(a[i][j]=='.')	isDotThere = true;
			}
			scanf("%c", &temp[0]);
		}
		gets(temp);

		/*for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				fprintf(stderr, "%c", a[i][j]);
			}
			fprintf(stderr, "\n");
		}*/

		bool x_won = judge('X');
		bool o_won = judge('O');

		if(x_won)	printf("X won\n");
		else if(o_won)	printf("O won\n");
		else if(isDotThere)	printf("Game has not completed\n");
		else	printf("Draw\n");


		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}