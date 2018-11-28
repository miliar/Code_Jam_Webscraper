#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int i=(a);(int)i<(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}



int main()
{

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

	string s;
	vector<string> source, convert;
/*
	for(int i = 0; i < 3; i++) {
		getline(cin,s);
		source.PB(s);
	}

	for(int i = 0; i < 3; i++) {
		getline(cin,s);
		convert.PB(s);
	}
*/
	map<char, char> m;
	//m['z']='q';

	m[' ']=' ';
	m['y']='a';
	m['n']='b';
	m['f']='c';
	m['i']='d';
	m['c']='e';
	m['w']='f';
	m['l']='g';
	m['b']='h';
	m['k']='i';
	m['u']='j';
	m['o']='k';
	m['m']='l';
	m['x']='m';
	m['s']='n';
	m['e']='o';
	m['v']='p';
	m['z']='q';
	m['p']='r';
	m['d']='s';
	m['r']='t';
	m['j']='u';
	m['g']='v';
	m['t']='w';
	m['h']='x';
	m['a']='y';
	m['q']='z';
	getline(cin,s);
	int n; sscanf(s.c_str(),"%d",&n);
	REP(k,n) {
		getline(cin,s);
		string r;
		REP(i,s.size()) r.PB(m[s[i]]);
		cout<<"Case #"<<k+1<<": "<<r<<endl;
	}

/*
	REP(i,source.size()) {
		REP(j,source[i].size()) {
			m[convert[i][j]] = source[i][j];
		}
	}

	for(map<char, char>::iterator it = m.begin(); it != m.end(); it++) {
		cout<<"m['"<<it->second<<"']='"<<it->first<<"';"<<endl;
	}
*/
     return 0;
}
