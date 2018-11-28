#include<stdio.h>
#define max 500
FILE *in=fopen("INPUT.TXT","r");
FILE *out=fopen("OUTPUT.TXT","w");
int r,c,d;
int res;
__int64 rs[max+5][max+5],cs[max+5][max+5],sum[max+5][max+5];
char map[max+5][max+5];
void input(){
	fscanf(in,"%d%d%d",&r,&c,&d);
	for(int i=1;i<=r;i++){
		fscanf(in,"%s",map[i]+1);
		for(int j=1;j<=c;j++){
			map[i][j]-='0';
			rs[i][j]=rs[i][j-1]+rs[i-1][j]-rs[i-1][j-1]+map[i][j]*j;
			cs[i][j]=cs[i-1][j]+cs[i][j-1]-cs[i-1][j-1]+map[i][j]*i;
			sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+map[i][j];
		}
	}
}
int row(int i,int j){
	return map[i][j]*j;
}
int col(int i,int j){
	return map[i][j]*i;
}
int rmax(int a,int b){
	if(a<b) return b;
	return a;
}
void process(){
	res=0;
	for(int i=1;i<=r;i++){
		for(int j=1;j<=c;j++){
			int sta=rmax(3,res);
			for(int k=sta;i-k>=0 && j-k>=0;k++){
				__int64 i1,i2,i3;
				i1=rs[i][j]-rs[i-k][j]-rs[i][j-k]+rs[i-k][j-k]-row(i,j)-row(i-k+1,j)-row(i,j-k+1)-row(i-k+1,j-k+1);
				i2=cs[i][j]-cs[i-k][j]-cs[i][j-k]+cs[i-k][j-k]-col(i,j)-col(i-k+1,j)-col(i,j-k+1)-col(i-k+1,j-k+1);
				i3=sum[i][j]-sum[i-k][j]-sum[i][j-k]+sum[i-k][j-k]-map[i][j]-map[i-k+1][j]-map[i][j-k+1]-map[i-k+1][j-k+1];
				if(i1*2!=i3*(j+j-k+1)) continue;
				if(i2*2!=i3*(i+i-k+1)) continue;
				res=k;
			}
		}
	}
}
void output(int tc){
	if(res==0) fprintf(out,"Case #%d: IMPOSSIBLE\n",tc);
	else fprintf(out,"Case #%d: %d\n",tc,res);
}
int main(){
	int t;
	fscanf(in,"%d",&t);
	for(int i=0;i<t;i++){
		input();
		process();
		output(i+1);
	}
	fcloseall();
	return 0;
}
