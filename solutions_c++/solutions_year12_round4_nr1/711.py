
#include <bits/stdc++.h>
#define rep(x,n) for(int x = 0; x < n; ++x)
#define print(x) cout << x << endl
#define dbg(x) cerr << #x << " == " << x << endl
#define _ << " , " <<
#define mp make_pair
#define x first
#define y second
using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;
typedef pair<int,int> pii;

const int maxn = 1e4+10;
int N,D;
int d[maxn], l[maxn], can[maxn];

int main() {
  int T;
  cin>>T;
  for(int caso=1;caso<=T;caso++){
    cin>>N;
    for(int i=0;i<N;i++) cin >> d[i] >> l[i];
    cin>>d[N]; l[N]=1e9;
    memset(can,-1,sizeof can);
    can[0]=d[0];
    for(int i=0;i<N;i++){
    	int x = d[i] + can[i];
    	for(int j=i+1;j<=N;j++){
    		if(x>=d[j]) {
    			can[j]=max(can[j],min(l[j],d[j]-d[i]));
    		}
    	}
    }
    printf("Case #%d: %s\n",caso, can[N]>=0?"YES":"NO");
  }
  return 0;
}

