#include<stdio.h>

#define MAXD 5000
#define MAXL 15


FILE *fs = fopen("input.txt","rt");
FILE *fp = fopen("output.txt","wt");

int N,D,L;
char data[MAXD+1][MAXL+1];

int testcase[MAXL+1][26];
int sol;

int main()
{
	int i,j,k;
	char c;

	fscanf(fs,"%d %d %d",&L,&D,&N);
	for(i=1;i<=D;i++) fscanf(fs,"%s\n",data[i]);

	for(i=1;i<=N;i++){
		for(j=1;j<=L;j++){
			for(k=0;k<26;k++) testcase[j][k]=0;
		}
		for(j=1;j<=L;j++){
			fscanf(fs,"%c",&c);
			if(c == '('){
				while(1){
					fscanf(fs,"%c",&c);
					if(c == ')') break;
					testcase[j][c-'a'] = 1;
				}
			}
			else testcase[j][c-'a'] = 1;
		}
		fscanf(fs,"\n");
		
		sol = 0;
		for(j=1;j<=D;j++){
			for(k=0;k<L;k++){
				if(!testcase[k+1][data[j][k]-'a']) break;
			}
			if(k == L) sol++;
		}

		fprintf(fp,"Case #%d: %d\n",i,sol);
	}
	return 0;
}
