//#include<stdio.h>
//A. Snapper Chain 
//bool solve(int N, int K){
//	int i=0;
//	while(K>0){
//		if(K%2==1){
//			K/=2;
//			++i;
//		}else
//			return false;
//		if(i==N)
//			return true;
//	}
//	return false;
//}
//int main(){
//	int T,N,K;
//	//freopen("A-large.in","r",stdin);
//	//freopen("A-large.out","w",stdout);
//	scanf("%d",&T);
//	for(int i=1;i<=T;++i){
//		scanf("%d%d",&N,&K);
//		printf("Case #%d: ",i);
//		if(solve(N,K))
//			printf("ON\n");
//		else
//			printf("OFF\n");
//	}
//	return 0;
//}

#include<stdio.h>
int roundnum;
int container;
int groupnum;
int groups[10];
int solve(){
	int first=0;
	int last=0;
	int result=0;
	int eachresult=0;
	for(int i=0;i<roundnum;++i){
		last = first;
		eachresult=groups[first];
		first = (++first)%groupnum;
		while(first!=last && eachresult+groups[first]<=container){
			eachresult+=groups[first];
			first = (++first)%groupnum;
		}
		result+=eachresult;
	}
	return result;
}
int main(){
	int T,N,K;
	//freopen("in.txt","r",stdin);
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;++i){
		scanf("%d%d%d",&roundnum,&container,&groupnum);
		for(int j=0;j<groupnum;++j){
			scanf("%d",&groups[j]);
		}
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}