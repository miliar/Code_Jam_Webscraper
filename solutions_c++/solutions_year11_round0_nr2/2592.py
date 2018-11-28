#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////

int main()
{
	int T;
	cin>>T;
	REP(index, T)
	{
		int C,D,N;
		map<string,char> comb;
		map<pair<char,char>,int> oppo;
		cin>>C;
		string tmp;
		REP(i,C)
		{
			cin>>tmp;
			string s=string(1,tmp[0])+string(1,tmp[1]);
			string t=string(1,tmp[1])+string(1,tmp[0]);
			comb[s]=tmp[2];
			comb[t]=tmp[2];
		}
		cin>>D;
		REP(i,D)
		{
			cin>>tmp;
			oppo[MP(tmp[0], tmp[1])]++;
			oppo[MP(tmp[1], tmp[0])]++;;
		}
		cin>>N;
		string seq;
		cin>>seq;
		/////

		string ret="";
		REP(i,seq.sz)
		{
			if((int)ret.sz==0) {ret+=seq[i]; continue;}
			char tc=ret[ret.size()-1];
			string p=string(1,tc)+string(1,seq[i]);
			string q=string(1,seq[i])+string(1,tc);
			if(comb.count(p) or comb.count(q)) { ret[ret.size()-1]=comb[p]; continue;}
			bool eraseAll=false;
			for(int j=0; j<ret.size(); j++) if(oppo.count(MP(ret[j], seq[i]))) {ret=""; eraseAll=true; break;}
			if(eraseAll) continue;

			ret+=seq[i];
		}
		cout<<"Case #"<<index+1<<": [";
		for(int i=0; i<ret.size(); i++)
		{
			if(i!=0) cout<<", ";
			cout<<ret[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}
