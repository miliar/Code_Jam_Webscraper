
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

const int maxn = 1e3+10;
int N,W,L;
int r[maxn];

double x[maxn], y[maxn];

int ok() {
	//rep(i,N) printf(" %lf %lf", x[i],y[i]); puts("");
	rep(i,N) if(x[i] < 0 || x[i] > W || y[i] < 0 || y[i] > L) return 0;
	rep(i,N) rep(j,N) if(i < j) {
		double d = sqrt(pow(x[i]-x[j],2.0)+pow(y[i]-y[j],2.0));
		if(d < r[i]+r[j]) {
			//dbg(i _ j _ d _ r[i] _ r[j]);
			return 0;
		}
	}
	return 1;
}

int main() {
  int T;
  cin>>T;
  for(int caso=1;caso<=T;caso++){
    cin>>N>>W>>L;
    for(int i=0;i<N;i++) cin >> r[i];
    rep(i,1<<N){
    	vector< pair<int,int> > a, b;
    	rep(j,N) if(i >> j & 1) a.push_back(mp(r[j],j)); else b.push_back(mp(r[j],j));
    	sort(a.begin(),a.end());
    	sort(b.begin(),b.end());
    	double xx,yy;
    	
    	rep(k,2) {
    		rep(l,2) {
    		
    			xx=0,yy=0;
    			rep(q,a.size()) {
    				int id=a[q].second;
    				if(xx!=0)xx+=r[id];
    				x[id]=xx,y[id]=yy;
    				xx+=r[id];
    			}
    			xx=W,yy=L;
     			rep(q,b.size()) {
    				int id=b[q].second;
    				if(xx!=W)xx-=r[id];
    				x[id]=xx,y[id]=yy;
    				xx-=r[id];
    			}
    			if(ok()) goto end;
    			
    			//goto end;

    			xx=0,yy=0;
    			rep(q,a.size()) {
    				int id=a[q].second;
    				if(yy!=0)yy+=r[id];
    				x[id]=xx,y[id]=yy;
    				yy+=r[id];
    			}
    			xx=W,yy=L;
     			rep(q,b.size()) {
    				int id=b[q].second;
    				if(yy!=L)yy-=r[id];
    				x[id]=xx,y[id]=yy;
    				yy-=r[id];
    			}
    			
    			if(ok()) goto end;    			
    			
    			reverse(b.begin(),b.end());
    		}
    		reverse(a.begin(),a.end());
    	}
    }
    assert(0);
    end:;
    printf("Case #%d:",caso);
    rep(i,N) printf(" %lf %lf", x[i],y[i]);
    puts("");
  }
  return 0;
}

