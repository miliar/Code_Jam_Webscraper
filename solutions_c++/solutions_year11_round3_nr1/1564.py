#include<cstdio>
#include<vector>
#include<list>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<time.h>
#include<iostream>
#include<map>
#include<set>
using namespace std;
#define REP(i,n) for(int i=0;i<(n); ++i)
#define FOREACH(it,V) for(typeof((V).begin()) it = (V).begin(); it!=(V).end(); ++it)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define ALL(c) ((c).begin(),(c).end())
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LLL;

int CN = 0;

char arr[1000][1000];

void scase(){
	int res, N, M;
	scanf("%d%d", &N, &M); REP(i, N) scanf("%s", arr[i]);
	bool ans = true;
	REP(i,N) REP(j,M){
		if(arr[i][j]=='#'){
			if(arr[i][j+1]=='#'&&i<N-1&&arr[i+1][j+1]=='#'&&arr[i+1][j+1]=='#'){
				arr[i][j] = '/';
				arr[i][j+1] = '\\';
				arr[i+1][j] = '\\';
				arr[i+1][j+1] = '/';
			}
			else { ans =false ; goto out;}
		}
	}out:
	printf("Case #%d:\n", ++CN);
	if(ans)
	REP(i,N)
		printf("%s\n", arr[i]);
	else printf("Impossible\n");
}

int main(){
	int z; scanf("%d", &z); while(z--) scase();
	return 0;
}

