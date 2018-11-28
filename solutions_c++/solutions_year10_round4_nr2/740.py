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
int pot[15];
int p, m[2000];

int main(){
	
	pot[0] = 1;
	for(int a=1; a<15; a++) pot[a] = pot[a-1] * 2;

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		memset(m,0,sizeof m);

		scanf("%d",&p);

		fu(a,pot[p]) scanf("%d",&m[a]);
		fu(a,pot[p]) m[a] = p - m[a];
		
		int tmp;
		for(int a=p-1; a>=0; a--){
			fu(b,pot[a]) scanf("%d",&tmp);	
		}
		
		int res = 0;

		fu(a,p){
			int gdzie = 0;
			fu(b,pot[a]){
				bool ok = false;
				fu(c,pot[p-a]){
					 if( m[ gdzie + c ] > 0 ){
						ok = true;	
					}
				}
				if( ok ){
					res++;
					for(int c=0; c<pot[p-a]; c++){
						 m[gdzie+c] = m[gdzie+c] - 1;
					}
				}
				gdzie += pot[p-a];
			}
		}

		printf("%d\n",res);
	}

	return 0;
}
