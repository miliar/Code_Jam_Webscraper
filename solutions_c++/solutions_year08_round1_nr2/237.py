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

const char *IMP = " IMPOSSIBLE";

struct Shake{
	int n,m;
	vector<vector<pair<int,bool> > > pref;
	vector<bool> res;
	void Go(){
/*
  cout << n << endl;
  foa(k,pref){
  foa(j,pref[k]) cout << " (" << pref[k][j].first << ' ' << pref[k][j].second << ")";
  cout << endl;
  }
*/
		res.assign(n,false);

		int minv = 0;
		int minc = 1000000;
		fo(k,1<<(n)){
//			cout << "k = " << k << endl;
			int c = 0;
			for(int j = k;j;j>>=1) if(j%2) c++;
//			cout << "c = " << c << endl;

			bool ok = true;
			foa(j,pref){
				bool got = false;
				foa(i,pref[j]){
					int type = pref[j][i].first-1;
					if( (bool)((1<<type) & k) == pref[j][i].second){got=true; break;}
				}
				if(!got) {ok=false; break;}
			}

			if(ok && minc > c){
				minv = k;
				minc = c;
			}
		}

		if(minc == 1000000) cout << IMP;
		else
			fo(k,n) cout << ' ' << (int)(bool)((1<<k)&minv);
	}
};

int main()
{
	string line;
	!getline(cin,line);
	int ca=0;
	while(++ca,getline(cin,line)){
		Shake s;

		{istringstream iss(line); iss >> s.n;}
		if(!getline(cin,line)) throw int();
		{istringstream iss(line); iss >> s.m;}

		fo(k,s.m){
			s.pref.pb(vector<pair<int,bool> >());
			if(!getline(cin,line)) throw int();
			istringstream iss(line);
			int t;
			iss >> t;
			fo(j,t){
				int l;
				bool b;
				if(!(iss >> l >> b)) throw int();
				s.pref.back().pb(mp(l,b));
			}
		}

		cout << "Case #" << ca << ":";
		s.Go();
		cout << endl;
	}
}
