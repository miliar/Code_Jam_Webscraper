#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

char mat[55][55];

int main(){
	int T;
	int cas=1;
	freopen("A-large.in","r",stdin);
	freopen("A2.txt","w",stdout);

	scanf("%d",&T);
	while(T--){
		int r,c;
		int i,j;
		scanf("%d %d",&r,&c);
		getchar();
		for(i=0;i<r;++i){
			gets(mat[i]);
		}

		bool flag=0;

		for(i=0;i<r;++i){
			if(flag)
				break;
			for(j=0;j<c;++j){
				if(flag)
					break;
				if(mat[i][j]=='#'){
					mat[i][j]='/';
					if(mat[i][j+1]=='#'){
						mat[i][j+1]='\\';
					}
					else{
						flag=1;
					}
					if(mat[i+1][j]=='#'){
						mat[i+1][j]='\\';
					}
					else{
						flag=1;
					}
					if(mat[i+1][j+1]=='#'){
						mat[i+1][j+1]='/';
					}
					else{
						flag=1;
					}
				}
			}
		}
		printf("Case #%d:\n",cas++);
		if(flag){
			printf("Impossible\n");
		}
		else{
			for(i=0;i<r;++i)
				puts(mat[i]);
		}
	}
	return 0;
}