#include<stdio.h>
#include<iostream>
using namespace std;

int main(void){
	int o[101], b[101];
	int o_p, b_p;
	char order[102];
	int T, N, but;
	char c;
	int O , B, time, sec;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		O = B = time = 0;
		scanf("%d ",&N);
		for(int i=0;i<N;i++){
			scanf("%c %d",&c,&but);	
			if(i!=N-1) scanf(" ");
			if(c=='O') o[O++] = but;
			else b[B++] = but;	
			order[i] = c;
		}
		o_p = b_p = 1; /* Start at buttom 1 */
		O = B = 0;
		for(int i=0;i<N;i++){
			/* Next buttom is O's */
			if(order[i]=='O'){
				/* Move O to his buttom */
				sec =   (o[O]-o_p)>=0?o[O]-o_p:-(o[O]-o_p);
				sec+=1;
				time += sec;
				o_p = o[O++];
				/* Move B (until he makes to his buttom) */
				if(b_p<b[B]) b_p = (b_p+sec>b[B])?b[B]:b_p+sec;
				else if(b_p>b[B]) b_p = (b_p-sec<b[B])?b[B]:b_p-sec;
			}else{
				/* Move B to his buttom */
				sec =   (b[B]-b_p)>=0?(b[B]-b_p):-(b[B]-b_p);
				sec += 1;
				time += sec;
				b_p = b[B++];
				/* Move O (until he makes to his buttom) */
				if(o_p<o[O]) o_p = (o_p+sec>o[O])?o[O]:o_p+sec;
				else if(o_p>o[O]) o_p = (o_p-sec<o[O])?o[O]:o_p-sec;
			}
		}
		printf("Case #%d: %d\n",t,time);
	}
	return 0;
}
