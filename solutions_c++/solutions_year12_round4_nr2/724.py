//#pragma comment(linker, "/STACK:32777216")
#include <iostream> 
#include <vector>
#include <set>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
#include <memory.h>
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define RFOR(i,a,b) for(int (i)=(a)-1;(i)>=(b);--(i))
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define PII pair<int,int>
#define CLEAR(a) memset((a),0,sizeof((a)))
#define X first
#define Y second
#define sz(a) (int)(a).size()

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;

const double pi=3.141592653589793;
const int INF=1000000000;
const ll mod=1000000007;

int dp[10005];

double dist(double x1,double y1,double x2,double y2){
       return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));       
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	FOR(ttt,0,t){
		cout << "Case #" << ttt + 1 << ": ";
		int n;
        cin >> n;
        double w,l;
        cin >> w >> l;
         vector<pair<double,int> > a(n);
        FOR(i,0,n){
                  cin >> a[i].first;
                  a[i].second = i;
        }
        sort(ALL(a));
        vector<pair<double, double> > res(n);
        vector<pair<double, double> > coor(n);
        FOR(i,0,n)
                  coor[i] = MP(-1,-1);
        RFOR(i,n,0){
                    bool ww = 0;
                    for(double x = 0; x < w; x += w/1000){
                               for(double y = 0; y < l; y += l/1000){
                                          bool q = 1;
                                          FOR(j,i+1,n)
                                                if (dist(x,y,coor[j].X,coor[j].Y) < a[i].X+a[j].X + 1e-9)
                                                   { q = 0; break;}
                                          if (q) {coor[i] = MP(x,y);ww = 1;break;}                        
                               }            
                               if (ww) break;
                    }
        }
        FOR(i,0,n)
                  res[a[i].Y] = coor[i];
        FOR(i,0,n)
                  printf("%.20f %.20f ",res[i].X,res[i].Y);
        cout << endl;
		cerr<<ttt+1;
	}
	return 0;
}
