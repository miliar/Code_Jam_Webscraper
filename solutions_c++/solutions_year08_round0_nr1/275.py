#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
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

int main()
{
	ios_base::sync_with_stdio(0);
	int N;
	cin>>N;
	REP(ncase,N) {
		int S,Q;

		cin>>S;
		cin.ignore(100, '\n');
		//we actually only need the number S of different engines here
		//set<string> all_engines;
		REP(si,S) {
			char cstr_engine[256];
			cin.getline(cstr_engine,250);
			//all_engines.insert(cstr_engine);
			//cout<<"added "<<cstr_engine<<endl;
		}

		//greedy! (always use the longest possible engine)
		cin>>Q;
		cin.ignore(100, '\n');
		int result = 0;
		set<string> met_engines;
		REP(qi,Q) {
			char cstr_engine[256];
			cin.getline(cstr_engine,250);
			met_engines.insert(cstr_engine);
			if(met_engines.size() == S /*all_engines.size()*/) {
				result++;
				met_engines.clear();
				met_engines.insert(cstr_engine);
			}
		}

		cout<<"Case #"<<ncase+1<<": "<<result<<"\n";
	}
	cout<<flush;

  return 0;
}
