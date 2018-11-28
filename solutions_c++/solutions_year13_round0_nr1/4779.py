#include<cstdio>
#define N 4
char b[N][N+1];

bool won(char v){
	bool p,q;
	for(int i=0;i<N;++i){
		p=q=1;
		for(int j=0;j<N;++j){
			p&=b[i][j]=='T'||b[i][j]==v;
			q&=b[j][i]=='T'||b[j][i]==v;
		}
		if(p||q) return 1;
	}
	p=q=1;
	for(int i=0;i<N;++i){
		p&=b[i][i]=='T'||b[i][i]==v;
		q&=b[i][N-1-i]=='T'||b[i][N-1-i]==v;
	}
	if(p||q) return 1;
	return 0;
}

bool full(){
	for(int i=0;i<N;++i)
		for(int j=0;j<N;++j)
			if(b[i][j]=='.')
				return 0;
	return 1;
}
int main(){
	int t;scanf("%d",&t); int caso=1;
	while(t--){
		for(int i=0;i<N;++i)
			scanf("%s",b[i]);

		printf("Case #%d: ",caso++);

		if( won('X') )
			printf("X won\n");
		else if( won('O') )
			printf("O won\n");
		else if( full() )
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}
