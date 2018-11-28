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

//#include<stdio.h>
//int roundnum;
//int container;
//int groupnum;
//int groups[10];
//int solve(){
//	int first=0;
//	int last=0;
//	int result=0;
//	int eachresult=0;
//	for(int i=0;i<roundnum;++i){
//		last = first;
//		eachresult=groups[first];
//		first = (++first)%groupnum;
//		while(first!=last && eachresult+groups[first]<=container){
//			eachresult+=groups[first];
//			first = (++first)%groupnum;
//		}
//		result+=eachresult;
//	}
//	return result;
//}
//int main(){
//	int T,N,K;
//	//freopen("in.txt","r",stdin);
//	//freopen("C-small-attempt0.in","r",stdin);
//	//freopen("C-small-attempt0.out","w",stdout);
//	scanf("%d",&T);
//	for(int i=1;i<=T;++i){
//		scanf("%d%d%d",&roundnum,&container,&groupnum);
//		for(int j=0;j<groupnum;++j){
//			scanf("%d",&groups[j]);
//		}
//		printf("Case #%d: %d\n", i, solve());
//	}
//	return 0;
//}


//#include<stdio.h>
//char board[52][52];
//char rotateboard[52][52];
//int T,N,K;
//void rotate(){
//	int i,j,k;
//	for(i=N-1;i>=0;--i){
//		for(k=N-1,j=N-1;j>=0;--j){
//			if(board[i][j]!='.'){
//					rotateboard[i][k--]=board[i][j];
//			}
//		}
//		while(k>=0)
//			rotateboard[i][k--]='.';
//	}
//}
//int checkwin(int curx, int cury, int result){
//	int k;
//	bool flag=true;
//	char curchar = rotateboard[curx][cury];
//	//up
//	if(cury-K+1>=0){
//		flag=true;
//		for(k=1;k<K;++k)
//			if(curchar!=rotateboard[curx][cury-k]){
//				flag=false;
//				break;
//			}
//		if(flag){
//			if(curchar=='R')result|=1;
//			else result|=2;
//		}
//	}
//	//right
//	if(curx-K+1>=0){
//		flag=true;
//		for(k=1;k<K;++k){
//			if(curchar!=rotateboard[curx-k][cury]){
//				flag=false;
//				break;
//			}
//		}
//		if(flag){
//			if(curchar=='R')result|=1;
//			else result|=2;
//		}
//	}
//	//right up
//	if(curx-K+1>=0 && cury-K+1>=0){
//		flag=true;
//		for(k=1;k<K;++k)
//			if(curchar!=rotateboard[curx-k][cury-k]){
//				flag=false;
//				break;
//			}
//		if(flag){
//			if(curchar=='R')result|=1;
//			else result|=2;
//		}
//	}
//	//right down
//	if(curx-K+1>=0 && cury+K-1<N){
//		flag=true;
//		for(k=1;k<K;++k){
//			if(curchar!=rotateboard[curx-k][cury+k]){
//				flag=false;
//				break;
//			}
//		}
//		if(flag){
//			if(curchar=='R')result|=1;
//			else result|=2;
//		}
//	}
//	return result;
//}
//void solve(int testcase){
//	int result=0;
//	rotate();
//	int i,j,k;
//	for(i=N-1;i>=0;--i){
//		for(j=N-1;j>=0;--j){
//			if(rotateboard[i][j]=='.')
//				break;
//			result=checkwin(i,j,result);
//			if(result==3){
//				printf("Case #%d: Both\n",testcase);
//				return;
//			}
//		}
//	}
//	printf("Case #%d: ",testcase);
//	switch(result){
//	case 0:
//		printf("Neither");
//		break;
//	case 1:
//		printf("Red");
//		break;
//	case 2:
//		printf("Blue");
//		break;
//	}
//	printf("\n");
//}
//int main(){
//	int i,j;
//	freopen("A-small-practice.in","r",stdin);
//	//freopen("C-small-attempt0.in","r",stdin);
//	freopen("A-small-practice.out","w",stdout);
//	scanf("%d",&T);
//	for(i=1;i<=T;++i){
//		scanf("%d%d",&N,&K);
//		for(j=0;j<N;++j)
//			scanf("%s",&board[j]);
//		solve(i);
//	}
//	return 0;


#include<stdio.h>
int sx[2],sy[2];
int main(){
	int i,j,T,N;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;++i){
		scanf("%d",&N);
		for(j=0;j<N;++j)
			scanf("%d%d",&sx[j],&sy[j]);
		printf("Case #%d: ",i);
		if(N==1)
			printf("0\n");
		if(N==2){
			if(sx[0]<sx[1]&&sy[0]<sy[1] || (sx[0]>sx[1] && sy[0]>sy[1]))
				printf("0\n");
			else
				printf("1\n");
		}
	}
	return 0;
}