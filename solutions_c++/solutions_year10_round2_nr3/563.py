#include<cstdio>


//inline bool isset(int state, int idx){
//	return (state&(1<<idx))!=0;
//}
#define isset(state,idx) ((state&(1<<idx))!=0)

int arr[30];
int sz;

inline int find(int num){
	int ret=-1;
	for(int i=0;i<sz && ret==-1;i++){
		if (num==arr[i]){
			ret=i+1;
		}
	}
	return ret;
}

inline bool isvalid(int state, int N){
	sz=0;
	for(int i=0;i<N-2;i++){
		if (isset(state,i)){
			arr[sz++]=i+2;
		}
	}
	arr[sz++]=N;
	int ind=N;
	while(ind!=-1 && ind!=1){
		ind=find(ind);
	}
	return (ind==1);
}

int solve(int N){
	int ret=0;
	for(int state=0;state<(1<<(N-2));state++){
		if (isvalid(state,N)) ret++;
	}
	return ret;
}

int MOD=100003;
int main(){
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++){
		int N;
		scanf("%d", &N);
		printf("Case #%d: %d\n",cas,solve(N)%MOD);
	}
}
