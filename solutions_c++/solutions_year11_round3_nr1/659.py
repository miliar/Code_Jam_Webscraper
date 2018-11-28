#include<stdio.h>
#include<stdlib.h>

int n,m;
char a[52][52];

void make(int t){
	printf("Case #%d:\n",t);
	scanf(" %d%d ",&n,&m);
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			scanf(" %c ",&a[i][j]);
		}
	}
	for(int i = 0; i < n - 1; i++){
		for(int j = 0; j < m - 1; j++){
			if (a[i][j] == '#'){
				if ((a[i + 1][j] == '#') && (a[i + 1][j + 1] == '#') && (a[i][j + 1] == '#')){
					a[i][j] = '/';
					a[i+1][j] = '\\';
					a[i][j+1] = '\\';
					a[i+1][j+1] = '/';
				}
				else{
					printf("Impossible\n");
					return;
				}
					
			}
		}
	}
	for(int i = 0; i < n; i++){
		if (a[i][m - 1] == '#'){
			printf("Impossible\n");
			return;
		}
	}
	for(int j = 0; j < m; j++){
		if (a[n - 1][j] == '#'){
			printf("Impossible\n");
			return;
		}
	}
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			printf("%c",a[i][j]);
		}
		printf("\n");
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int q = 0; q < t; q++){
		make(q + 1);
	}
	return 0;
}
