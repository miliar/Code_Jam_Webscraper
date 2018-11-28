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
#define un(a) a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow, k;
char t[1010], tmp[1010];

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		fu(a,1010) t[a]=tmp[a]=0;
		scanf("%d",&k);
		scanf("%s",t);
	
		int n = strlen(t);

		vi permut;
		fu(a,k) permut.pb(a);

		int score = -1;
		
		do {
			fu(a,n/k){
				fu(b,k) tmp[ k*a+b ] = t[ k*a +permut[b] ];
			}
			int gdzie=0, zlicz=0;
			while( gdzie < n ){
				zlicz++;
				while( gdzie+1<n && tmp[gdzie] == tmp[gdzie+1] ) gdzie++;
				gdzie++;
			}
			if( score == -1 || score > zlicz ) score = zlicz;
		} while( next_permutation(ALL(permut)) );

		printf("Case #%d: %d\n",q,score);
	}

	return 0;
}
