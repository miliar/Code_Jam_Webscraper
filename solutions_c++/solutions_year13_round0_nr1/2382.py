// 2013_QA.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

// template

#include "stdafx.h"

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

//#define pb push_back
//#define all(v) v.begin(),v.end()
//#define rall(v) v.rbegin(),v.rend()
//#define sz size()
//#define rep(i,m) for(int i=0;i<(int)(m);i++)
//#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
//#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
//#define mem(a,b) memset(a,b,sizeof(a))
//#define mp make_pair
//#define dot(a,b) ((conj(a)*(b)).X)
//#define X real()
//#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
//#define vect(a,b) ((b)-(a))
//#define cross(a,b) ((conj(a)*(b)).imag())
//#define normalize(v) ((v)/length(v))
//#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
//#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
//
//typedef stringstream ss;
//typedef pair<int, int> pii;
//typedef vector<pii> vpii;
//typedef vector<string> vs;
//typedef vector<int> vi;
//typedef vector<double> vd;
//typedef vector<vector<int> > vii;
//typedef long long ll;
//typedef long double ld;
//typedef complex<double> point;
//typedef pair<point, point> segment;
//typedef pair<double, point> circle;
//typedef vector<point> polygon;

char a[4][4];
#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T;
	int ans;
	bool flag;
	int xwin, owin;
	cin >> T;
	for (int i = 1; i<=T; i++)
	{
		flag = true;
		for (int j=0; j<4; j++)
			for (int k=0; k<4; k++)
			{
				cin >> a[j][k];
				if (a[j][k] == '.') flag = false;
			}
		for (int j=0; j<4; j++)
		{
			xwin = 0; owin = 0;
			for (int k=0; k<4; k++)
			{
				if ((a[j][k] == 'X') || (a[j][k] == 'T')) xwin++;
				if ((a[j][k] == 'O') || (a[j][k] == 'T')) owin++;
			}
			if (xwin == 4) {cout << "Case #" << i << ": X won" << endl; goto the_end;}
			if (owin == 4) {cout << "Case #" << i << ": O won" << endl; goto the_end;}
		}
		for (int j=0; j<4; j++)
		{
			xwin = 0; owin = 0;
			for (int k=0; k<4; k++)
			{
				if ((a[k][j] == 'X') || (a[k][j] == 'T')) xwin++;
				if ((a[k][j] == 'O') || (a[k][j] == 'T')) owin++;
			}
			if (xwin == 4) {cout << "Case #" << i << ": X won" << endl; goto the_end;}
			if (owin == 4) {cout << "Case #" << i << ": O won" << endl; goto the_end;}
		}
		xwin=0; owin=0;
		for (int j=0; j<4; j++)
		{
			if ((a[j][j] == 'X') || (a[j][j] == 'T')) xwin++;
			if ((a[j][j] == 'O') || (a[j][j] == 'T')) owin++;

		}
					if (xwin == 4) {cout << "Case #" << i << ": X won" << endl; goto the_end;}
			if (owin == 4) {cout << "Case #" << i << ": O won" << endl; goto the_end;}
		xwin=0; owin=0;
		for (int j=0; j<4; j++)
		{
			if ((a[j][3-j] == 'X') || (a[j][3-j] == 'T')) xwin++;
			if ((a[j][3-j] == 'O') || (a[j][3-j] == 'T')) owin++;

		}
			if (xwin == 4) {cout << "Case #" << i << ": X won" << endl; goto the_end;}
			if (owin == 4) {cout << "Case #" << i << ": O won" << endl; goto the_end;}
		if (flag)
			cout << "Case #" << i << ": Draw" << endl;
		else
			cout << "Case #" << i << ": Game has not completed" << endl;
the_end: 
		continue;
	}
	return 0;
}







