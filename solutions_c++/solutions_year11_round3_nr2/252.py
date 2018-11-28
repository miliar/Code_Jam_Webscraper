#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<numeric>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

#define MAX 1000000
long long a[MAX+3];
long long ac[MAX+3];
long long dist[MAX+3];
int main(){
	int runs;
	cin>>runs;
	for(int r = 1; r<=runs;r++){
		long long L,t,N,C;
		cin>>L>>t>>N>>C;
		memset(a,0,sizeof a);
		memset(dist,0,sizeof dist);
		memset(ac,0,sizeof ac);				
		long long s = 0;
		long long M = 0;
		for(int i = 0; i < C; i++) cin>>a[i];

		ac[0] = 0;
		for(int i = 1, j = 0; i <= N; i++, j++){
			dist[i] = a[j%C];
			ac[i] = dist[i] + ac[i-1];
			s += dist[i];
		}
		s *= 2;
		int id = lower_bound(ac,ac+N,t/2) - ac;
		vector<long long> H;
		H.push_back(t/2-ac[id]);
		for(int i = id+1; i <= N; i++) {
			H.push_back(-dist[i]);
		}
		sort(H.begin(),H.end());
		for(int i = 0, it = 0; i < L && it < H.size(); i++, it++){
			s += H[it];
		}
		printf("Case #%d: %lld\n",r,s);
		
		
		
	}
	
	return 0;
}
