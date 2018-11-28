#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

int main(){
	//freopen("in.in","rt",stdin);
	//freopen("out.out","wt",stdout);

	int R,K,N,T,i,j,P;		
	scanf("%d",&T);	
	for(i = 0; i < T; i++){
		scanf("%d %d %d",&R,&K,&N);
		queue <int>Q;
		for(j = 0; j < N; j++){
			scanf("%d",&P);
			Q.push(P);
		}
		
		int max = 0;
		for(j = 0; j < R; j++){
			int k = 0;
			int f = 0;
			while(k + Q.front() <= K ){
				f++;
				Q.push(Q.front());
				k +=  Q.front();
				Q.pop();

				if(f >= N)
					break;
			}
			max += k;
		}
		printf("Case #%d: %d\n",i+1,max);
	}

	//fclose(stdin);
	//fclose(stdout);
	return 0;
}

