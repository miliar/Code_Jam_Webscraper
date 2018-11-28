#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
using namespace std;
#define sz size()
#define pb push_back
#define FOR(i,a,b) for(int i = a; i < b; ++i)

char c[5][5];

int check(char a, char b, char c, char d)
{
	if (a == '.' || b == '.' || c == '.' || d == '.') return 0;
	if (a == 'T') a = b;
	if (b == 'T') b = a;
	if (c == 'T') c = a;
	if (d == 'T') d = a;
	if (a != b || b != c || c != d)
		return 0;
	if (a == 'X') return 1;
	return -1;
}

int check()
{
	FOR(i,0,4)
	{
		int x = check(c[i][0],c[i][1],c[i][2],c[i][3]);
		if (x != 0) return x;
		x = check(c[0][i],c[1][i],c[2][i],c[3][i]);
		if (x != 0) return x;
	}
	int x = check(c[0][0], c[1][1], c[2][2], c[3][3]);
	if (x != 0) return x;
	x = check(c[3][0], c[2][1], c[1][2], c[0][3]);
	if (x != 0) return x;
	
	FOR(i,0,4)
	FOR(j,0,4)
		if (c[i][j] == '.') return 0;
	return 78;
}

int main()
{
	freopen ("in1.txt", "r", stdin);
	freopen ("out1.txt", "w", stdout);
	
	int ppp;
	cin >> ppp;
	FOR(o,0,ppp)
	{
		cout << "Case #" << o + 1 << ": ";
		cin >> c[0] >> c[1] >> c[2] >> c[3];
		int x = check();
		if (x == 1) cout << "X won";
		if (x == -1) cout << "O won";
		if (x == 0) cout << "Game has not completed";
		if (x == 78) cout << "Draw";
		cout << endl;
	}	
	return 0;
}
