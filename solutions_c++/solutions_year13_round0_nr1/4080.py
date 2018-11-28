#include<stdio.h>
int x,i,j,t,empty,st,a[4][4];
char b[4][4];

int main(){
FILE * fin, *fout;
char ans[4][25] ={"Game has not completed","X won", "O won", "Draw"};
char temp[8];
fin =fopen("c:\\input.txt","r");
fout=fopen("c:\\output","w");
fscanf(fin,"%d",&t);


for (x=1;x<=t;x++){
empty =0;

	for(i=0;i<4;i++){
		fscanf(fin,"%s",b[i]);
		//fgets(b[i],100,fin);
		for(j=0;j<4;j++){
			//fscanf(fin,"%c",&b[i][j]);
		//	printf("%c",b[i][j]);
			if (b[i][j]=='.'){
				empty=1;
				a[i][j]=0;
			} else if (b[i][j]=='X'){
			
				a[i][j]=1;
			} else if (b[i][j]=='O'){
			
				a[i][j]=2;
			} else if(b[i][j]=='T'){
			
				a[i][j]=3;
			}
		//	printf("%d",a[i][j]);
		}
		//fgets(temp,sizeof(temp),fin);
		
	//	printf("\n");
	}
//	fscanf(fin,"\n");
	//1 x 2 o
	st=0;
	for(i=0;i<4;i++){
		if(a[i][0]&a[i][1]&a[i][2]&a[i][3]){
			st=a[i][0]&a[i][1];
			break;
		}
	}
	if (!st){
		for(i=0;i<4;i++){
		if(a[0][i]&a[1][i]&a[2][i]&a[3][i]){
			st=a[0][i]&a[1][i];
			break;
		}
		}
	}
	if(!st) {
		if(a[0][0]&a[1][1]&a[2][2]&a[3][3]){
			st=a[0][0]&a[1][1];
		} else if(a[3][0]&a[2][1]&a[1][2]&a[0][3]) {
			st=a[3][0]&a[2][1];
		} else if (empty){
			st=0;
		} else 
			st=3;
	}
	
	fprintf(fout,"Case #%d: %s",x,ans[st]);
	
	fprintf(fout,"\n");
}
fclose(fin);
fclose(fout);
return 0;
}
