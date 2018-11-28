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

bool areRec(int a, int b) {
	string s = i2a(a), r = i2a(b);
	if(s.size() != r.size()) return false;
	REP(i,s.size()) {
		if(s == r) return true;
		char c = s[0];
		s.PB(c);
		s.erase(s.begin());
	}
	return false;
}


int main()
{

    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);

	int cases;
	scanf("%d",&cases);
	REP(k,cases) {
		int a, b;
		//fprintf(stderr, "case = %d\n", k);
		scanf("%d %d",&a, &b);
		int count = 0;
		for(int n = a; n <= b; n++) {
			for(int m = n; m <= b; m++) {
				if( m == n ) continue;
				if(areRec(m,n)) count++;
			}
		}
		printf("Case #%d: %d\n", k+1, count);
	}
     return 0;
}
