#include <cstdio>
#include <cstring>

int T;
char b[5][5];

bool check (char c){
	bool f;
	for (int i=0;i<4;++i){
		f=1;
		for (int j=0;j<4;++j)
			f=f&&((b[i][j]==c)||(b[i][j]=='T'));
		if (f){
			return f;
		}
	}
	for (int i=0;i<4;++i){
		f=1;
		for (int j=0;j<4;++j)
			f=f&&((b[j][i]==c)||(b[j][i]=='T'));
		if (f){
			return f;
		}
	}
	f=1;
	for (int j=0;j<4;++j)
		f=f&&((b[j][j]==c)||(b[j][j]=='T'));
	if (f){
		return f;
	}
    f=1;
	for (int j=0;j<4;++j)
		f=f&&((b[3-j][j]==c)||(b[3-j][j]=='T'));
	if (f){
		return f;
	}
	return 0;
}

int main(){
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		for (int i=0;i<4;++i)
			scanf(" %s",b[i]);
		printf("Case #%d: ",t);
		if (check('O')){
			printf("O won");
		}
		else if (check('X')){
			printf("X won");
		}
		else {
			bool v=0;
			for (int i=0;i<4;++i)
				for (int j=0;j<4;++j)
					if (b[i][j] == '.') v=1;
			if (v)
				printf("Game has not completed");
			else printf("Draw");
		}
		printf("\n");
//		scanf(" %s",b[4]);
	}
}
