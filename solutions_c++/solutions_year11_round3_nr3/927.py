#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <fstream>
#include <numeric>
#include <map>
#include <iterator>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define INF 99999999
#define EPS 1e-7
#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)
#define REP(i,n) for(i=0; i<(n); i++)
#define FOR(i,a,b) for(i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()

#define SIZE 100+10
#define IN freopen("C-small-attempt0.in","r",stdin);
#define OUT freopen("out","w",stdout);

int T,N,L,H,freq[SIZE];

int gcd(int a,int b){
	return (!a)?b:gcd(b%a,a);
}

int main()
{
	IN
	OUT
	int t,i,j,lcm;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		scanf("%d %d %d",&N,&L,&H);
		REP(i,N) {scanf("%d",&freq[i]);}
		/*lcm = freq[0];
		FOR(i,1,N-1) {
			lcm = (lcm*freq[i])/gcd(lcm,freq[i]);
		}
		printf("lcm:%d\n",lcm);
		FOR(i,L,H) if(i%lcm == 0) {printf("%d\n",lcm);break;}
		if(i==H+1) printf("NO\n");*/
		FOR(i,L,H) {
			REP(j,N){
				if(i%freq[j]!=0 && freq[j]%i!=0) break;
			}
			if(j==N){
				printf("%d\n",i);
				break;
			}
		}
		if(i==H+1) printf("NO\n");
	}
	return 0;
}

