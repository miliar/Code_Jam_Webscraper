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
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow,n,A,B,C,D,M;
ll xx,yy;

int main(){
	
	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
	
		scanf("%d%d%d%d%d%lld%lld%d",&n,&A,&B,&C,&D,&xx,&yy,&M);

		vector<long long> x; x.clear();
		vector<long long> y; y.clear();

		x.pb(xx);
		y.pb(yy);
	
		for(int i=1; i<=n-1; i++){
			x.pb( (ll)(A*xx+B)%M );
			y.pb( (ll)(C*yy+D)%M );
			xx = (ll)(A*xx+B)%M;
			yy = (ll)(C*yy+D)%M;
		}
		
		int score = 0;

		for(int a=0; a<n; a++) for(int b=a+1; b<n; b++) for(int c=b+1; c<n; c++) if( (ll)(x[a]+x[b]+x[c])%3==0 && (ll)(y[a]+y[b]+y[c])%3==0 ) score++;

		printf("Case #%d: %d\n",q,score);
	}

	return 0;
}
