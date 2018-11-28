#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#define sz(a) ((int)(a).size())
#define foreach(i, Type, v) for(Type::iterator i=v.begin(); i!=v.end(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Item;

const int Maxn = 1000+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int compareTo(double a, double b) { return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

bool check(vector<string> s, char ch)
{
	string cmp, t;

	for(int i=0; i<4; i++)
		cmp += ch;
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if( s[i][j] == 'T' )
				s[i][j] = ch;
	for(int i=0; i<4; i++)
		if( s[i] == cmp )
			return true;
	for(int j=0; j<4; j++)
	{
		t = "";
		for(int i=0; i<4; i++)
			t += s[i][j];
		if( t == cmp )
			return true;
	}
	t = "";
	for(int i=0; i<4; i++)
		t += s[i][i];
	if( t == cmp )
		return true;
	t = "";
	for(int i=0; i<4; i++)
		t += s[i][3-i];
	if( t == cmp )
		return true;
	return false;
}

int main()
{
	int cas;
	ios::sync_with_stdio(0);
	freopen("aaa.in", "r", stdin);
	freopen("aaa.out", "w", stdout);

	cin>>cas;
	for(int c=1; c<=cas; c++)
	{
		vector<string> s(4);
		for(int i=0; i<4; i++)
			cin>>s[i];

		printf("Case #%d: ", c);
		if( check(s, 'X') )
			printf("X won\n");
		else if( check(s, 'O') )
			printf("O won\n");
		else
		{
			bool flags = false;
			for(int i=0; i<4; i++)
				for(int j=0; j<4; j++)
					if( s[i][j] == '.' )
						flags = true;
			if( flags )
				printf("Game has not completed\n");
			else
				printf("Draw\n");
		}
	}

	return 0;
}
