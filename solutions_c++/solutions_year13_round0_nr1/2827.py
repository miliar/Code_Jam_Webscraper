#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdio>
#include <sstream>
#include <queue>

using namespace std;

#define MAXN 12000
#define pi pair <int, int>
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a.size())

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef double D;
typedef vector<D> VD;
typedef vector<VD> VVD;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

int flag, T;
string s[4];


int main (int argc, char const* argv[])
{
	cin >> T;
	for (int cs = 1; cs <= T; cs += 1)
	{
		for (int i = 0; i < 4; i += 1)
			cin >> s[i];
		cout << "Case #" << cs << ": ";
		flag = 0;
		for (int i = 0; i < 4; i += 1)
		{
			if( (s[i][0] == 'X' || s[i][0] == 'T') && (s[i][1] == 'X' || s[i][1] == 'T') && (s[i][2] == 'X' || s[i][2] == 'T') && (s[i][3] == 'X' || s[i][3] == 'T') )
			{
				cout << "X won\n";
				flag = 1;
			}
			else if( (s[0][i] == 'X' || s[0][i] == 'T') && (s[1][i] == 'X' || s[1][i] == 'T') && (s[2][i] == 'X' || s[2][i] == 'T') && (s[3][i] == 'X' || s[3][i] == 'T') )
			{
				cout << "X won\n";
				flag = 1;
			}
			else if( (s[i][0] == 'O' || s[i][0] == 'T') && (s[i][1] == 'O' || s[i][1] == 'T') && (s[i][2] == 'O' || s[i][2] == 'T') && (s[i][3] == 'O' || s[i][3] == 'T') )
			{
				cout << "O won\n";
				flag = 1;
			}
			else if( (s[0][i] == 'O' || s[0][i] == 'T') && (s[1][i] == 'O' || s[1][i] == 'T') && (s[2][i] == 'O' || s[2][i] == 'T') && (s[3][i] == 'O' || s[3][i] == 'T') )
			{
				cout << "O won\n";
				flag = 1;
			}
			if(flag)
				break;
		}
		if(flag)
			continue;
		if( (s[0][0] == 'X' || s[0][0] == 'T') && (s[1][1] == 'X' || s[1][1] == 'T') && (s[2][2] == 'X' || s[2][2] == 'T') && (s[3][3] == 'X' || s[3][3] == 'T') )
		{
			cout << "X won\n";
			flag = 1;
		}
		else if( (s[3][0] == 'X' || s[3][0] == 'T') && (s[2][1] == 'X' || s[2][1] == 'T') && (s[1][2] == 'X' || s[1][2] == 'T') && (s[0][3] == 'X' || s[0][3] == 'T') )
		{
			cout << "X won\n";
			flag = 1;
		}
		else if( (s[0][0] == 'O' || s[0][0] == 'T') && (s[1][1] == 'O' || s[1][1] == 'T') && (s[2][2] == 'O' || s[2][2] == 'T') && (s[3][3] == 'O' || s[3][3] == 'T') )
		{
			cout << "O won\n";
			flag = 1;
		}
		else if( (s[3][0] == 'O' || s[3][0] == 'T') && (s[2][1] == 'O' || s[2][1] == 'T') && (s[1][2] == 'O' || s[1][2] == 'T') && (s[0][3] == 'O' || s[0][3] == 'T') )
		{
			cout << "O won\n";
			flag = 1;
		}
		if(flag)
			continue;
		for (int i = 0; i < 4; i += 1)
		{
			for (int j = 0; j < 4; j += 1)
			{
				if(s[i][j] == '.')
				{
					flag = 1;
					cout << "Game has not completed\n";
					break;
				}
			}
			if(flag)
				break;
		}
		if(!flag)
			cout << "Draw\n";
	}
	return 0;
}










