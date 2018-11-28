#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

typedef long long ll;

int dist[10011];
int l[10011];
int goal;
int dp[10011];

int main(){
	int cases;
	cin >> cases;
	for(int c=1; c<=cases; ++c){
		printf("Case #%d: ",c);
		int vines;
		cin >> vines;
		for(int i=1; i<=vines; ++i){
			cin >> dist[i] >> l[i];
			dp[i]=-1;
		}
		dp[0]=-1;
		dist[0]=0;
		l[0]=dist[1];
		cin >> dist[vines+1];
		l[vines+1]=0;
		dp[vines+1]=0;
		int d;
		for(int i=vines; i>=0; --i){
			for(int j=i+1; j<=vines+1; ++j){
				d=dist[j]-dist[i];
				if(d>l[i]) break;
				if(dp[j]==-1) continue;
				if(d>=dp[j]){
					if(dp[i]==-1 || d<dp[i]) dp[i]=d;
				}
			}
		}
		if(dp[0]>0){
			printf("YES\n");
		}else{
			printf("NO\n");
		}

	}

	return 0;
}

