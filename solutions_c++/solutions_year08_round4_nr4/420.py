#include<iostream>
#include<string>
using namespace std;
char kk[2000], temp[2000];
int str[10], visit[10];
int num , len , Min;

void Ans(){
	int i,j;
	int ans ;
	int length = strlen(kk);
	int jishu = 0 ;
	for(i = 0 ; i < length ;){
		for(j = 0 ; j < len ; j ++){
			temp[i++] = kk[ str[j] - 1 + jishu];
		}
		jishu += num ;
	}
	ans = 0 ;
	for(i = 0 ; i < length ;){
		j = i ;
		while(j+1 < length && temp[j] == temp[j+1]){
			j ++ ;
		}
		j ++ ;
		i = j ;
		ans ++ ;
	}
	if(Min == -1 || ans < Min)
		Min = ans ;
}
void dfs(){
	int i;
	if(len == num){
		Ans();
		return ;
	}
	for(i = 1 ; i <= num ; i ++){
		if(visit[i])
			continue ;
		visit[i] = 1 ;
		str[len++] = i ;
		dfs();
		visit[i] = 0 ;
		len-- ;
	}
}
int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout);
	int test;
	int Case = 0;
	scanf("%d",&test);
	while(test--){
		Case++;
		scanf("%d",&num);
		scanf("%s",kk);
		memset(visit,0,sizeof(visit));
		Min = -1 ;
		len = 0 ;
		dfs();
		printf("Case #%d: %d\n",Case,Min);
	}
	return 0;
}