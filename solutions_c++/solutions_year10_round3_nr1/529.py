#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000

struct node{
	int a;
	int b;
	int order;
};
bool sort1 (struct node i,struct node j) { return (i.a<j.a); }
bool sort2 (struct node i, struct node j){return (i.b<j.b);}

int main(int argc, char **argv) {
	int caseNum = -1, caseN = 1;
//	freopen("test.txt", "r", stdin);
	freopen("A.out", "w", stdout);

		freopen("A-small-attempt0.in","r",stdin);
	//	freopen("A-small-attempt1.in","r",stdin);
	//	freopen("A-large.in","r",stdin);
	//	FILE *fp = fopen("test.txt", "r");
	//	FILE *fp = fopen("A-small-attempt0.in", "r");
	//	FILE *fp = fopen("A-small-attempt1.in", "r");
	//	FILE *fp = fopen("A-large.in", "r");
	//	FILE *fpw = fopen("A.out", "w");
	cin >> caseNum;

	while (caseNum--) {
		int lines;

		cin >> lines;
		struct node nlines[lines];
//		struct node nlines2[lines];
		int a,b;
		REP(i,lines) {cin>>a>>b; nlines[i].a=a;nlines[i].b=b;}

		sort(nlines, nlines+lines, sort1);
		REP(i,lines){
			nlines[i].order=i;
		}
		sort(nlines, nlines+lines, sort2);


		int res=0;
		REP(i,lines){
			if(nlines[i].order<i) res+=lines-1-nlines[i].order;
		}

//		cout<<res;
		// fprintf(fpw, "Case #%d: %d\n", caseN,);
		//pay attention to endl!!!
		cout<<"Case #"<<caseN<<": "<< res <<endl;

		caseN++;
	}
}

