#include <stdio.h>
const int SIZE = 60;
char mat[SIZE][SIZE];
int N,K;
char strans[][50]={"Neither","Both","Red","Blue"};
void init();
int work();
enum {Neither,Both,Red,Blue};
int check(int,int);
void show();
const int WAY = 4;
int deta[WAY][2]={{1,0},{0,1},{1,-1},{1,1}};
int main(){
	freopen("dat.in","r",stdin);
	freopen("dat.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for (int i=0;i<cas;i++){
		init();
		int ans = work();
		printf("Case #%d: %s\n",i+1,strans[ans]);
	}
}

void init(){
	scanf("%d%d",&N,&K);
	
	for (int i=0;i<N;i++){
		scanf("%s",mat[i]);
	}
	for (int i=0;i<N;i++){
		int last = N-1;
		for (int j=N-1;j>=0;j--){
			if ('.'!=mat[i][j]){
				mat[i][last--]=mat[i][j];
			}
		}
		for (int j=last;j>=0;j--){
			mat[i][j]='.';
		}
	}
//	show();
}
int check(int row,int col){
	char aim = mat[row][col];
	for (int i=0;i<WAY;i++){
		int x=row;
		int y=col;
		bool isok=true;
		int j;
		for (j=0;j<K-1;j++){
			int tx = x+deta[i][0];
			int ty = y+deta[i][1];
            x=tx;
            y=ty;
			if (tx>=0 && tx<N && ty>=0 &&ty<N){
				if (aim!=mat[tx][ty]){
					isok=false;
					break;
				}
			}else{
				isok=false;
				break;
			}
		}
		if (isok && (K-1)==j){
		
			return ('R'==aim?Red:Blue);
		}
	}
	return Neither;
}
int work(){
	bool redwin=false;
	bool bluewin=false;
	for (int i=0;i<N;i++){
		for (int j=0;j<N;j++){
			if (redwin && bluewin){
				break;
			}
			if ('.'!=mat[i][j]){
				int ret=Neither;
				if (redwin==false && 'R'==mat[i][j]){
					ret = check(i,j);
				}else if (bluewin==false && 'B'==mat[i][j]){
					ret = check(i,j);
				}
				
				if (Red==ret){
					
					redwin=true;
				}else if (Blue==ret){
					bluewin=true;
				}
			}
		}
	}
	
	if (redwin==false && bluewin==false){
		return Neither;
	}else if (redwin&&bluewin){
		return Both;
	}else if (redwin){
		return Red;
	}else{
		return Blue;
	}
}
void show(){
	for (int i=0;i<N;i++){
		printf("%s\n",mat[i]);
	}
}
