#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
using namespace	std;

int num_robo(char R){
	switch(R){
		case 'O':
			return 0;
		case 'B':
			return 1;
	}
}


int main(){
#ifdef	xDx
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int T,N;
	int pos[2];
	scanf("%d",&T);
	for(int i=0; i < T; i++){
		scanf("%d",&N);
		char R;
		int P;
		pos[0] = pos[1] = 1;
		int pred = 0, answ_time = 0, time_pred = 0;
		for(int j = 0 ; j < N; j++){
			getchar();
			scanf("%c %d",&R,&P);
			int cur = num_robo(R);
			if(pred != cur){
				int tmp = abs(P - pos[cur]) + 1;
				pos[cur] = P;
				if(tmp>time_pred){
					answ_time+=tmp-time_pred;
					time_pred = tmp-time_pred;					
				}
				else{
					answ_time++;
					time_pred=1;
				}
				pred = cur;
			}
			else{
				int tmp = abs(P - pos[cur]) + 1;
				pos[cur] = P;				
				answ_time+=tmp;
				time_pred += tmp;									
			}

		}
		printf("Case #%d: %d\n",i+1,answ_time);

	}

	return 0;
}