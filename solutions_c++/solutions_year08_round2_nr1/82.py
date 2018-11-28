#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define forn(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(__typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
#define ll long long
int N, n, m;
ll X[100010], Y[100010];
int main(){
	int i,j ,k, casos;
	scanf("%i", &N );
	for(int h = 0 ;h <  N ; h ++ ){
		scanf("%i", &n);
		ll A, B, C, D, x0, y0;
		ll M;
		scanf("%lld %lld %lld %lld %lld %lld %lld", &A, &B, &C, &D, &x0, &y0, &M);
// 		printf("ENTRO\n");
		X[0] = x0, Y[0] = y0;
		for(i=1;i<n;i++){
			X[i] = (A * X[i-1] + B ) % M;
			Y[i] = (C * Y[i-1] + D ) % M;
		}
// 		printf("SALIO\n");
		ll res = 0;
		ll cant[3][3];
		memset(cant,0,sizeof(cant));
		
		for(i=0;i<n;i++)cant[X[i]%3][Y[i]%3] ++ ;
		
		vector<pair<ll,pair<int,int> > > vec;
		for(i=0;i<3;i++)for(j=0;j<3;j++)vec.push_back(make_pair(cant[i][j], make_pair(i,j)));
		for(i=0;i<vec.size();i++)for(j=i;j<vec.size();j++)for(k=j;k<vec.size();k++){
			int a = 0, b = 0 ; 
			a += vec[i].second.first + vec[j].second.first  + vec[k].second.first;
			b += vec[i].second.second + vec[j].second.second + vec[k].second.second;
			a %= 3, b %= 3;
			if( a || b ) continue;
// 			printf(" %d %d\n", vec[i].second.first, vec[i].second.second);
// 			printf(" s  %d %d\n", vec[j].second.first, vec[j].second.second);
// 			printf(" t     %d %d\n", vec[k].second.first, vec[k].second.second);
			if( k == i ){
				ll c = vec[i].first;
				res += (c * ( c -1 ) * (c-2 ) ) / 6;
			}else if( k == j ){
				ll c1 = vec[i].first, c2 = vec[j].first;
				res += c1 * (c2 * (c2-1 )) / 2;
			}else if( j == i ){
				ll c1 = vec[i].first, c2 = vec[k].first;
				res += ((c1*(c1-1))/2) * c2;
			}else{
				ll c1 = vec[i].first, c2 = vec[j].first, c3 = vec[k].first;
				res += c1 * c2 * c3;
			}
		}
		printf("Case #%i: %lld\n", h+1, res);
	}
	
	
	return 0;
}





































