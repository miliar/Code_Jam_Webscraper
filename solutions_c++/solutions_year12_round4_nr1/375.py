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
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow;

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		int N, d[10001], l[10001], tab[10001];
		memset(tab,-1,sizeof tab);

		scanf("%d", &N);

		fu(a,N){
			scanf("%d%d", &d[a], &l[a]);
		}

		scanf("%d", &d[N]);
		l[N] = 1000000000;

		tab[0] = d[0];

		fu(a,N){
			int gdzie = d[a], dlugosc = tab[a];
			for(int b=a+1; b<N+1 && d[b]-d[a] <= dlugosc; b++){
				tab[b] = min(l[b], max(tab[b], d[b]-d[a]));
			}
		}

		if( tab[N] >= 0 ){
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}

	return 0;
}
