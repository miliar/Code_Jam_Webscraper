#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <memory>
#include <cctype>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define FOR( i , a , n ) for (int i = (a); i <= (n) ; i++ )
#define REP( i , n ) for (int i = 0; i < (n) ; i++ )
#define debug(x) cout << #x" = " << x << "\n"
#define FORIT( i , c ) for ( __typeof((c).begin())  i  = (c).begin() ; (i) != (c).end() ; (i)++ )

#define MAXN 30

typedef long long ll;

int N,R;
ll k;
ll GAIN[1001][MAXN];
int NXT[1001][MAXN];
ll g[1001];


void calc(int n){
		int p = n;
		ll ret = 0;
		ll ppl = 0;
		while(ppl + g[p] <=k )
			{
			ppl+=g[p];
			ret+=g[p];
			p=(p+1)%N;
			if(p==n) break;
			}
		GAIN[n][0]=ret;
		NXT[n][0]=p;
	}

void doProblemC(){
	int T;
	cin>>T;
	REP(tcase,T){
		cout<<"Case #"<<tcase+1<<": ";
		cin>>R>>k>>N;
		REP(i,N)
			cin>>g[i];
		REP(i,N)
		  calc(i);
		for(int n = 1; n<MAXN; n++)	
			for(int g = 0; g < N ; g++){
				NXT[g][n]=NXT[NXT[g][n-1]][n-1];
				GAIN[g][n]=GAIN[g][n-1]+GAIN[NXT[g][n-1]][n-1];
			}
		ll ret = 0;
		int p = 0;
		for(int n = MAXN-1; n>=0; n--)
			if(R>=(1<<n))
				{
				ret+=GAIN[p][n];
				p=NXT[p][n];
				R-=(1<<n);
				}
		
		cout<<ret<<"\n";

	}

	
	
	}






int main() {
	doProblemC();
	return 0;
	}


