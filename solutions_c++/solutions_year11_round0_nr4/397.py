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
	int T, N;
	int i, j;
	READ_INT(T);
	REP(i,T){
		READ_INT(N);
		int tmp, ret;
		ret = N;
		REP(j, N){
			READ_INT(tmp);
			if(tmp == j+1)ret--;
		}
		printf("Case #%d: %.7f\n", i+1, (double)ret);
	}
	return 0;
}
