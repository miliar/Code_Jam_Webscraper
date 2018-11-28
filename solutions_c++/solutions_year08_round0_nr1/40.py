#include<cassert>
#include<algorithm>
#include<cstring>
#include<cctype>
#include<cmath>
#include<functional>
#include<cerrno>
#include<iomanip>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>
//#include<gmpxx.h>
using namespace std;
#define sz(x) ((int)(x.size()))
#define mp make_pair
#define pb push_back
#define fr(k,y,z) for(int k=(y);k<=(z);k++)
#define fo(k,z) for(int k = 0;k<(z);k++)
#define foa(k,x) fo(k,sz(x))
#define all(x) (x).begin(),(x).end()
#define iall(I,x) for(typeof((x).begin()) I = (x).begin(); I != (x).end();++I)

struct Search{
	int S,Q;
	vector<string> s,q;
	void Go();
	vector<int> cant;
	vector<vector<int> > memo;

	int dps(int cq,int cs){
		if(cq < 0) return 0;
		if(memo[cq][cs] != -1) return memo[cq][cs];

		int mv = 100099;
		if(cant[cq] != cs){
			foa(k,s)
				mv = min(mv, dps(cq-1,k) + (k == cs ? 0 : 1));
		}
		return memo[cq][cs] = mv;
	}
};

void Search::Go(){
//	foa(k,s) cout << "s " << s[k] << endl;
//	foa(k,q) cout << "q " << q[k] << endl;

	map<string,int> m;
	foa(k,s) m[s[k]] = k;
	foa(k,q) assert(m.find(q[k]) != m.end());
	foa(k,q) cant.pb(m[q[k]]);

	int mv = 100099;
//	memo.assign(sz(q)+3,vector<int>(sz(s)+3,-1));
	memo.assign(1000 + 3,vector<int>(100+3,-1));
	foa(k,s) mv = min(mv,dps(sz(q)-1,k));
	cout << mv;
}

int main()
{
	string line;
	getline(cin,line);
	int ca=0;
	while(++ca,getline(cin,line)){
		Search s;
		istringstream iss(line);
		iss >> s.S;
		fo(k,s.S){
			if(!getline(cin,line)) throw int();
			s.s.pb(line);
		}

		if(!getline(cin,line)) throw int();
		istringstream iss2(line);
		iss2 >> s.Q;

		fo(k,s.Q){
			if(!getline(cin,line)) throw int();
			s.q.pb(line);
		}

		cout << "Case #" << ca << ": ";
		s.Go();
		cout << endl;
	}
}
