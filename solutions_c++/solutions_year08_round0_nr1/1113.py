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
#include <fstream>
#include <time.h>

using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;


#define ALL(x) x.begin(),x.end()
#define FILL(a,c) memset(&a, c, sizeof(a))
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,bas,son) for (int var=(bas); var<=(son); ++var)
#define FORD(var,bas,son) for (int var=(bas); var>=(son); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ME(a,b) max_element((a), (b))
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define INF INT_MAX
#define P2(a) (a)*(a)
#define MS(a,b,c) memset(a,(b),sizeof(c))

#define MAXS 200

bool check[MAXS];

int get(VS& pr,const string& s) {
  for (int i = 0; i < pr.size(); i++) if (pr[i] == s) return i;
  return -1;
}
int solve(VS& s,VS& q){
	int rst=0;
	int cnt=0;
	MS(check,false,check);
	int j=0;
	REP(i,q.size()){
		j=get(s,q[i]);
		if(!check[j]){	cnt++;	check[j]=true;}
		if(cnt==s.size()){	rst++;	cnt=1;	MS(check,false,check);	check[j]=true;}	
	}
	
	return rst;
}

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");
 
  long st = clock();
 string s;
  int n,ns,nq;	in >> n;
  REP(i,n){
	  VS vs;VS vq;
	 in>>ns;
	 getline(in,s);
	 REP(j,ns){getline(in,s);	vs.PB(s);}
	 in>>nq;
	 getline(in,s);
	 REP(j,nq){getline(in,s);	vq.PB(s);}

	out<<"Case #"<<i+1<<": "<<solve(vs,vq)<<endl;
  }

	
	cout<<"t: "<<(clock()-st);
	out.close();
	return 0;
}

