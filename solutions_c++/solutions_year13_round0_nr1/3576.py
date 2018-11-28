#include<stdio.h>
char c[5][5];
int print[1003];
int chk2(int x){
	if(x==0) return 0;
	if(x%2==0 && x%3!=0) return 1;
	if(x%2!=0 && x%3==0) return -1;
	return 0;
}
int chk(int x,int y){
	if(c[x][y]=='.')
		return 0;
	else if(c[x][y]=='O')
		return 2;
	else if(c[x][y]=='X')
		return 3;
	else if(c[x][y]=='T')
		return 1;
}
int main()
{
	FILE *in,*out;
	int i,j,t,k[4],k2[4],l,draw;
	in=fopen("A-large.in","r");
	out = fopen("A-large.out","w");

	fscanf(in,"%d",&t);
	for(l=0;l<t;l++){
		draw=1;
		for(i=0;i<4;i++)
			fscanf(in,"%s",c[i]);
		for(i=0,k[0]=1,k[1]=1;i<4;i++) k[0]*=chk(i,i),k[1]*=chk(3-i,i);
		if(chk2(k[0])!=0) {print[l]=chk2(k[0]); continue; }
		if(chk2(k[1])!=0) {print[l]=chk2(k[1]); continue; }
		for(i=0;i<4;i++)
			k[i]=k2[i]=1;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				k[i]*=chk(i,j);
				k2[j]*=chk(i,j);
				if(c[i][j]=='.') draw=0;
			}
		}
		for(i=0;i<4;i++){
			if(chk2(k[i])!=0) {print[l]=chk2(k[i]); break;}
			if(chk2(k2[i])!=0) {print[l]=chk2(k2[i]); break;}
		}
		if(print[l]==0 && draw==1) print[l]=2;
	}
	for(i=0;i<t;i++){
		fprintf(out,"Case #%d: ",i+1);
		if(print[i]==0) fprintf(out,"Game has not completed\n");
		if(print[i]==1) fprintf(out,"O won\n");
		if(print[i]==-1) fprintf(out,"X won\n");
		if(print[i]==2) fprintf(out,"Draw\n");
	}
	return 0;
}