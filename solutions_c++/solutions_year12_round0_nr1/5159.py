#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <fstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

#define LEN(a) (int)(sizeof(a) / sizeof(a[0]))

typedef double dbl;
typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

template <class T> T inline sqr(T x) { return x * x; }
template <class T> inline void relaxMin( T &a, T b ) { a = min(a, b); }
template <class T> inline void relaxMax( T &a, T b ) { a = max(a, b); }

string str( int i ) { char s[100]; sprintf(s, "%d", i); return string(s); }

inline int sign( int x ) { return x > 0 ? 1 : (x < 0 ? -1 : 0); }
inline int myAbs( int a ) { return a > 0 ? a : -a; }

int main()
{
	int T;
	map<char,char> aa;
	aa[' ']=' ';
	aa['z']='q';
	aa['q']='z';
	aa['a']='y';
	aa['b']='h';
	aa['c']='e';
	aa['d']='s';
	aa['e']='o';
	aa['f']='c';
	aa['g']='v';
	aa['h']='x';
	aa['i']='d';
	aa['j']='u';
	aa['k']='i';
	aa['l']='g';
	aa['m']='l';
	aa['n']='b';
	aa['o']='k';
	aa['p']='r';
	aa['r']='t';
	aa['s']='n';
	aa['t']='w';
	aa['u']='j';
	aa['v']='p';
	aa['w']='f';
	aa['x']='m';
	aa['y']='a';
//	forit(it,aa){
//		printf("a['%c']='%c'\n",it->first,it->second);
//	}
///	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
//	string s2 = "our language is impossible to understand";
//	string s3 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
//	string s4 = "there are twenty six factorial possibilities";
//	string s5 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
//	string s6 = "so it is okay if you want to just give up";
///	for (int i=0; i<s1.size(); ++i)
//		aa[s1[i]]=s2[i];
//	for (int i=0; i<s3.size(); ++i)
//		a[s3[i]]=s4[i];
//	for (int i=0; i<s5.size(); ++i)
//		a[s5[i]]=s6[i];
//	forit(it,a){
//		printf("a['%c']='%c'\n",it->first,it->second);
//	}
	cin>>T;
	string str;
	getchar();
	forab(tt,1,T){
		getline(cin,str);
		forn(i,str.size()){
			str[i]=aa[str[i]];
		}
		printf("Case #%d: %s\n",tt,str.c_str());
	}
}
