#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <math.h>
#include <cstring>
#include <complex>
using namespace std;

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef vector<vector<string> > VVS;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VPII;
#define rep(i,start,m) for(int i=(int)(start);i<(int)(m);i++)
#define showarray(array,m) for(int sa_i=0;sa_i<(int)(m);sa_i++) cout << array[sa_i] <<" "; cout << endl;
#define showvector(array) for(int sa_i=0;sa_i<(int)(array.size());sa_i++) cout << array[sa_i] << " "; cout << endl;
stringstream ss;
#define cast(a,b) ss.clear(); ss<<a; ss>>b; ss.clear();
#define rev(s) (string((s).rbegin(), (s).rend()))
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << endl;
#define clr(a) memset((a), 0, sizeof(a))
const int INF = INT_MAX;
string alpha = "abcdefghijklmnopqrstuvwxyz";
//INT_MAXで最大？

int dx[] = {-1,0,1,0,1,1,-1,-1};
int dy[] = {0,-1,0,1,1,-1,1,-1};


#define MAX_N 1000
int T;
ll n,D;
ll d[20000],l[20000];
ll length[20000];
void solve(){
	//if(n>4) return;
	//cout << n << " " << D << endl;showarray(d,n); showarray(l,n); cout << "*****" << endl;
	clr(length);
	length[0] = d[0];
	if(n==1){
		if(length[0]+d[0] >= D)	{
			cout << "YES" << endl;
		}else{
			cout << "NO" << endl;
		}
		return;
	}
	if(length[0]+d[0] >= D)	{
		cout << "YES" << endl;
		return;
	}
	rep(i,0,n){
		//cout << i << " " << d[i] << " " << l[i] << endl;
		rep(j,i+1,n){
			if(d[j]-d[i]>length[i]) break;
			length[j] = max(length[j], min(d[j]-d[i],l[j]));
			if(length[j]+d[j] >= D){
				cout << "YES" << endl;
				return;
			}
		}
		//showarray(length,n);
	}
	cout << "NO" << endl;
}

int main () {
	freopen("/Users/katsuma/c++/input.txt","rt",stdin);
	freopen("/Users/katsuma/downloads/A-small-attempt2.in","rt",stdin);
	freopen("/Users/katsuma/downloads/A-large.in","rt",stdin);
	freopen("/Users/katsuma/downloads/A-small-attempt2out.txt","wt",stdout);
	freopen("/Users/katsuma/downloads/A-largeout.txt","wt",stdout);
	cin >> T;
	rep(tttt,0,T){
		//fprintf(stderr, "%d / %d\n", tttt, T);
		cin >> n;
		rep(i,0,n) cin >> d[i] >> l[i];
		cin >> D;
		//if(tttt!=9) continue;
		cout << "Case #" << tttt+1 << ": " ; 
		solve();
	}
}








