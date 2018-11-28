#include <stdio.h>
#include <malloc.h>

#define N 100

int T,H,W;
int altitudes[N][N];
char basins[N][N];
bool instack[N][N];
char c = 'a';


typedef struct stack{
	int *base;
	int *top;
	int stacksize;
}*Sqstack;

bool InitStack(Sqstack s){
	s->base = (int *)malloc(H*W*sizeof(int *));
	if(!s->base){
		return false;
	}
	s->top=s->base;
	s->stacksize = H*W;
	return true;
}

int GetTop(Sqstack s){
	if(s->top==s->base)
		return NULL;
	return *(s->top-1);
}

void Push(Sqstack s,int e){
	*(s->top++)=e;
	instack[e/W][e%W]=true;
}

int Pop(Sqstack s){
	if(s->top == s->base)
		return -1;
	return *(--s->top);
}

Sqstack S;

bool Isbasins(int i,int j){
	if(i>0&&altitudes[i-1][j]<altitudes[i][j]){
		return false;
	}
	if(j>0&&altitudes[i][j-1]<altitudes[i][j]){
		return false;
	}
	if(j<W-1&&altitudes[i][j+1]<altitudes[i][j]){
		return false;
	}
	if(i<H-1&&altitudes[i+1][j]<altitudes[i][j]){
		return false;
	}
	return true;
}

int trans(int m,int t){
	int i=m/W;
	int j=m%W;
	if(t==0){
		if(i>0){
			return (i-1)*W+j;
		} else {
			return -1;
		}
	} else if(t==1){
		if(j>0){
			return i*W+j-1;
		} else {
			return -1;
		}
	} else if(t==2){
		if(j<W-1){
			return i*W+j+1;
		} else {
			return -1;
		}
	} else if(t==3){
		if(i<H-1){
			return (i+1)*W+j;
		} else {
			return -1;
		}
	}
}

bool Goto(int m,int n){
	int minPos = -1;
	int min = -1;
	for(int t=0;t<4;t++){
		int tran = trans(m,t);
		if(tran>=0&&altitudes[tran/W][tran%W]<altitudes[m/W][m%W]){
			if(min == -1||altitudes[tran/W][tran%W]<min){
				minPos = tran;
				min = altitudes[tran/W][tran%W];
			}
		}
	}
	if(minPos == n){
		return true;
	} else {
		return false;
	}
}

int main(){
//	if(freopen("B-large.in", "r", stdin)!=NULL){
//		freopen("B-large.out", "w", stdout);
//	}
	scanf("%d",&T);
	int i;
	int j,k;
	for(i=0;i<T;i++){
		c = 'a';
		scanf("%d%d",&H,&W);
		S = (Sqstack)malloc(sizeof(Sqstack));
		InitStack(S);
		for(j=0;j<H;j++){
			for(k=0;k<W;k++){
				scanf("%d",&altitudes[j][k]);
				basins[j][k] = 0;
				instack[j][k] = false;
			}
		}
		for(j=0;j<H;j++){
			for(k=0;k<W;k++){
				if(!instack[j][k]){
					basins[j][k] = c;
					c++;
					Push(S,j*W+k);
					int e=Pop(S);
					while(e!=-1){
						int min = -1;
						int minPos = -1;
						for(int t=0;t<4;t++){
							int tran = trans(e,t);
							if(tran>=0&&altitudes[tran/W][tran%W]<altitudes[e/W][e%W]){
								if(min == -1||altitudes[tran/W][tran%W]<min){
									minPos = tran;
									min = altitudes[tran/W][tran%W];
								}
							} else if(tran>=0&&altitudes[tran/W][tran%W]>altitudes[e/W][e%W]){
								if(Goto(tran,e)&&!instack[tran/W][tran%W]){
									basins[tran/W][tran%W]=basins[e/W][e%W];
									Push(S,tran);
								}
							}
						}
						if(minPos!=-1&&!instack[minPos/W][minPos%W]){
							basins[minPos/W][minPos%W]=basins[e/W][e%W];
							Push(S,minPos);
						}
						e=Pop(S);
					}
				}
			}
		}
		printf("Case #%d:\n",i+1);
		for(j=0;j<H;j++){
			for(k=0;k<W;k++){
				printf("%c",basins[j][k]);
				if(k<W-1){
					printf(" ");
				}
			}
			printf("\n");
		}
	}
	return 0;
}