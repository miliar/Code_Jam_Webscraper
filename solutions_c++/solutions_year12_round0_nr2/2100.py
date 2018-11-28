// <-------------------[sWitCHcAsE]---------------------->
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<cstring>
#include<cassert>
#include<queue>

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORS(i,a,n) for(int i=a;i<n;i++)
#define ERR(x) cerr<<#x<<" "<<x<<endl
#define pb push_back

using namespace std;

typedef vector<int> VI;
typedef long long ll;
typedef long double ld;

int N,S,P;
int scores[150];
int prepro[35][2];
int dp[100][100];

#define INF 99999;

int solve(int curr, int Sleft) {
	if( curr>=N && Sleft==0)return 0;
	if ( curr>=N && Sleft>0)return -INF;
	if ( curr==N-1 && Sleft>1)return -INF;
	if( dp[curr][Sleft]!=-1) return dp[curr][Sleft];
	dp[curr][Sleft] = (prepro[scores[curr]][0]>=P);
	dp[curr][Sleft] += solve(curr+1, Sleft);
	if ( Sleft>0 && prepro[scores[curr]][1]>0)
	dp[curr][Sleft] = max(dp[curr][Sleft], (prepro[scores[curr]][1]>=P) + solve(curr+1, Sleft-1));
	return dp[curr][Sleft];

}


int main(int argc,char** args)
{
	int kases=0,T;
	memset(prepro,-1, sizeof prepro);
	FOR(i,11) {
		FORS(j,i,11) {
			FORS(k,j,11) {
					int s = i+j+k;
					int mn = min(i,min(j,k));
					int mx = max(i,max(j,k));
					if ( mx-mn >2)continue;
					if (mx-mn==2)prepro[s][1]=max(prepro[s][1],mx);
					else prepro[s][0]=max(prepro[s][0],mx);
				
			}
		}
	}
	scanf("%d", &T);
	while(kases<T) {
		kases++;
		cout<<"Case #"<<kases<<": ";
		scanf("%d", &N);
		scanf("%d", &S);
		scanf("%d", &P);
		FOR(i,N) {
			scanf("%d", &scores[i]);
		}
		memset(dp, -1, sizeof dp);
		int ans = solve(0,S);
		if(ans<0)ans=0;
		cout<<ans<<endl;
	}
}
