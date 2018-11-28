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

    freopen("B-large.in","r",stdin);
    freopen("blarge.out","w",stdout);

	int cases; scanf("%d",&cases);
	REP(k,cases) {
		int n; scanf("%d",&n);
		int s; scanf("%d",&s);
		int p; scanf("%d",&p);
		vector<int> totals;
		int tmp;
		REP(i,n) { scanf("%d",&tmp); totals.push_back(tmp); }

		vector< vector<int> > d;
		REP(i, totals.size()) {
			int tot = totals[i];
			vector<int> a;
			for(int j = 0; j < 3; j++) a.push_back(tot/3);
			if(tot%3==1) a[2]++;
			if(tot%3==2) a[1]++,a[2]++;
			d.push_back(a);
		}

		int count = 0;
		REP(i,d.size()) {
			vector<int> x = d[i];
			if(x[2] >= p || x[1] >= p || x[0] >= p) count++;
			else {
				int need = p - x[2];
				if(need == 1) {
					x[2]++;
					x[1]--;
					if(x[1] < 0) continue;
					sort(ALL(x));
					int a = x[1] - x[0], b = x[2] - x[1], c = x[2] - x[0];
					if(a>2 || b > 2 || c > 2) continue;
					if(a == 2 || b == 2 || c == 2) {
						if(s > 0) {
							count++;
							s--;
						}
					}
					else {
						count++;
					}
				}
			}
		}
		printf("Case #%d: %d\n", k+1, count);


	}
     return 0;
}
