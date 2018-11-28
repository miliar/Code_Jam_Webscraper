#include <stdio.h>

char b[60][60];

int main(){
	int T;
	scanf("%d", &T);
	for(int TT=1;TT<=T;TT++){
		int r,c;
		scanf("%d%d", &r,&c);
		for(int i=0;i<r;i++){
			scanf("%s", b[i]);
		}
		bool ok=true;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(b[i][j] == '#'){
					if(j < c && i < r){
						b[i][j] = '/';
						if(b[i][j+1] == '#'){
							b[i][j+1] = '\\';
						}else{
							ok=false;
						}
						if(b[i+1][j] == '#'){
							b[i+1][j] = '\\';
						}else{
							ok=false;
						}
						if(b[i+1][j+1] == '#'){
							b[i+1][j+1] = '/';
						}else{
							ok=false;
						}
					}else{
						ok=false;
					}
				}
			}
		}
		printf("Case #%d:\n", TT);
		if(ok){
			for(int i=0;i<r;i++){
				printf("%s\n", b[i]);
			}
		}else{
			printf("Impossible\n");
		}
	}
}