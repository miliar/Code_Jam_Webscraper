#include<cstdio>
#include<cstring>
//#include<conio.h>

int N, S, Q;
char query[1000][128], search[100][128];

int doit(int idx){
	//printf("trying %d-%s with %s\n", idx, query[idx], search[en]);
    //getch();
    if(idx==Q) return 0;
	int max=idx;
	for(int j, i=0; i<S; i++){
		j=idx;
		while(strcmp(query[j], search[i])!=0 && j<Q) j++;
		if(j==Q) return 0;
		if(max<j) max=j;
	}
	return 1+doit(max);
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &N);
	for(int c=1; c<=N; c++){
		scanf("%d", &S);
		for(int i=0; i<S; i++) scanf(" %[^\n]", search[i]);
		scanf("%d", &Q);
		for(int i=0; i<Q; i++) scanf(" %[^\n]", query[i]);
		//printf("%d %d\n", S, Q);
		printf("Case #%d: %d\n", c, doit(0));
	}
	//getch();
	return 0;
}
