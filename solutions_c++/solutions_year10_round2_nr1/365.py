#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

#define ME(s) memset((s), 0, sizeof((s)))
#define MM(s,a) memset((s),(a),sizeof((s)))
#define MCP(s,a) memcpy((s), (a), sizeof(s))
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PDD pair<double, double>
#define mkp(a,b) make_pair((a),(b))
#define y first
#define x second
#define sqr(a) ((a)*(a))
#define lowbit ((x)&(-(x)))
#define two(x) (1<<(x))
#define contain(mask,x) ((mask&two(x))!=0) 

FILE *fin=freopen("A.in","r",stdin);
FILE *fout=freopen("A.out","w",stdout);
set<string> H;

int work(string s){
	s+='/';
	for(int i=1;i<s.size();i++)
		if(s[i]=='/'){
			string p=s.substr(0,i);
			H.insert(p);
			//cout << p << endl;
		}
}

int main(){
	int T,c=0;
	cin >> T;
	while(T--){
		H.clear();
		int N,M;		
		cin >> N >> M;
		for(int i=0;i<N;i++){
			string s;
			cin >> s;
			work(s);
		}
		int ans=H.size();
		for(int i=0;i<M;i++){
			string s;
			cin >> s;
			work(s);
		}
		ans=H.size()-ans;
		cout << "Case #" << ++c << ": " << ans << endl;
	}
	return 0;
}

//Powered by [KawigiEdit] 2.0!

