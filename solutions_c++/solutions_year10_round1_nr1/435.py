#include <cstdio>
#include <cstring>

char ori[51][51];
char aft[51][51];
int N,K;
int T;
bool blue,red;

void swap(char& lhs,char& rhs){
	char tmp=lhs;
	lhs=rhs;
	rhs=tmp;
}

void input(){
	scanf("%d%d",&N,&K);
	for(int i = 0;i < N;++i)
		scanf("%s",ori[i]);
	for(int i = 0;i < N;++i)
		for(int j = 0;j < N;++j)
			aft[i][j]=ori[N-1-j][i];
}

void gravity(){
	for(int i = 0;i < N;++i){
		int before = N;
		for(int j = N-1;j >= 0;--j){
			if(aft[j][i]!='.'){
				if(j != before-1)
					swap(aft[j][i],aft[before-1][i]);
				before--;
			}
		}
	}
}

bool check(char col){
	for(int i = 0;i < N;++i){
		for(int j = 0;j < N;++j){
			int k;
			if(i+K <= N){
				for(k = i;k < i+K;++k)
					if(aft[k][j] != col)
						break;
				if(k == i+K)
					return true;
			}
			if(j+K <= N){
				for(k = j;k < j+K;++k)
					if(aft[i][k] != col)
						break;
				if(k == j+K)
					return true;
			}
			if(i+K <= N && j+K <= N){
				for(k = 0;k < K;++k)
					if(aft[i+k][j+k] != col)
						break;
				if(k == K)
					return true;
			}
			if(i >= K-1 && j+K <= N){
				for(k = 0;k < K;++k)
					if(aft[i-k][j+k] != col)
						break;
				if(k == K)
					return true;
			}
		}
	}
	return false;
}

int main(){
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T;++t){
		input();
		gravity();
		blue = check('B');
		red = check('R');
		if(blue&&red)
			printf("Case #%d: Both\n",t);
		else if(blue)
			printf("Case #%d: Blue\n",t);
		else if(red)
			printf("Case #%d: Red\n",t);
		else
			printf("Case #%d: Neither\n",t);
	}
	return 0;
}
