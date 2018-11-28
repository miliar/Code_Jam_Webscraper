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
			oppo[MP(tmp[1], tmp[0])]++;
		}
		cin>>N;
		string seq;
		cin>>seq;
		/////

		string ret="";
		map<char,int> exist;
		REP(i,seq.sz)
		{
			if((int)ret.sz==0) {ret+=seq[i]; exist[seq[i]]++; continue;}
			char tc=ret[ret.size()-1];
			string p=string(1,tc)+string(1,seq[i]);
			if(comb.count(p)) {ret[ret.size()-1]=comb[p]; exist[tc]--; continue;}
			bool eraseAll=false;
			for(map<char,int>::iterator it=exist.begin(); it!=exist.end(); it++) if(it->second > 0)
		 	{ 
				if(oppo.count(MP(seq[i], it->first)))
				{
					ret=""; exist.clear(); eraseAll=true; break;
				}
			}
			if(eraseAll) continue;

			ret+=seq[i];
			exist[seq[i]]++;
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
