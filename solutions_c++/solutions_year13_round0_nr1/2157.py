#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <malloc.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <stdint.h>
#include <unistd.h>
#include <ctime>
#include <climits>
using namespace std;
#define EPS 		1e-8
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define F(i,a)      FOR(i,0,a)
#define PB          push_back
#define S           size()
#define MP          make_pair
#define ALL(v)      v.begin(),v.end()
#define LLA(v)      v.rbegin(),v.rend()
#define fi          first
#define se          second
#define NL 			printf("\n")
#define SP 			system("pause")
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)
const double PI = acos(-1.0);
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<string> vstr;
typedef long long   LL;
#define DEBUG
int cnt = 0;

void run() {
	vi xh(4, 0);// X horizontales
	vi xv(4, 0);// X verticales
	vi oh(4, 0);// O horizontales
	vi ov(4, 0);// O verticales
	int xdp = 0;//X diagonal principal
	int xds = 0;//X diagonal secundaria
	int odp = 0;//O diagonal principal
	int ods = 0;//O diagonal secundaria
	char s[10];
	int total = 0;
	bool X = false, O = false;
	F(i, 4) {
		gets(s);
		F(j, 4) {
			if(s[j] == 'X') {
				xh[i]++;
				xv[j]++;
				total++;
				if(i == j)			xdp++;
				else if(i + j == 3)	xds++;
				X |= (xh[i] == 4 | xv[j] == 4 | xdp == 4 | xds == 4);
			} else if(s[j] == 'O') {
				oh[i]++;
				ov[j]++;
				total++;
				if(i == j)			odp++;
				else if(i + j == 3)	ods++;
				O |= (oh[i] == 4 | ov[j] == 4 | odp == 4 | ods == 4);
			} else if(s[j] == 'T') {
				xh[i]++;
				xv[j]++;
				oh[i]++;
				ov[j]++;
				total++;
				if(i == j) {
					xdp++;
					odp++;
				}
				else if(i + j == 3)	{
					xds++;
					ods++;
				}
				X |= (xh[i] == 4 | xv[j] == 4 | xdp == 4 | xds == 4);
				O |= (oh[i] == 4 | ov[j] == 4 | odp == 4 | ods == 4);
			}
		}
	}
	printf("Case #%d: ", ++cnt);
	if(X) {
		printf("X won");
	} else if(O) {
		printf("O won");
	} else if(total == 16) {
		printf("Draw");
	} else {
		printf("Game has not completed");
	}
	NL;
	getchar();
}

int main(){
	#ifdef DEBUG
		freopen("a_large_input.in","r",stdin);
		freopen("a_large_output.in","w",stdout);
		time_t st=clock();
	#endif
	int t = in();
	while(t--)
		run();
	#ifdef DEBUG
		//printf("=============\n");
		//printf("Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
	#endif
	return 0;
}




























//Author: Gabriel Menacho                      Nickname: tzyirvo.
