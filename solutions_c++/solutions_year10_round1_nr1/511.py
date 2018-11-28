#include <stdio.h>

int T, K;
int N;

int main(){
	FILE *fin = fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");

	char before[100][100];
	char after[100][100];
	bool b;
	bool r;

	fscanf(fin,"%d",&T);

	for(int k=0;k<T;k++){
		fscanf(fin,"%d%d",&N,&K);
		for(int i=0;i<N;i++){
			fscanf(fin,"%s",before[i]);
		}

		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				after[i][j]=before[N-j-1][i];
			}
		}

		for(int j=0;j<N;j++){
			int cnt=N-1;
			for(int i=N-1;i>=0;i--){
				if(after[i][j]!='.'){
					if(cnt==i)
						cnt--;
					else{
						after[cnt--][j]=after[i][j];
						after[i][j]='.';
					}
				}
			}
		}

		b=false;
		r=false;
		
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				if(after[i][j]=='.')
					continue;

				bool flag1=true;
				bool flag2=true;
				bool flag3=true;
				bool flag4=true;

				for(int ind=0;ind<K;ind++){
					if(j+ind>=N || after[i][j]!=after[i][j+ind])
						flag1=false;
					if(i+ind>=N || after[i][j]!=after[i+ind][j])
						flag2=false;
					if(i+ind>=N || j+ind>=N || after[i][j]!=after[i+ind][j+ind])
						flag3=false;
					if(i+ind>=N || j-ind<0 || after[i][j]!=after[i+ind][j-ind])
						flag4=false;
				}
				
				if(flag1 || flag2 || flag3 || flag4){
					if(after[i][j]=='B')
						b=true;
					else
						r=true;
				}
			}
		}

		if(!b && !r)
			fprintf(fout,"Case #%d: Neither\n", k+1);
		else if(b && r)
			fprintf(fout,"Case #%d: Both\n",k+1);
		else if(b && !r)
			fprintf(fout,"Case #%d: Blue\n", k+1);
		else
			fprintf(fout,"Case #%d: Red\n",k+1);

	}

	fclose(fin);
	fclose(fout);

	return 0;
}
