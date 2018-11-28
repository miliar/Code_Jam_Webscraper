#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int FLAG=0;
int map[5][5];

void init(){
	FLAG=0;
	for(int i=1;i<=4;i++) for(int j=1;j<=4;j++){
		char ch; scanf(" %c",&ch);
		if(ch=='X') map[i][j]=1;
		if(ch=='O') map[i][j]=2;
		if(ch=='T') map[i][j]=3;
		if(ch=='.') map[i][j]=0,FLAG++;
	}
}

int work(){
	for(int i=1;i<=4;i++){
		int j;
		for(j=1;j<=4;j++) if(map[i][j]!=1 && map[i][j]!=3) break;
		if(j==5) return 1;
	}
	for(int j=1;j<=4;j++){
		int i;
		for(i=1;i<=4;i++) if(map[i][j]!=1 && map[i][j]!=3) break;
		if(i==5) return 1;
	}
	for(int i=1;i<=1;i++){
		int j;
		for(j=1;j<=4;j++) if(map[j][j]!=1 && map[j][j]!=3) break;
		if(j==5) return 1;
	}
	for(int i=1;i<=1;i++){
		int j;
		for(j=1;j<=4;j++) if(map[j][5-j]!=1 && map[j][5-j]!=3) break;
		if(j==5) return 1;
	}
	for(int i=1;i<=4;i++){
		int j;
		for(j=1;j<=4;j++) if(map[i][j]!=2 && map[i][j]!=3) break;
		if(j==5) return 2;
	}
	for(int j=1;j<=4;j++){
		int i;
		for(i=1;i<=4;i++) if(map[i][j]!=2 && map[i][j]!=3) break;
		if(i==5) return 2;
	}
	for(int i=1;i<=1;i++){
		int j;
		for(j=1;j<=4;j++) if(map[j][j]!=2 && map[j][j]!=3) break;
		if(j==5) return 2;
	}
	for(int i=1;i<=1;i++){
		int j;
		for(j=1;j<=4;j++) if(map[j][5-j]!=2 && map[j][5-j]!=3) break;
		if(j==5) return 2;
	}
	if(FLAG==0) return 0;
	return -1;
}

int main(){
	int T,T2=0; scanf("%d",&T);
	while(T--){
		printf("Case #%d: ",++T2);
		init();
		int tmp=work();
		if(tmp==-1) printf("Game has not completed\n");
		if(tmp==1) printf("X won\n");
		if(tmp==2) printf("O won\n");
		if(tmp==0) printf("Draw\n");
	}
	return 0;
}