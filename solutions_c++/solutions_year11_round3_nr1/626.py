#include<stdio.h>
#define max 50
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");
int n,m;
int pos;
char map[max+5][max+5];
void input(){
	fscanf(in,"%d%d",&n,&m);
	for(int i=0;i<n;i++){
		fscanf(in,"%s",map[i]);
	}
}
int blue(char a[][max+5],int n,int m,int i,int j){
	if(i>=0 && i<n){
		if(j>=0 && j<m){
			if(a[i][j]=='#') return 1;
		}
	}
	return 0;
}
void process(){
	pos=1;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(map[i][j]=='#'){
				if(blue(map,n,m,i,j) && blue(map,n,m,i,j+1) && blue(map,n,m,i+1,j) && blue(map,n,m,i+1,j+1)){
					map[i][j]='/';
					map[i][j+1]='\\';
					map[i+1][j]='\\';
					map[i+1][j+1]='/';
				}
				else{
					pos=0;
					return;
				}
			}
		}
	}
}
void output(int tc){
	fprintf(out,"Case #%d:\n",tc);
	if(pos==0) fprintf(out,"Impossible\n");
	else{
		for(int i=0;i<n;i++){
			fprintf(out,"%s\n",map[i]);
		}
	}
}
int main(){
	int t;
	fscanf(in,"%d",&t);
	for(int i=0;i<t;i++){
		input();
		process();
		output(i+1);
	}
	fclose(in);
	fclose(out);
	return 0;
}
