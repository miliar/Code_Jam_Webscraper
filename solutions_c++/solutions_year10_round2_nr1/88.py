#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

#define VI vector<int> 
#define VS vector<string> 
#define LL long long 
#define FOR(i,n,m) for(int i=n;i<=m;i++)
#define REP(i,n) for(int i = 0; i < n; i++)
#define REPD(i,n) for(int i = n - 1; i>=0; i--)
#define BE(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair
#define SI(a) sizeof(a)
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR_SET(it, type, ss) for (set<type>::iterator it = ss.begin(); it!= ss.end(); it++)

const int INFI = 2000000000;
const int goX[4] = {-1, 0, 1, 0};
const int goY[4] = {0, 1, 0, -1};

const string PROBLEM_NAME = "A-large";
const string INPUT_FILE = PROBLEM_NAME + ".in";
const string OUTPUT_FILE = PROBLEM_NAME + ".out";

ofstream fout (OUTPUT_FILE.c_str());
ifstream fin (INPUT_FILE.c_str());

class Directory{
public:
	string parent, name;

	Directory(){}
	Directory(string parent, string name) : parent(parent), name(name){}

	bool operator<(const Directory& other) const{
		if (parent != other.parent) return parent < other.parent;
		return name < other.name;
	}

};
vector<string> tokenize(string s, string del=" ") {
        vector<string> ret(0); 
        for (int i=0,j;i<s.size();i=j+1) {
			if ((j=s.find_first_of(del,i))==s.npos) j = s.size();
                if (j-i>0) ret.PB(s.substr(i,j-i));
        }
        return ret;
}

const int MAXN = 200;
int n, m, T ;
set <Directory> myDir;
string dir1[MAXN], dir2[MAXN];

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}

void solve(int testNo){
	myDir.clear();

	REP(i, n){
		VS vs = tokenize(dir1[i], "/");
		string s = "/";
		REP(j, vs.size()){
			myDir.insert(Directory(s, vs[j]));
			s = s + "/" + vs[j];
		}
	}

	int res = 0;
	REP(i, m){
		VS vs = tokenize(dir2[i], "/");
		string s = "/";
		REP(j, vs.size()){
			Directory cur (s, vs[j]);
			if (myDir.find(cur) == myDir.end()){
				res++;
				myDir.insert(cur);
			}
			s = s + "/" + vs[j];
		}
	}

	cout << "Case #" << testNo << ": " << res << endl;
}

void m_main(){
	cin >> T;
	REP(step, T){
		cin >> n >> m;
		REP(i, n) cin >> dir1[i];
		REP(i, m) cin >> dir2[i];
		solve(step + 1);
	}
}

int main(){
	read_input();
	m_main();

	return 0;
}