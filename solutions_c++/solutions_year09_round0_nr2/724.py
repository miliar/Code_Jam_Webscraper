#include <stdio.h>
#include <string.h>

const int size=200;
const int dx[]={-1,0,0,+1};
const int dy[]={0,-1,+1,0};

int a[size][size],W,H;
char s[size][size],ch;

int in_range(int i,int n){
	return 0<=i&&i<n;
}

char work(int i,int j){
	if(s[i][j]!=0) return s[i][j];
	int p,v=a[i][j];
	for(int k=0; k<4; k++){
		int x=i+dx[k];
		int y=j+dy[k];
		if(!in_range(x,H)) continue;
		if(!in_range(y,W)) continue;
		if(a[x][y]<v){
			v=a[x][y];
			p=k;
		}
	}
	if(v==a[i][j]){
		s[i][j]=ch;
		ch++;
	}else{
		s[i][j]=work(i+dx[p],j+dy[p]);
	}
	return s[i][j];
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cs=1; cs<=T; cs++){
		scanf("%d%d",&H,&W);
		for(int i=0; i<H; i++)
			for(int j=0; j<W; j++)
				scanf("%d",&a[i][j]);
		memset(s,0,sizeof(s));
		ch='a';
		printf("Case #%d:\n",cs);
		for(int i=0; i<H; i++)
			for(int j=0; j<W; j++)
				printf("%c%c",work(i,j),j+1<W?' ':'\n');
	}
	return 0;
}
