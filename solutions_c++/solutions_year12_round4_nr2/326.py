#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#include <ctime>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow;
int n,w,l;
int Z=1000000;
vector<pair<int,int> > r; // promien x indeks
int x[1000], y[1000];

int main(){

	srand(time(0));

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);

		r.clear();
		memset(x,-1,sizeof x);
		memset(y,-1,sizeof y);
		
		scanf("%d%d%d", &n, &w, &l);

		fu(a,n){
			int tmp;
			scanf("%d", &tmp);	
			r.pb(make_pair(tmp,a));
		}

		sort(ALL(r));

		int sze=0, wys = 0, nextWys = 0;
			
		for(int i=r.size()-1; i>=0; i--){
			if( sze > 0 && sze+r[i].first > w ){
				sze = 0;
				wys = nextWys;
			}

			if( sze == 0 ){
				x[r[i].second] = 0;
				sze = r[i].first;
				nextWys = wys + r[i].first;
				if( wys > 0 ) nextWys += r[i].first;
			} else {
				x[r[i].second] = sze + r[i].first;
				sze += 2*r[i].first;
			}

			if( wys == 0 ){
				y[r[i].second] = 0;
			} else {
				y[r[i].second] = wys + r[i].first;
			}

			if( x[r[i].second] < 0 || x[r[i].second] > w || y[r[i].second] < 0 || y[r[i].second] > l ){
				cerr << "####" << endl;
				cerr << "####" << endl;
				cerr << "####" << endl;
				cerr << "####" << endl;
				cerr << "i: " << i << " r.size(): " << r.size() << " sze: " << sze << " wys: " << wys << endl;
				cerr << x[r[i].second] << " " << y[r[i].second] << endl;
				int bleah = 1/(1-1);
			}

		}

		fu(a,n){
			printf("%d %d ", x[a], y[a]);
		}
		printf("\n");
	}

	return 0;
}
