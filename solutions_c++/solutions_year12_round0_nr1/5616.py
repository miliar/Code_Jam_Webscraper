#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <bitset>

using namespace std;

#define LL long long
#define pb push_back
#define r(_x,_a,_b,_c) for(_x _a = _b; _a <= _c; _a++)
#define rm(_x,_a,_b,_c,_m) for(_x _a = _b; _a <= _c; _a+=_m)
#define revr(_x,_a,_b,_c) for(_x _a = _b; _a >= _c; _a--)
#define revrm(_x,_a,_b,_c,_m) for(_x _a = _b; _a >= _c; _a-=_m)
#define eps 1e-3
#define mp make_pair
#define fi first
#define se second
#define INF 100000000

int t;
string s;
map<char,char> ch;

int main() {
		ch['a'] = 'y';
		ch['b'] = 'h';
		ch['c'] = 'e';
		ch['d'] = 's';
		ch['e'] = 'o';
		ch['f'] = 'c';
		ch['g'] = 'v';
		ch['h'] = 'x';
		ch['i'] = 'd';
		ch['j'] = 'u';
		ch['k'] = 'i';
		ch['l'] = 'g';
		ch['m'] = 'l';
		ch['n'] = 'b';
		ch['o'] = 'k';
		ch['p'] = 'r';
		ch['q'] = 'z';
		ch['r'] = 't';
		ch['s'] = 'n';
		ch['t'] = 'w';
		ch['u'] = 'j';
		ch['v'] = 'p';
		ch['w'] = 'f';
		ch['x'] = 'm';
		ch['y'] = 'a';
		ch['z'] = 'q';
		scanf("%d",&t);
		r(int,i,0,t) {
				getline(cin,s);
				if(i != 0) {
						string hasil;
						r(unsigned int,j,0,s.size()-1) {
							if(s[j] != ' ')
									hasil += ch[s[j]];
							else
									hasil += ' ';
						}
						cout << "Case #" << i << ": " << hasil << endl;
				}
		}
}
