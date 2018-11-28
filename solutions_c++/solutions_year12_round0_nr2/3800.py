#include <cstdio>

void working(int round){
	int N,S,P;
	int i,n;
	int input;
	int cnt = 0;
	int now;
	
	scanf("%d %d %d",&N,&S,&P);
	for(i=0;i<N;i++){
		scanf("%d",&input);
		for(n=10;n>=P;n--){
			now = input;
			now = now-n;
			if(now < 0)continue;
			if(n == 0){
				cnt++;
				break;
			}
			if(now - (n-1) - (n-1) < 0){
				if(n == P && S > 0){
					if(now - (n-2) - (n-2) < 0){
						continue;
					}
					else {
						S--;
						cnt++;
						//printf("input:%d n:%d S:%d\n",input,n,S);
						break;
					}
				}
				else continue;
			}
			else {
				cnt++;
				//printf("input:%d n:%d S:%d\n",input,n,S);
				break;
			}
		}
	}
	printf("Case #%d: %d\n",round,cnt);
}
int main(){
	int T;
	int i;
	
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		working(i);
	}
	return 0;
}