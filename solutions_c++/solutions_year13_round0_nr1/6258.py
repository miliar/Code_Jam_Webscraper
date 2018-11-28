#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main(){
	int t;
	char d[5][5];
	FILE *f1=fopen("A-large.in","r");
	FILE *f2=fopen("A-large.out","w");
	fscanf(f1,"%d",&t);
	for(int i=0;i<t;i++){
		for(int j=0;j<4;j++)	fscanf(f1,"%s",d[j]);
		int x=0,o=0,cnt=0,flag=3;
		if((d[0][0]=='X' || d[0][0]=='T') && (d[1][1]=='X' || d[1][1]=='T') && (d[2][2]=='X' || d[2][2]=='T') && (d[3][3]=='X' || d[3][3]=='T'))
			flag=0;
		else if((d[0][0]=='O' || d[0][0]=='T') && (d[1][1]=='O' || d[1][1]=='T') && (d[2][2]=='O' || d[2][2]=='T') && (d[3][3]=='O' || d[3][3]=='T'))
			flag=1;
		else if((d[3][0]=='X' || d[3][0]=='T') && (d[2][1]=='X' || d[2][1]=='T') && (d[1][2]=='X' || d[1][2]=='T') && (d[0][3]=='X' || d[0][3]=='T'))
			flag=0;
		else if((d[3][0]=='O' || d[3][0]=='T') && (d[2][1]=='O' || d[2][1]=='T') && (d[1][2]=='O' || d[1][2]=='T') && (d[0][3]=='O' || d[0][3]=='T'))
			flag=1;
		else{
			for(int j=0;j<4;j++){
				if((d[j][0]=='X' || d[j][0]=='T') && (d[j][1]=='X' || d[j][1]=='T') && (d[j][2]=='X' || d[j][2]=='T') && (d[j][3]=='X' || d[j][3]=='T'))
					flag=0;
				else if((d[j][0]=='O' || d[j][0]=='T') && (d[j][1]=='O' || d[j][1]=='T') && (d[j][2]=='O' || d[j][2]=='T') && (d[j][3]=='O' || d[j][3]=='T'))
					flag=1;
				else if((d[0][j]=='X' || d[0][j]=='T') && (d[1][j]=='X' || d[1][j]=='T') && (d[2][j]=='X' || d[2][j]=='T') && (d[3][j]=='X' || d[3][j]=='T'))
					flag=0;
				else if((d[0][j]=='O' || d[0][j]=='T') && (d[1][j]=='O' || d[1][j]=='T') && (d[2][j]=='O' || d[2][j]=='T') && (d[3][j]=='O' || d[3][j]=='T'))
					flag=1;
				else{
					for(int k=0;k<4;k++)
						if(d[j][k]=='X' || d[j][k]=='O' || d[j][k]=='T')	cnt++;
				}
			}
		}
		if(flag==0)	fprintf(f2,"Case #%d: X won\n",i+1);
		else if(flag==1)	fprintf(f2,"Case #%d: O won\n",i+1);
		else if(cnt==16)	fprintf(f2,"Case #%d: Draw\n",i+1);
		else	fprintf(f2,"Case #%d: Game has not completed\n",i+1);
	}
	fclose(f1);
	fclose(f2);
}