#include <cstdio>
#include <queue>

using namespace std;

int main(){
	int orange[200], blue[200], q[200];
	int oFront, bFront, oSize, bSize, n, front,step, oPos, bPos, pressed;
	int T,CASE=1;
	scanf("%d\n",&T);
	while(T--){
		front = 0;
		oPos = 1;
		bPos = 1;
		oSize = 0;
		bSize = 0;
		oFront = 0;
		bFront = 0;
		step = 0;
		
		scanf("%d\n",&n);
		char a;
		int tmp;
		for(int i=0; i<n; i++){
			scanf("%c\n",&a);
			scanf("%d\n",&tmp);
			if(a == 'O'){
				orange[oSize++] = tmp;
				q[i] = tmp;
			}else{
				blue[bSize++] = -tmp;
				q[i] = -tmp;
			}
		}
		
		
		
		while(front < n){
			step++;
			pressed = 0;
			//printf("%d %d %d\n",q[front], orange[oFront], blue[bFront]);
			if(oFront < oSize){
				if(oPos == orange[oFront]){
					if(q[front]>0){
						front++;
						oFront++;
						pressed = 1;
					}
				}else{
					if(oPos < orange[oFront]){
						oPos++;
					}else{
						oPos--;
					}
				}
			}
			
			if(bFront < bSize){
				if(bPos == -blue[bFront]){
					if(q[front]<0 && !pressed){
						front++;
						bFront++;
					}
				}else{
					if(bPos < -blue[bFront]){
						bPos++;
					}else{
						bPos--;
					}
				}
			}
			
		}
	
		printf("Case #%d: %d\n",CASE++,step);
	}
}

