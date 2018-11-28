// google-code-jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstring>
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
#include <climits>
#include <cctype>



using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
//#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

#define SMALL

int N,nx;


int _tmain(int argc, _TCHAR* argv[])
{
#ifdef SMALL
	freopen("./data/2013/A-small-attempt0.in", "rt", stdin);
	freopen("./data/2013/A-small-attempt0.out", "wt", stdout);
#endif

#ifdef LARGE
	freopen("./data/2013/A-large.in", "rt", stdin);
	freopen("./data/2013/A-large.out", "wt", stdout);
#endif
	cin >> N;
	for (int nn=1; nn<=N; nn++){
		cout << "Case #" << nn << ": ";
		char playgroung[4][4];
		for (int row=0; row<4; row++) {
			cin >> playgroung[row][0];
			cin >> playgroung[row][1];
			cin >> playgroung[row][2];
			cin >> playgroung[row][3];
		}
		bool pased = false;
		string game_result = "Draw";
 		// check rows
		for (int row=0; row<4; row++) {
			char reference = playgroung[row][0];
			if (reference == '.'){
				pased = false;
				break;
			}
			if (reference == 'T') {
				reference = playgroung[row][1];
			}
			pased = true;
			for (int col=0;col<4;col++) {
				if ((reference != playgroung[row][col]) && (playgroung[row][col] != 'T')) {
					pased = false;
					break;
				}
			}
			if (pased) {
				game_result = reference;
				break;
			}
		}

		if (pased) {
			// write results
			cout << game_result << " won" << endl;
			continue;
		}

		// check cols
		for (int col=0; col<4; col++) {
			char reference = playgroung[0][col];
			if (reference == '.'){
				pased = false;
				break;
			}
			if (reference == 'T') {
				reference = playgroung[1][col];
			}
			pased = true;
			for (int row=0;row<4;row++) {
				if ((reference != playgroung[row][col]) && (playgroung[row][col] != 'T')) {
					pased = false;
					break;
				}
			}
			if (pased) {
				game_result = reference;
				break;
			}
		}

		if (pased) {
			// write results
			cout << game_result << " won" << endl;
			continue;
		}

		// check diagonal 1
		char reference = playgroung[0][0];
		if (reference == 'T') {
			reference = playgroung[1][1];
		}
		pased = true;
		for (int diag=0; diag<4; diag++) {
			if (((reference != playgroung[diag][diag]) && (playgroung[diag][diag] != 'T')) || (reference == '.')) {
				pased = false;
				break;
			}
		}
		if (pased) {
			game_result = reference;
			// write results
			cout << game_result << " won" << endl;
			continue;
		}

		// check diagonal 2
		reference = playgroung[0][3];
		if (reference == 'T') {
			reference = playgroung[1][1];
		}
		pased = true;
		for (int diag=0; diag<4; diag++) {			
			if (((reference != playgroung[diag][3-diag]) && (playgroung[diag][3-diag] != 'T')) || (reference == '.')) {
				pased = false;
				break;
			}
		}
		if (pased) {
			game_result = reference;
			// write results
			cout << game_result << " won" << endl;
			continue;
		}

		// check if finished
		pased = false;
		for (int col=0; col<4; col++) {
			for (int row=0;row<4;row++) {
				if (playgroung[row][col] == '.') {
					pased = true;
					break;
				}
			}
			if (pased) {
				game_result = "Game has not completed";
				break;
			}
		}

		// write results
		cout << game_result << endl;
	}
	return 0;
}

