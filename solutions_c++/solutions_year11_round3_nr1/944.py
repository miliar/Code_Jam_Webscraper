#include<cstdio>

using namespace std;

int main(){
	int T, R, C, k=1;
	char M[100][100];
	scanf("%d\n",&T);
	while(T--){
		scanf("%d%d\n",&R,&C);
		for(int i=0;i<R;i++)
			scanf("%s\n",M[i]);
		
		
		for(int i=0;i<R-1;i++)
			for(int j=0;j<C-1;j++){
				if(M[i][j]=='#' && M[i][j+1]=='#'
				&& M[i+1][j]=='#' && M[i+1][j+1]=='#'){
					M[i][j]='/';
					M[i][j+1]='\\';
					M[i+1][j]='\\';
					M[i+1][j+1]='/';
				}
			}
		int ok=1;
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++){
				if(M[i][j]=='#'){
					ok=0;
					goto fim;
				}
			}
		fim:
		
		printf("Case #%d:\n",k);
		if(ok){
			for(int i=0;i<R;i++){
				printf("%s\n",M[i]);
			}
		}else{
			printf("Impossible\n");
		}
		
		k++;
	}
	return 0;
}