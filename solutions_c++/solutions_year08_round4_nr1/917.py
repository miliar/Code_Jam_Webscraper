#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <cmath>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PI;
#define MP make_pair
#define REP(x,n) for(int x=0; x<(int)(n); ++x)
#define REB(b,x,n) for(int x=b; x<(int)(n); ++x)
#define REPD(x,n) for(int x=(n)-1; x>=0; --x)
#define PB push_back
#define ST first
#define ND second
const int INF = 1000000001;
const double EPS = 10e-9;

bool gat[10001];
bool chg[10001];
bool val[10001];
int M,V;
int mi, ml;

map<pair<int,bool>,int> pam;

int whatmin(int where, bool v) {
	//if matches, nothing to change
	if(v==val[where]) return 0;
	//leaf nodes can't change
	if(where>=mi) return INF;

	if(pam.find(MP(where,v))!=pam.end()) return pam.find(MP(where,v))->ND;

	int result = INF;

	//change left AND to 1
	if(v && gat[where] && val[2*where+2])
		result = min(result, whatmin(2*where+1,1));
	//change right AND to 1
	else if(v && gat[where] && val[2*where+1])
		result = min(result, whatmin(2*where+2,1));
	//change both and to 1
	else if(v && gat[where])
		result = min(result, whatmin(2*where+1,1)+whatmin(2*where+2,1));
	//change any OR to 1
	else if(v && (!gat[where])) {
		result = min(result, whatmin(2*where+1,1));
		result = min(result, whatmin(2*where+2,1));
	}
	//change any AND to 0
	else if((!v) && gat[where]) {
		result = min(result, whatmin(2*where+1,0));
		result = min(result, whatmin(2*where+2,0));
	}
	//change left OR to 0
	else if((!v) && (!gat[where]) && (!val[2*where+2]))
		result = min(result, whatmin(2*where+1,0));
	//change right OR to 0
	else if((!v) && (!gat[where]) && (!val[2*where+1]))
		result = min(result, whatmin(2*where+2,0));
	//change both OR to 0
	else if((!v) && (!gat[where]))
		result = min(result, whatmin(2*where+2,0)+whatmin(2*where+1,0));

	if(chg[where]) {
	result--;
	gat[where]=!gat[where];
	if(gat[where] && ((val[2*where+1] && val[2*where+2])) == v) result = 0;
	else if((!gat[where]) && ((val[2*where+1] || val[2*where+2])) == v) result = 0;
	//change left AND to 1
	if(v && gat[where] && val[2*where+2])
		result = min(result, whatmin(2*where+1,1));
	//change right AND to 1
	else if(v && gat[where] && val[2*where+1])
		result = min(result, whatmin(2*where+2,1));
	//change both and to 1
	else if(v && gat[where])
		result = min(result, whatmin(2*where+1,1)+whatmin(2*where+2,1));
	//change any OR to 1
	else if(v && (!gat[where])) {
		result = min(result, whatmin(2*where+1,1));
		result = min(result, whatmin(2*where+2,1));
	}
	//change any AND to 0
	else if((!v) && gat[where]) {
		result = min(result, whatmin(2*where+1,0));
		result = min(result, whatmin(2*where+2,0));
	}
	//change left OR to 0
	else if((!v) && (!gat[where]) && (!val[2*where+2]))
		result = min(result, whatmin(2*where+1,0));
	//change right OR to 0
	else if((!v) && (!gat[where]) && (!val[2*where+1]))
		result = min(result, whatmin(2*where+2,0));
	//change both OR to 0
	else if((!v) && (!gat[where]))
		result = min(result, whatmin(2*where+2,0)+whatmin(2*where+1,0));
	gat[where]=!gat[where];
	result++;
	}

	pam[MP(where,v)] = result;
	return result;
}


void doit() {
	pam.clear();
	cin>>M>>V;
	mi = (M-1)/2;
	ml = (M+1)/2;
	REP(i,mi) {
		cin>>gat[i]>>chg[i];
	}
	REP(i,ml) {
		cin>>val[mi+i];
	}
	REPD(i,mi) {
		if(gat[i])
			val[i] = val[2*i+1] && val[2*i+2];
		else
			val[i] = val[2*i+1] || val[2*i+2];
	}

	int result = whatmin(0,V);
	if(result>=INF) cout<<"IMPOSSIBLE";
	else cout<<result;
	cout<<endl;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int NCase;
	cin>>NCase;
	REP(ncase,NCase) {
		cout<<"Case #"<<ncase+1<<": ";
		doit();
	}

  return 0;
}
