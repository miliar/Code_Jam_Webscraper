#pragma warning(disable: 4786)
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef __int64 LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define LEN 256
#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,p,k) for (int var=(p); var<=(k); ++var)
#define FORD(var,p,k) for (int var=(p); var>=(k); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

static string infile, outfile;
static void init(int argc, char* argv[]){
    if (argc > 1) 
    {infile = argv[1]; freopen(infile.c_str(),"r",stdin);}
    if (argc > 2)
    {outfile=argv[2];  freopen(outfile.c_str(),"w",stdout);}

}


int main(int argc, char* argv[]){
  init(argc, argv);
  int te;
  scanf("%d", &te);
  FOR(nr, 1, te){
    int S=0,Q=0;
    int count=0;
    VS mys;
    scanf("%d\n",&S);
    REP(i,S) {
        char name[128];
        scanf("%[^\n]\n",name);
        mys.push_back(name);
    }
    scanf("%d\n",&Q);
    set<string> tot;
    REP(j,Q) {
        char name[128];
        scanf("%[^\n]\n",name);
        string n(name);
        tot.insert(n);
        if(tot.size() >= S) {
            count++;
            tot.clear();
            tot.insert(n);
        }
    }
    printf("Case #%d: %d\n",nr,count);
  }
	return 0;
}
