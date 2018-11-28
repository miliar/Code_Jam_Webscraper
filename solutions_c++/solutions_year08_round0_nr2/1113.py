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

struct trip{
	int d,a;
	char s;
	bool f;
	trip(int _d,int _a,char _s){d=_d;	a=_a;	s=_s;	f=false;}
	
};

bool cmp(struct trip* r,struct trip* t){	return r->d==t->d? r->a<t->a:r->d<t->d;}
typedef vector <struct trip*> VT;

string solve(VT& t){
	int a,b,ta,tb;
	a=b=ta=tb=0;
	sort(ALL(t),cmp);

	REP(i,t.size()){
		REP(j,i){
			if(!t[j]->f && t[j]->a<=t[i]->d){
				if(t[j]->s=='A')	tb++;
				else ta++;
				t[j]->f=true;

			}
		}

		if(t[i]->s=='A'){
			if(ta==0)a++;
			else ta--;
		}else if(t[i]->s=='B'){
			if(tb==0)b++;
			else tb--;
		}
	
	
	}
	char bf[128];
	sprintf(bf,"%d %d",a,b);
	return string("")+bf;
}

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");
 
  long st = clock();
 string s;
  int n;	in >> n;
  REP(i,n){
	  VT vt;
	  int to,na,nb;
	 in>>to>>na>>nb;
	 
	 REP(j,na){
		 int d,a;
		 in>>s; int k=s.find(":");
		 d=60*atoi(s.substr(0,k).c_str());
		 d+=atoi(s.substr(k+1).c_str());

		 in>>s; k=s.find(":");
		 a=60*atoi(s.substr(0,k).c_str());
		 a+=atoi(s.substr(k+1).c_str());
		 a+=to;
		 vt.PB(new struct trip(d,a,'A'));
	 }

	 REP(j,nb){
		 int d,a;
		 in>>s; int k=s.find(":");
		 d=60*atoi(s.substr(0,k).c_str());
		 d+=atoi(s.substr(k+1).c_str());

		 in>>s;  k=s.find(":");
		 a=60*atoi(s.substr(0,k).c_str());
		 a+=atoi(s.substr(k+1).c_str());
		 a+=to;
		 vt.PB(new struct trip(d,a,'B'));
	 }

	out<<"Case #"<<i+1<<": "<<solve(vt)<<endl;
  }

	
	cout<<"t: "<<(clock()-st);
	out.close();
	return 0;
}

