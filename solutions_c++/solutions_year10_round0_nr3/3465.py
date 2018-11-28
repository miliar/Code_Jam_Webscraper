#include<stdio.h>
#include<stdlib.h>
#include<string.h>

__forceinline void readnum(const char *str,long long int g[],int N){
	int i=0,j=0,k=0;
	char tmp[32];
	while(str[i] != '\0'){
		if(str[i] == ' '){
			tmp[j] = '\0';
			g[k] = (long long)atol(tmp);
			j=0;k++;
		}else{
			tmp[j] = str[i];
			j++;
		}
		i++;
	}
	tmp[j] = '\0';
	g[k] = (long long)atol(tmp);
}

__forceinline void one_ride(long long int g[],long long int k, int N, long long int *earn){
	long long int remain = k;
	long long int t[64] = {0};
	int i,j;
//	for(i=0;i<N;i++) printf("%lld ",g[i]);printf("\n");

	for(i=0;i<N;i++){
		if(remain < g[i]) 
			break;
		remain -= g[i];
		*earn += g[i];
		t[i] = g[i];
	}
	if(i==N || i==0)
		return;
	for(j=0;i<N;j++,i++)
		g[j] = g[i];
	for(i=0;j<N;j++,i++)
		g[j] = t[i];

//	for(i=0;i<N;i++) printf("%lld ",g[i]);printf("\n");

}

int main(int a,char **v){
	char buffer[2048];
	int T,N,i;
	long long int R,k,*g,j,earn;
	fgets(buffer,2048,stdin);
	sscanf(buffer,"%d",&T);
	for(i=0;i<T;i++){
		earn=0;
		fgets(buffer,2048,stdin);
		sscanf(buffer,"%lld %lld %d",&R,&k,&N);
		g = (long long int *)malloc(sizeof(long long int)*N);
		fgets(buffer,2048,stdin);
		readnum(buffer,g,N);
		for(j=0;j<R;j++)
			one_ride(g,k,N,&earn);
		printf("Case #%d: %lld\n",i+1,earn);
		free(g);
	}
	return 0;
}