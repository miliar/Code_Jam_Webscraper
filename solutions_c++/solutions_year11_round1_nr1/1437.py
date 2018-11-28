#include <cstdio> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <cmath> 
#include <utility> 
 
#define MP make_pair 
#define PB push_back 
 
using namespace std; 
 
#define REP(i,n) for(i=0;(i)<(int)(n);(i)++) 
typedef long long ll; 
 
#define READ_INT(a) scanf("%d", &a); 
#define READ_LL(a) scanf("%I64d", &a); 
#define READ_STRING(a) cin >> a; 

int main ()
{
	int T, t;
	READ_INT(T);
	REP(t,T){
		ll N;
		int Pd, Pg;
		READ_LL(N);
		READ_INT(Pd);
		READ_INT(Pg);
		ll i;
		int flag = 0;
		REP(i, N){
			if((((i+1)*Pd) % 100)==0){
				flag = 1;
				break;
			}
		}
		if(flag == 0){
			printf("Case #%d: Broken\n", t+1);
			continue;
		}
		if(Pg == 100 && Pd != 100){
			printf("Case #%d: Broken\n", t+1);
			continue;
		}
		if(Pg == 0 && Pd != 0){
			printf("Case #%d: Broken\n", t+1);
			continue;
		}
		printf("Case #%d: Possible\n", t+1);
	}
	return 0;
}
