#include<cstdio>
#define FOR(a,b) for(int a=0;a<b;++a)

int main(){
	int x,a,b,z,c;
	scanf("%d",&z);
	FOR(x,z){
		printf("Case #%d: ",x+1);
		scanf("%d %d", &a, &b);
		c=b;
		FOR(i,a) b|=(1<<i);
		if(b==c) printf("ON\n"); else printf("OFF\n");
	}
}
/*
4
1 0
1 1
4 0
4 47

Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON

*/
