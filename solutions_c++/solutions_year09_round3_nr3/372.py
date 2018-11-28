#include<cstdio>
#include<algorithm>
using namespace std;

#define MAX 110
#define MAXQ 10

int P,Q;
int querry[MAXQ];

int simulate(){
	int i,j,k;
	char map[MAX];
	for(i=1;i<=P;i++){
		map[i]=1;
	}
	map[0] = 0;
	map[P+1] = 0;
	int value = P-1;
	map[querry[0]] = 0;
	for(i=1;i<Q;i++){
		for(j=querry[i]+1;map[j];j++){
			value++;
		}
		for(j=querry[i]-1;map[j];j--){
			value++;
		}
		map[querry[i]] = 0;
	}
	return value;
}

int main(){
	int cases,i,j,k=1;
	int min,v;
	scanf("%d\n",&cases);
	while(cases--){
		scanf("%d %d\n",&P,&Q);
		for(i=0;i<Q;i++){
			scanf("%d\n",&querry[i]);
		}
		sort(querry,querry+Q);
		min = simulate();
		while(next_permutation(querry,querry+Q)){
			v = simulate();
			if(min > v)
				min = v;
		}
		printf("Case #%d: %d\n",k++,min);
	}
}
