#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int n;

string x[4];

void init_deal(){
}

bool check(char ch){
	int ax[2][4] = {{0,1,2,3},{0,1,2,3}},
		ay[2][4] = {{0,1,2,3},{0,-1,-2,-3}};
	for (int i = 0; i<4; i++)
	{
		bool yes = true;
		for (int j = 0; j<4; j++)
		if(x[i][j] != ch && x[i][j] != 'T')
		{
			yes = false;
			break;
		}
		if(yes)
			return true;

		yes = true;
		for (int j = 0; j<4; j++)
		if(x[j][i] != ch && x[j][i] != 'T')
		{
			yes = false;
			break;
		}
		if(yes)
			return true;
	}
	int sx = 0,
		sy = 0;
	bool yes = true;
	for (int i = 0; i<4; i++)
	{
		int nx = sx+ax[0][i],
			ny = sy+ay[0][i];
		if(x[nx][ny] != ch && x[nx][ny] != 'T'){
			yes = false;
			break;
		}
	}
	if(yes)
		return true;

	sx = 0,
	sy = 3;
	yes = true;
	for (int i = 0; i<4; i++)
	{
		int nx = sx+ax[1][i],
			ny = sy+ay[1][i];
		if(x[nx][ny] != ch && x[nx][ny] != 'T'){
			yes = false;
			break;
		}
	}
	if(yes)
		return true;

	return false;
}

bool finished(){
	for (int i = 0; i<4; i++)
	for (int j = 0; j<4; j++)
	if(x[i][j] == '.'){
		return false;
	}
	return true;
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	string s;
	for(int ttt = 1;ttt<=tttt;ttt++){
		printf("Case #%d: ",ttt);
		getline(cin, s);

		for (int i = 0; i<4; i++)
		{
			getline(cin, x[i]);
		}

		bool x_won = check('X');
		bool o_won = check('O');
		bool end = finished();

		if(x_won)
			printf("X won\n");
		else
		if(o_won)
			printf("O won\n");
		else
		if(end)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	

	return 0;
};

