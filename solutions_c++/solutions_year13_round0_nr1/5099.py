#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <typeinfo>
#include <cmath>


#define fi first
#define se second
#define pbk push_back
#define mpr make_pair
#define ins insert
#define ii pair<int,int>
#define iii pair<int,ii>
#define fori(x,y) for(__typeof(x) i = (x),__y(y);i!=__y;i++)
#define forj(x,y) for(__typeof(x) j = (x),__y(y);j!=__y;j++)
#define fork(x,y) for(__typeof(x) k = (x),__y(y);k!=__y;k++)
#define ford(i,x,y) for(typeof(x) i = (x)-1,__y(y);i!=__y;i--)
#define openfile freopen("inp.txt","r",stdin); freopen("out.txt","w",stdout);
#define closefile fclose(stdin); fclose(stdout);
#define mset(a) memset(a,0,sizeof(a));
#define aset(a,size,val) for(int i = 0;i<size;i++) a[i] = val;
#define ll long long
#define abs(x) (x<0? -x:x)
#define sqr(x) ((x) * (x))
using namespace std;

int gcd(int a,int b) {return (!b? a:gcd(b,a%b));}
string toString(double x) {ostringstream cv; cv << x;return cv.str();}
int toInt(string x) {int n;return (istringstream(x) >> n ? n:0);}
char toChar(int x) {return char(int('0') + x);}
string toBase(ll x,int y) {string s("");while(x) {s=toChar(x%2)+s;x/=2;}return s;}
const double pi = 2*acos(0.0);
const int oo = 100000000;
const int maxn = 102;

const string O[5] = {"OOOO", "OOOT", "OOTO", "OTOO", "TOOO"};
const string X[5] = {"XXXX", "XXXT", "XXTX", "XTXX", "TXXX"};

char map[4][4];
int test(int x,int y,int u,int v) {
	string st("");
	for(int i = 0;i<4;i++) {
		st += map[x][y];
		x += u; y += v;
	}
	//cout << st << endl;
	for(int i = 0;i<5;i++) 
		if (X[i] == st) return 1;
	for(int i = 0;i<5;i++) 
		if (O[i] == st) return -1;	
	return 0;
}
string solve() {
	for(int i = 0;i<4;i++) {
		int x = test(0,i,1,0);
		if (x == 1) return "X won";
		if (x == -1) return "O won";
		x = test(i,0,0,1);
		if (x == 1) return "X won";
		if (x == -1) return "O won";		
	}
	int x = test(0,0,1,1);
	if (x == 1) return "X won";
	if (x == -1) return "O won";	
	
	x = test(0,3,1,-1);
	if (x == 1) return "X won";
	if (x == -1) return "O won";	

	for(int i = 0;i<4;i++)
		for(int j = 0;j<4;j++)
			if (map[i][j] == '.')
				return "Game has not completed";
	return "Draw";
}
int main() {
	openfile
	int T;
	scanf("%d\n",&T);
	for(int i = 0;i<T;i++) {
		for(int j = 0;j<4;j++) {
			for(int k = 0;k<4;k++)
				scanf("%c",&map[j][k]);
			scanf("\n");
		}
		scanf("\n");

		cout <<"Case #" << i+1 <<": " << solve() << endl;
	}
	closefile
	return 0;
}
