#include<stdio.h>
#include<string.h>

#define MAXL 100

int n;
char data[MAXL+1];

FILE *fs = fopen("input.txt","rt");
FILE *fp = fopen("output.txt","wt");

int ret[MAXL+1];
int alphanum[200];

int main()
{
	int i,j,cnt,flag;
	__int64 p,sol;

	fscanf(fs,"%d\n",&n);
	for(i=1;i<=n;i++){
		for(j=0;j<200;j++) alphanum[j] = -1;
		fscanf(fs,"%s\n",data);
		alphanum[data[0]] = 1;
		ret[0] = 1;
				
		flag = 0; cnt = 2;
		for(j=1;j<strlen(data);j++){
			if(alphanum[data[j]] >= 0);
			else{
				if(!flag){ 
					alphanum[data[j]] = 0;
					flag = 1;
				}
				else alphanum[data[j]] = cnt++;
			}

			ret[j] = alphanum[data[j]];
		}

		sol = 0; p = 1;
		for(j=strlen(data)-1;j>=0;j--){
			sol += p * ret[j];
			p *= cnt;
		}
		fprintf(fp,"Case #%d: %d\n",i,sol);
	}

	return 0;
}
