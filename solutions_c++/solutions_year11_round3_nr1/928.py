#include <stdio.h>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
int n,m;
int oflag;
int visit[100][100];
char tile[100][100];
void input()
{
	int i;
	fscanf(fin,"%d %d",&n,&m);
	for (i=0;i<n;i++){
		fscanf(fin,"%s",&tile[i]);
	}
}
void pro()
{
	int i,j;
	for (i=0;i<n-1;i++){
		for (j=0;j<m-1;j++){
			if (tile[i][j] == '#' && visit[i][j] == 0){
				if (tile[i+1][j] == '#' && tile[i][j+1] == '#' && tile[i+1][j+1] == '#'){
					tile[i][j]=tile[i+1][j+1] = '/';
					visit[i][j]=visit[i+1][j+1]=visit[i+1][j]=visit[i][j+1] = 1;
				}else{
					oflag = 1;
					break;
				}
			}
		}
	}
	for (i=0;i<n;i++){
		for (j=0;j<m;j++){
			if (tile[i][j] == '#' && visit[i][j] == 0){
				oflag = 1;
				break;
			}else if (tile[i][j] == '#' && visit[i][j] == 1){
				tile[i][j] = '\\';
			}
		}
		if (oflag == 1) break;
	}
}
void output()
{
	if (oflag == 1){
		fprintf(fout,"Impossible\n");
	}else{
		for (int i=0;i<n;i++){
			fprintf(fout,"%s\n",tile[i]);
		}
	}
	for (int i=0;i<n;i++){
		for (int j=0;j<m;j++){
			visit[i][j] = 0;
		}
	}

}
int main()
{
	int i,t;
	fscanf(fin,"%d",&t);
	for (i=0;i<t;i++){
		oflag=0;
		input();
		pro();
		fprintf(fout,"Case #%d:\n",i+1);
		output();
	}
	return 0;
}