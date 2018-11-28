#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define maxn 220
struct node{
	char ch;
	int pos;
}list[maxn];
int main(){
	int i,j,tem,T,zu,N,num;
	int x,y,tem1,tem2,tot;
	char s[3];
	FILE *fp1,*fp2;
	fp1 = fopen("A-large.in","r");
	fp2 = fopen("A-large.out","a");
	fscanf(fp1,"%d", &T);
	for (zu = 1; zu <=T; zu++){
		fscanf(fp1,"%d", &N);
		for (i = 1; i <= N; i++){
			fscanf(fp1,"%1s%d",s,&tem);
			list[i].ch = s[0];
			list[i].pos = tem;
		}
		tot = tem1 = tem2 = 0;
		x = y =1;
		for (i = 1; i <= N; i++){
			if (list[i].ch == 'O'){
				tem = abs(list[i].pos - x);
				if (tem < tem1) tem = 0;
				else tem = tem - tem1;
				tot += tem + 1;
				x = list[i].pos;
				tem1 = 0;
				tem2 += tem + 1;	
			}

			if (list[i].ch == 'B'){
				tem = abs(list[i].pos - y);
				if (tem < tem2) tem = 0;
				else tem = tem - tem2;
				tot += tem + 1;
				y = list[i].pos;
				tem2 = 0;
				tem1 += tem + 1;	
			}


		}
		fprintf(fp2,"Case #%d: %d\n",zu,tot);
	}
	return 0;
}