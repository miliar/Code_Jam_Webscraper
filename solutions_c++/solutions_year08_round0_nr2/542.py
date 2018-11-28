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
#define FOREACH(type,it, X) for(type it = (X).begin(); it != (X).end(); ++it)
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
struct mtime {
    int h;int m;
    mtime(){
        scanf("%d:%d",&h,&m);
    }
    void addm(int mini) {
        m += mini;
        if (m >= 60)
        {
            h++;
            m -= 60;
        }
    }
    bool operator<(const mtime& c) const {
        if (h<c.h) return true;
        else if (h == c.h)
          return m < c.m;
        else return false;
    }
    bool operator<=(const mtime& c) const {
        if (h<c.h) return true;
        else if (h == c.h)
          return m <= c.m;
        else return false;
    }
	~mtime(){}
};
typedef vector<mtime> VM;

int main(int argc, char* argv[]){
  init(argc, argv);
  int te;
  scanf("%d", &te);
  FOR(nr, 1, te){
    int turn = 0;
    int needa=0,needb=0;
    VM AS,AE,BS,BE;
    scanf("%d",&turn);
    int na=0,nb=0;
    scanf("%d %d",&na, &nb);
    REP(i,na) {
        mtime st;mtime et;
        AS.push_back(st);
        BE.push_back(et);
    }
    sort(AS.begin(),AS.end());
    sort(BE.begin(),BE.end());
    FOREACH(VM::iterator,ia,BE) {
        ia->addm(turn);
    }
    REP(j,nb) {
        mtime st;mtime et;
        BS.push_back(st);
        AE.push_back(et);
    }
    sort(BS.begin(),BS.end());
    sort(AE.begin(),AE.end());
    FOREACH(VM::iterator,ib,AE) {
        ib->addm(turn);
    }
    FOREACH(VM::iterator,ita,AS) {
        VM::iterator tmp = AE.begin();
        if (tmp != AE.end() && *tmp <= *ita)
        {
            AE.erase(tmp);
        }
        else
           needa ++;
    }
    FOREACH(VM::iterator,itb,BS) {
        VM::iterator tmp = BE.begin();
        if (tmp != BE.end() && *tmp <= *itb)
        {
            BE.erase(tmp);
        }
        else
           needb ++;
    }
    printf("Case #%d: %d %d\n",nr,needa,needb);
  }
	return 0;
}
