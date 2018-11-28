#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cassert>
#include <utility>
#include <sstream>
#include <cstring>
using namespace std;

#define FALL(ii,vv) for (int (ii)=0; (ii)<(vv).size();(ii)++)
#define REP(i,b) for(int (i)=(0);(i)<(b);(i)++)
#define FUP(i,a,b) for(int (i)=(a); (i)<=(b); (i)++)
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef vector<int> vi;
typedef long long ll;

const int MOD = 100003;

int newton[555][555];

int dp[555][555];

int go(int ilosc,int n){
	if (ilosc==1) return 1;
	if (n<=2) return 0;
	if (ilosc>=n) return 0;
	
	if (dp[ilosc][n]>=0) return dp[ilosc][n];
	int res = 0;
	for(int i=1; i<ilosc; i++){
		//printf("(%d %d) (%d %d) (n po k %d %d = %d) %d\n",ilosc,n, i,ilosc, n-ilosc-1,ilosc-i-1,newton[n-ilosc-1][ilosc-i-1], go(i,ilosc));
		res = (res + go(i,ilosc) * newton[n-ilosc-1][ilosc-i-1]) % MOD; 
	}
	dp[ilosc][n] = res;
	return res;
}

int main(){
	
	REP(i,501) REP(j,501){ dp[i][j]=-1; newton[i][j]=0; }
	FUP(i,0,500) newton[i][i] = newton[i][0] = 1;
	FUP(i,2,500) FUP(j,1,i-1) newton[i][j] = (newton[i-1][j]+newton[i-1][j-1]) % MOD;
	
	//REP(i,10){ REP(j,i+1) printf("%d ",newton[i][j]); puts(""); }
	
	
	int test,n;
	scanf("%d",&test);
	FUP(ii,1,test){
		scanf("%d",&n);
		int res = 0;
		FUP(i,1,n){
			res += go(i,n);
			//printf("ilosc = %d n = %d ---> %d\n",i,n,go(i,n));
		}
		res %= MOD;
		printf("Case #%d: %d\n",ii,res);
	}
	return 0;
}
