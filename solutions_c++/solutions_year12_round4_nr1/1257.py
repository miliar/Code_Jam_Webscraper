//Jakub Sygnowski
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
//#include<gmp.h> // http://gmplib.org/
//#include<gmpxx.h>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define ST first
#define ND second
#define INF 1000000007
#define PB push_back
#define MP make_pair
typedef pair<int,int> PII;
typedef long long LL;
#define MAXV 10007

int t, n, gdzie[MAXV], ile[MAXV], D, mam, last, dokad, gdz, best;
int jakdaleko[MAXV], najd, odkad;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		scanf("%d",&n);
		REP(i, n){ scanf("%d%d",&gdzie[i], &ile[i]); jakdaleko[i] = 0; }
		scanf("%d",&D);
		jakdaleko[0] = gdzie[0] + gdzie[0];
		najd = jakdaleko[0];
		odkad = 1;
		for(int i = 0; i < n; i++){
			for(int j = max(odkad, i + 1); j < n; j++){
				if (jakdaleko[i] >= gdzie[j]){
					jakdaleko[j] = max(jakdaleko[j], min(gdzie[j] - gdzie[i], ile[j]) + gdzie[j]);	
					odkad = j;
				} else
					break;
			}
			najd = max(najd, jakdaleko[i]);
		}

		printf("Case #%d: ",nr+1);
		if (najd >= D)
			printf("YES\n");
		else
			printf("NO\n");
	}
}
