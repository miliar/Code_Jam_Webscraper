#include<cstdio>
#include<vector>

using namespace std;

int main() {
	int T;
	scanf("%d",&T);
	for(int caso=1;caso<=T;caso++) {
		int n,m;
		scanf("%d %d",&n,&m);
		char A[n][m+1];
		for(int i=0;i<n;i++)
			scanf("%s",A[i]);
		bool vale=1;
		for(int i=0;i<n-1;i++) {
			for(int j=0;j<m-1;j++) {
				if(A[i][j]=='#') {
					if(A[i][j+1]=='#' && A[i+1][j]=='#' && A[i+1][j+1]=='#') {
						A[i][j]='/';
						A[i][j+1]='\\';
						A[i+1][j]='\\';
						A[i+1][j+1]='/';
				//		puts("aqui");
					}
					else {
						vale=0;
						break;
					}
				}
			}
			if(!vale)
				break;
		}
		for(int i=0;i<n;i++)
			if(A[i][m-1]=='#')
				vale=0;
		for(int i=0;i<m;i++)
			if(A[n-1][i]=='#')
				vale=0;
		printf("Case #%d:\n",caso);

/*		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++)
				printf("%c",A[i][j]);
			printf("\n");
		}*/

		if(!vale)
			printf("Impossible\n");
		else
			for(int i=0;i<n;i++) {
				for(int j=0;j<m;j++)
					printf("%c",A[i][j]);
				printf("\n");
			}
	}
	return 0;
}
