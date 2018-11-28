#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
#include <memory.h> 
#include <iomanip>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT((c)), (c).erase(unique(ALL((c))), (c).end())
#define INF 1000000000
#define MAX(a,b) (((a) > (b)) ? (a) : (b))	
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define SQR(a) ((a)*(a))
#define X first
#define Y second

typedef pair<int,int> ii;
typedef vector<int > vi;
typedef vector<vi > vvi;
typedef vector<ii  > vii;
typedef vector<vii  > vvii;
typedef long long ll;
typedef unsigned long long ull;

string filename = "A-large";

int main(){	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int T;
	cin>>T;
	REP(test, T){
		set<string> have;
		string s;
		int res = 0;
		int n, m;
		cin>>n>>m;
		REP(i, n){
			cin>>s;
			have.insert(s);
		}
		REP(i, m){
			cin>>s;
			while(1){
				if (s.empty() || have.find(s) != have.end())
					break;
				++res;
				have.insert(s);
				int index = s.find_last_of('/');
				s = s.substr(0, index);
			}
		}

		cout<<"Case #"<<test+1<<": "<<res<<endl;
	}


	return 0;
}