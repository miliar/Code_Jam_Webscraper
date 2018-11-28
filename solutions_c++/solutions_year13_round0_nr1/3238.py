#include <cstdio>
char board[4][4];
int m[4];
int judge(int b){
	if((b&0x55)==0x55)
		return 1;
	if((b&0xAA)==0xAA)
		return 2;
	return 0;
}
int main(){
	int T;
	scanf("%d",&T);
	m['X']=1;
	m['O']=2;
	m['T']=3;
	m['.']=0;
	for(int t=1;t<=T;++t){
		int res=0,full=3;
		for(int i=0;i<4;++i)
			scanf("%s",board[i]);
		int r=0,c=0;
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				r = (r<<2) | m[board[i][j]];
				c = (c<<2) | m[board[j][i]];
				if(board[i][j]=='.')full=0;
			}
			if(res=judge(r)) goto result;
			if(res=judge(c)) goto result;
		}
		r =  (m[board[0][0]]<<6) | (m[board[1][1]]<<4) |(m[board[2][2]]<<2) |(m[board[3][3]]);
		c =  (m[board[0][3]]<<6) | (m[board[1][2]]<<4) |(m[board[2][1]]<<2) |(m[board[3][0]]);
		if(res=judge(r)) goto result;
		if(res=judge(c)) goto result;
result:
		if(!res)
			res=full;
		printf("Case #%d: ",t);
		switch(res){
		case 0: printf("Game has not completed\n");break;
		case 1: printf("X won\n");break;
		case 2: printf("O won\n");break;
		case 3: printf("Draw\n");break;
		default:break;
		}
	}
	return 0;
}