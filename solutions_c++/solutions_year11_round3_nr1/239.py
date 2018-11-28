#include<stdio.h>

int n,m;
char map[51][51];

int main(void){
	int T;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");

	fscanf(fin,"%d\n",&T);
	for(int t=1;t<=T;t++){
		int i,j;
		bool flag = true;
		fprintf(fout,"Case #%d:\n", t);
		fscanf(fin,"%d %d\n",&n,&m);
		for(i=0;i<n;i++){
			fscanf(fin,"%s",map[i]);
		}

		for(i=0;i<n-1;i++){
			for(j=0;j<m-1;j++){
				if(map[i][j] == '#' && map[i+1][j] == '#' && map[i][j+1] == '#' && map[i+1][j+1] == '#'){
					map[i][j] = '/';
					map[i+1][j] = '\\';
					map[i][j+1] = '\\';
					map[i+1][j+1] = '/';
				} else if(map[i][j] == '#'){
					flag = false;
				}
			}
		}
		for(i=0;i<m;i++){
			if(map[n-1][i] == '#') flag = false;
		}
		for(i=0;i<n;i++){
			if(map[i][m-1] == '#') flag == false;
		}
		if(flag == false) fprintf(fout,"Impossible\n");
		else{
			for(i=0;i<n;i++){
				for(j=0;j<m;j++){
					fprintf(fout,"%c",map[i][j]);
				}
				fprintf(fout,"\n");
			}
		}
	}
	
	fcloseall();
}