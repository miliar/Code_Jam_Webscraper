#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <numeric>
#include <queue>
#include <iostream>
#include <string>
#include <cstring>
#include <utility>
#define sz(a) int((a).size())
#define pb push_back
#define mk make_pair
#include <cmath>
#define fi first
#define se second
#define Rep(i,j,k) for (int i=(j); i<=(k); i++)
#define Repd(i,j,k) for (int i=(j); i>=(k); i--)
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define SUM(a) accumulate(all(a),string())
#define online1
#define eps (1e-10)
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;

int n, d[20000], l[20000];
int f[20000];

int main(){

	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int TT;
	cin>>TT;
	
	Rep(tt,1,TT){
		cin>>n;
		Rep(i,1,n) scanf("%d%d",d+i,l+i);
		scanf("%d",d+n+1); l[n+1]=0;
		
		memset(f,0,sizeof(f));
		f[1]=min(l[1],d[1]);
		bool ff=0;
		Rep(i,1,n){
			Rep(j,i+1,n)
				if (d[j]-d[i]<=f[i]){
					int dd=d[j]-d[i];
					f[j]=max(f[j],min(l[j],dd));
				}
			//cout<<i<<" "<<f[i]<<endl;
			if (f[i]>=d[n+1]-d[i])
				ff=true;
		}
		
		printf("Case #%d: ",tt);
		if (ff) puts("YES"); else puts("NO");
	}

    return 0;
}
