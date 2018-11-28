#include <cstdio>

char str[100][100];

void newprob(){
	int r,c;
	scanf("%d %d",&r,&c);
	for(int i=0;i<r;i++){
		scanf("%s",str[i]);
	}
	for(int i=0;i<r-1;i++){
		for(int j=0;j<c-1;j++){
			if(str[i][j] == '#' && str[i][j+1] == '#'
			&& str[i+1][j] == '#' && str[i+1][j+1] == '#'){
				str[i][j] = '/';
				str[i][j+1] = '\\';
				str[i+1][j] = '\\';
				str[i+1][j+1] = '/';
			}
		}
	}
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(str[i][j] == '#'){
				printf("Impossible\n");
				return;
			}
		}
	}
	for(int i=0;i<r;i++)printf("%s\n",str[i]);
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		printf("Case #%d:\n",i);
		newprob();
	}
	return 0;
}
