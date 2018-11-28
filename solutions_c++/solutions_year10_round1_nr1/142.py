#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <cstdarg>

#ifndef DBG
#define	DBG	0
#endif

//#define	DBG(f,x)	if(_____debug & f) { x; }
using namespace std;

#define	rep(i,n)	for((i) = 0; (i) < (n); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define all(v)		(v).begin(),(v).end()
#define	Fi(n)		rep(i,n)
#define	Fj(n)		rep(j,n)
#define	Fk(n)		rep(k,n)
#define	sz(v)		(v).size()

// {{{ gprintf for debugging
bool gprintf(int debug,const char *format,...) {
	if(DBG & debug) {
		va_list	listpointer;

		va_start(listpointer, format);
		vfprintf(stderr,format,listpointer);
		va_end(listpointer);

		return true;
	}
	else
		return false;
}
// }}}

vector <string>	state;
vector <string>	rot;
int	N,K;

string trimdot(string s) {
	int	i;

	Fi(sz(s)) {
		if(s[i] != '.') break;
	}

	if(i != 0) s = s.substr(0,i);

	for(i = sz(s) - 1;i >= 0; i--) {
		if(s[i] != '.') break;
	}

	return s.substr(i+1);
}

void rotate() {
	int	i,j;
	Fi(sz(state[0])) rot.push_back("");
	int	p;

	for(i = N - 1; i >= 0; i--) {
		p = sz(rot) - 1;

		for(j = sz(state[i]) - 1; j >= 0; j--) {
			if(state[i][j] != '.') {
				rot[p] += state[i][j];
				p--;
			}
		}

	 	for(j = 0; j <= p; j++) rot[j] += ".";
	}
}

bool horz(int r,int c) {
	int	i;
	int	k = 0;

	for(i = c; i < sz(rot[r]); i++) {
		if(rot[r][i] != rot[r][c])
			break;
		k++;
	}

	return k == K;
}

bool vert(int r,int c) {
	int	i;
	int	k = 0;

	for(i = r; i < sz(rot); i++) {
		if(rot[i][c] != rot[r][c])
			break;
		k++;
	}

	return k == K;
}

bool diag(int r,int c,int dr,int dc) {
	char	ch = rot[r][c];
	int	k = 0;

	while(r >= 0 && r < sz(rot) && c >= 0 && c < sz(rot[r])) {
		if(rot[r][c] != ch)
			break;

		k++;
		r += dr,c += dc;
	}

	return k == K;
}

int main()
{
	int	T;
	int	cs;
	int	i,j;
	string	s;
	
	cin >> T;

	rab(cs,1,T) {
		cin >> N >> K;

		state.clear();
		rot.clear();

		Fi(N) {
			cin >> s;

			state.push_back(s);
		}

		rotate();

		//Fi(sz(rot)) cout << rot[i] << endl;

		bool	rw,bw;

		rw = bw = false;

		Fi(sz(rot)) Fj(sz(rot[i])) {
			if(rot[i][j] == '.') continue;
			if(horz(i,j) || vert(i,j) || diag(i,j,1,1) || diag(i,j,1,-1)) {
				if(rot[i][j] == 'R') rw = true;
				if(rot[i][j] == 'B') bw = true;

				//printf("%d %d: %s %s\n",i,j,rw ? "T" : "F", bw ? "T" : "F");
			}
		}

		char	*res;

		if(!rw && !bw) res = "Neither";
		else if(rw && bw) res = "Both";
		else if(rw) res = "Red";
		else
			res = "Blue";

		printf("Case #%d: %s\n",cs,res);
	}
	return 0;
}
