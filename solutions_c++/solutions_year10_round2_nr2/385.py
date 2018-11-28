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
int N, ile, obora, czas;
int x[100];
int v[100];
int t[100];

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		scanf("%d%d%d%d",&N,&ile,&obora,&czas);

		fu(a,N){
			scanf("%d",&x[a]);
		}

		fu(a,N){
			scanf("%d",&v[a]);
			t[a] = ceil((double)(obora - x[a]) / v[a]);
		}

		int ileNieDojdzie = 0;
		int res = 0;

		for(int a=N-1; a>=0 && ile > 0; a--) 
			if( t[a] <= czas ){
				res += ileNieDojdzie;	
				ile--;
			} else {
				ileNieDojdzie++;
			}
		
		if( ile == 0 ){
			printf("%d\n",res);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}
