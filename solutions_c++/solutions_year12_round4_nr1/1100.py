#include <iostream>
#include <vector>
#include <cstdio>
#include <queue>
#include <cstring>
#define MAX 10010

using namespace std;

class Info
{
public:
	int at,len;
};

int main(){
	int T,N,Dist;
	int i,k;
	Info I,II;
	int D[MAX],L[MAX];
	
	k = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&N);
		for(i=0;i<N;i++)
			scanf("%d %d",&D[i],&L[i]);
		scanf("%d",&Dist);

		printf("Case #%d: ",k);
		
		queue<Info> q;
		I.at = 0;
		I.len = D[0];
		q.push(I);
		
		bool ans = false;
		for(i=1;!q.empty();){
			I = q.front(); q.pop();
			if(I.len >= (Dist - D[I.at])){
				ans = true;
				break;
			}
			
			for(;i<N && (D[i]-D[I.at]) <= I.len;i++){
				II.at = i;
				II.len = min(L[i],D[i]-D[I.at]);
				q.push(II);
			}
		}
		
		if(ans) printf("YES\n");
		else printf("NO\n");
		
		k++;
	}
	return 0;
}
