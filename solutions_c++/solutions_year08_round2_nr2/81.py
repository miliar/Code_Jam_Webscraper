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

ll primos[400000];
ll p[ 1000010 ], rank[ 1000010 ];
ll find(ll a ){
	if( a != p[a] ) p[a] = find(p[a]);
	return p[a];
}
void link(ll a, ll b ){
	if( rank[a] > rank[b] ) p[b] = p[a];
	else p[a] = p[b];
	if( rank[a] == rank[b] ) rank[b] ++;
}
void join ( ll a, ll b ){link(find(a),find(b));}


int main(){
	int casos;
	ll i , j, k;
	bool mark[1000001];
#define MM 1000000
	for(i=0;i<=MM;i++) mark[i] = true;
	mark[0] = mark[1] = false;
	for(i=2;i<=1000;i++){
		if( !mark[i] ) continue;
		ll a = i + i;
		while( a <= MM ){ mark[a] = false; a += i;}
	}
	int cant = 0;
	for(i=0;i<MM;i++)if( mark[i] ) primos[cant++] = i;
	
	scanf("%i", &casos);

	ll A, B, P;
	for(int h = 0 ; h < casos ; h++ ){
		scanf("%lld %lld %lld", &A, &B, &P);
// 		printf("HATA A\n");
		for(i=A;i<=B;i++) p[i-A] = i-A, rank[i-A] = 0;
		
		for(i=0;i<cant;i++){
			if( primos[i] < P || primos[i] > B) continue;
			ll first;
			if( A % primos[i] == 0 ) first = A;
			else first = ((A+primos[i])/primos[i]) * primos[i];
			ll AUX = first;
			while( AUX <= B ){
				join(AUX-A,first-A);
				AUX += primos[i];
			}
		}
		set<ll> S;
		for(i=A;i<=B;i++){
			S.insert(find(i-A));
		}
		printf("Case #%i: %i\n", h+1, S.size());
	}
	
	return 0;
}
