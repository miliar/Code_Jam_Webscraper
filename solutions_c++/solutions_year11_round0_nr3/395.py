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
		vector<unsigned int> vec(N);
		unsigned int tmp = 0;
		ll sum = 0;
		int min =1000001;
		REP(j, N){
			READ_INT(vec[j]);
			sum += vec[j];
			tmp ^= vec[j];
			if(min > vec[j])min = vec[j];
		}
		if(tmp==0)printf("Case #%d: %d\n", i+1, sum - min);
		else printf("Case #%d: NO\n", i+1);
	}
	return 0;
}
