#include <stdio.h>
#include <math.h>
#define	MAX	40

bool power[MAX];
bool state[MAX];

int main(){
	int n,k,t,tt,i,j;
	scanf("%d", &t);

	for(tt=0;tt<t;tt++){
		scanf("%d %d", &n, &k);
		if((k+1)%(1<<n)==0)
			printf("Case #%d: ON\n", tt+1);
		else
			printf("Case #%d: OFF\n", tt+1);
	}
    return 0;
}

