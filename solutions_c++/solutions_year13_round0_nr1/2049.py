#include<cstdio>
using namespace std;
long long T[4][4]={{2,3,5,7},{11,13,17,19},{23,29,31,37},{41,43,47,53}};
unsigned long long Xval, Oval;
inline bool win(unsigned long long val){
	if(val%20746==0 || val%48633==0 || val%123845==0 ||
		val%260813==0 || val%42718==0 || val%4391633==0 ||
		val%765049==0 || val%46189==0 || val%210==0 || val%141491==0)
			return true;
	return false;
}
int main(){
	int z;
	scanf("%d\n", &z);
	for(int k=1; k<=z; k++){
		char x;
		bool dot = false; 
		Xval=Oval=1;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				scanf("%c", &x);
				if(x=='O')Oval*=T[i][j];
				else if(x=='X')Xval*=T[i][j];
				else if(x=='T')Xval*=T[i][j],Oval*=T[i][j];
				else dot=true;
			}
			scanf("\n");
		}
		bool Xwon=win(Xval);
		bool Owon=win(Oval);
		printf("Case #%d: ",k);
		if(Xwon)printf("X won\n");
		else if(Owon)printf("O won\n");
		else if(!dot)printf("Draw\n");
		else printf("Game has not completed\n");
	}	
	
	return 0;
}
