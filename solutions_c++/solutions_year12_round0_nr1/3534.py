#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	char a[26][2];
	a[0][0]='a';
	a[0][1]='y';
	a[1][0]='b';
	a[1][1]='h';
	a[2][0]='c';
	a[2][1]='e';
	a[3][0]='d';
	a[3][1]='s';
	a[4][0]='e';
	a[4][1]='o';
	a[5][0]='f';
	a[5][1]='c';
	a[6][0]='g';
	a[6][1]='v';
	a[7][0]='h';
	a[7][1]='x';
	a[8][0]='i';
	a[8][1]='d';
	a[9][0]='j';
	a[9][1]='u';
	a[10][0]='k';
	a[10][1]='i';
	a[11][0]='l';
	a[11][1]='g';
	a[12][0]='m';
	a[12][1]='l';
	a[13][0]='n';
	a[13][1]='b';
	a[14][0]='o';
	a[14][1]='k';
	a[15][0]='p';
	a[15][1]='r';
	a[16][0]='q';
	a[16][1]='z';
	a[17][0]='r';
	a[17][1]='t';
	a[18][0]='s';
	a[18][1]='n';
	a[19][0]='t';
	a[19][1]='w';
	a[20][0]='u';
	a[20][1]='j';
	a[21][0]='v';
	a[21][1]='p';
	a[22][0]='w';
	a[22][1]='f';
	a[23][0]='x';
	a[23][1]='m';
	a[24][0]='y';
	a[24][1]='a';
	a[25][0]='z';
	a[25][1]='q';
	int t,i,j,u,v;
	char c;
	FILE *fp1,*fp2;
	fp1=fopen("A-small-attempt0.in","r");
	fp2=fopen("trying1.txt","w");
	fscanf(fp1,"%d",&t);
	fscanf(fp1,"%c",&c);
	char x[101];
	for(i=1;i<=t;i++){
		v=0;
		while(1){
			fscanf(fp1,"%c",&c);
			if(c=='\n')
				break;
			else{
				x[v]=c;
				v++;
			}
		}
		x[v]='\0';	
		for(j=0;x[j]!='\0';j++){
			if(x[j]==' ')
				continue;
			for(u=0;u<26;u++){
				if(a[u][0]==x[j])
					break;
			}
			x[j]=a[u][1];
		}
		fprintf(fp2,"Case #%d: %s\n",i,x);
	}	
	fclose(fp1);
	fclose(fp2);
	return(0);
}
