#include<stdio.h>
using namespace std;
char g[4][4],s;
inline bool checkx(){
	int tmp=0;
	for(int i=0;i<4;i++){
		tmp=0;
		for(int j=0;j<4;j++)
			if(g[i][j]=='X' || g[i][j]=='T') tmp++;
		if(tmp==4) return true;
	}
	for(int i=0;i<4;i++){
		tmp=0;
		for(int j=0;j<4;j++)
			if(g[j][i]=='X' || g[j][i]=='T') tmp++;
		if(tmp==4) return true;
	}
	tmp=0;
	for(int i=0;i<4;i++)
		if(g[i][i]=='X' || g[i][i]=='T')
			tmp++;
	if(tmp==4) return true;
	tmp=0;
	for(int i=0;i<4;i++)
		if(g[3-i][i]=='X' || g[3-i][i]=='T')
			tmp++;
	if(tmp==4) return true;
	return false;
}
inline bool checky(){
	int tmp=0;
	for(int i=0;i<4;i++){
		tmp=0;
		for(int j=0;j<4;j++)
			if(g[i][j]=='O' || g[i][j]=='T') tmp++;
		if(tmp==4) return true;
	}
	for(int i=0;i<4;i++){
		tmp=0;
		for(int j=0;j<4;j++)
			if(g[j][i]=='O' || g[j][i]=='T') tmp++;
		if(tmp==4) return true;
	}
	tmp=0;
	for(int i=0;i<4;i++)
		if(g[i][i]=='O' || g[i][i]=='T')
			tmp++;
	if(tmp==4) return true;
	tmp=0;
	for(int i=0;i<4;i++)
		if(g[3-i][i]=='O' || g[3-i][i]=='T')
			tmp++;
	if(tmp==4) return true;
	return false;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int n;
	scanf("%d",&n);
	for(int p=1;p<=n;p++){
		for(int i=0;i<4;i++)
			scanf("%s",g[i]);
		getchar();
		printf("Case #%d: ",p);
		if(checkx()){
			puts("X won");continue;}
		if(checky()){
			puts("O won");continue;}
		int c=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(g[i][j]!='.') c++;
		if(c!=16)
			puts("Game has not completed");
		else
			puts("Draw");
	}
	scanf("%d",&n);
}
