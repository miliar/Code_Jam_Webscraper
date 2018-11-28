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
		
		int N;
		scanf("%d", &N);

		int sum=0, xorr=0, mn=-1;
			
		fu(a,N){
			int tmp;
			scanf("%d",&tmp);

			sum += tmp;
			xorr = xorr ^ tmp;

			if( mn == -1 || mn > tmp ){
				mn = tmp;
			}
		}

		if( xorr != 0 ){
			printf("NO\n");
		} else {
			sum -= mn;
			printf("%d\n", sum);
		}
	}

	return 0;
}
