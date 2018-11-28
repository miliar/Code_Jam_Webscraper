#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <ctime>
using namespace std;

#define sz size()
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<vector<double> > vvd;
const int INF=2000000000;
const double eps=1e-7;
vector<pair<int,int> > d;

int main() {
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
   // freopen("input.txt","r",stdin);
	int t;
	cin>>t;
	srand(time(NULL));
	rep(T,t){
		cout<<"Case #"<<T+1<<": ";
		int n,g,h;
		cin>>n;
		vint a(n-1);
		rep(i,n-1){cin>>a[i];a[i]--;}
		vector<int> b(n);
		int F=0;
		FOR(od,1,400){
			int uh=rand()%(2*n) + 1;
			if(F)break;
			rep(i,n)b[i]=rand()%uh;
			rep(it,14880){
				random_shuffle(all(b));
				int i;
				for(i=0;i<n-1;i++){
					vector<double> g(n);
					FOR(j,i+1,n-1){
						g[j]=atan((b[j]-b[i])/((j-i)*2.0));
					}
					if(max_element(g.begin()+i,g.end())-g.begin()!=a[i])break;
				}
				if(i==n-1){
					F=1;
					break;
				}
			}
			
		}
		if(F){
			rep(i,n)cout<<b[i]<<' ';
			cout<<endl;
		}else{
			puts("Impossible");
		}
	}
	
	
    return 0;
}
