/*

Name: Takvir Hossain Tusher
E-Mail : tusher205@gmail.com

*/

#include <cstring>
#include <string>
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

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

#define SMALL
//#define LARGE

int N;
map<char,char> refMap;

void setRefMap(){
    refMap[' '] = ' ';

    refMap['a'] = 'y';
    refMap['b'] = 'h';
    refMap['c'] = 'e';
    refMap['d'] = 's';
    refMap['e'] = 'o';
    refMap['f'] = 'c';
    refMap['g'] = 'v';
    refMap['h'] = 'x';
    refMap['i'] = 'd';
    refMap['j'] = 'u';
    refMap['k'] = 'i';
    refMap['l'] = 'g';
    refMap['m'] = 'l';
    refMap['n'] = 'b';
    refMap['o'] = 'k';
    refMap['p'] = 'r';
    refMap['q'] = 'z';
    refMap['r'] = 't';
    refMap['s'] = 'n';
    refMap['t'] = 'w';
    refMap['u'] = 'j';
    refMap['v'] = 'p';
    refMap['w'] = 'f';
    refMap['x'] = 'm';
    refMap['y'] = 'a';
    refMap['z'] = 'q';
}

int main() {
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large-practice.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

    setRefMap();

	cin >> N;

	string s1;
	getline(cin, s1);

	rep2(nn,0,N) {
		getline(cin, s1, '\n');

		printf("Case #%d: ", nn+1);
		rep(i, s1.size()){
            char c = s1.at(i);
            cout<<refMap.find(c)->second;
		}
		cout<<endl;
	}
	return 0;
}
