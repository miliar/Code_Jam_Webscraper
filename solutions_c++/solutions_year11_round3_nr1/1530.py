#include<iostream>

using namespace std;


int rep( int row, int col, char mat[100][100]){
	if(mat[row][col] == '#' && mat[row][col+1] == '#' && mat[row+1][col] == '#' && mat[row+1][col+1] == '#'){
		mat[row][col] = '/';
		mat[row][col+1] = '\\';
		mat[row+1][col] = '\\';
		mat[row+1][col+1] = '/';
		return 1;
	}
	return 0;
}

int main(){

	int numbers[5000];
  char mat[100][100];
	int T, rs,cs;
	int t, i, j;
	scanf("%d", &T);
	char ch;

	for(t=0;t<T; t++)
	{
		int flag = 1;
    cin>>rs;
    cin>>cs;
		for(i=0;i<rs;i++){
			for(j=0;j<cs;j++){
        cin>>mat[i][j];
			}
		}

		for(i=0;i<rs-1;i++){
                        for(j=0;j<cs-1;j++){
                                if(mat[i][j] == '#') {
					if(rep(i,j, mat) == 0){
						flag = 0;
						break;
					}
				}
                        }
			if(flag ==0)break;
                }
		for(i=0;i<rs;i++){
                        for(j=0;j<cs;j++){
				if(mat[i][j] == '#')
					flag = 0;
			}
		}
		
		printf("Case #%d:\n", t+1);
		if(flag ==1) {	
			for(i=0;i<rs;i++){
				for(j=0;j<cs;j++){
					printf("%c",mat[i][j]);
				}
				printf("\n");
			}
		}else {
			 printf("Impossible\n");
		}
		
	}

	return 0;
}

