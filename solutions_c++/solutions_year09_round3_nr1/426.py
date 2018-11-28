#include<cstdio>
#include<cstring>
#define MAX 100
int map[128];

int doMap(char num[MAX]){
	int i,j=2,k=1;
	for(i=0;i<128;i++){
		map[i]=-1;
	}
	map[num[0]]=1;
	//printf("%c = %d\n",num[0],1);
	int size = strlen(num);
	if(size == 1) return k;
	for(i=1;num[i]==num[0];i++);
	map[num[i]]=0;
	//printf("%c = %d\n",num[i],0);
	for(;num[i]!='\0';i++){
		if(map[num[i]]<0){
		//	printf("%c = %d\n",num[i],j);
			map[num[i]]=j++;
		}
	}
	//printf("base %d\n",j);
	return j;
}

long long int convert(char num[MAX], int base){
	int i;
	long long int j=0,k=1;
	for(i=strlen(num)-1;i>=0;i--){
		j+=map[num[i]]*k;
		k*=base;
	}
	return j;
}

int main(){
	char num[MAX];
	int cases,i,j,k=1;
	int min;
	scanf("%d\n",&cases);
	
	while(cases--){
		scanf("%s\n",num);
		min = doMap(num);
		printf("Case #%d: %lld\n",k++,convert(num,min));
	}
	
}