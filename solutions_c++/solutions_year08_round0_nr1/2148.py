
#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <iostream>
#include <cstdlib>
#define N 100
#define M 1000
#define L 50

using namespace std;

void input();
void process();

FILE *fp = fopen("input.txt","rt");
FILE *fo = fopen("output.txt","wt");

int tcase;
int one;
int n;
int m;

char Engines[N+5][L+5];
char Query[M+5][L+5];

int main()
{
	one = 0;
	fscanf(fp,"%d%*c",&tcase);
	while(tcase-->0){
		one++;
		input();
		process();
	}
	fclose(fp);
	fclose(fo);
	return 0;
}

void input(){

	int i=0;
	fscanf(fp,"%d%*c",&n);

	for (i=0;i<n;i++){
		fgets(Engines[i],50,fp);
	}

	fscanf(fp,"%d%*c",&m);


	for (i=0;i<m;i++){
		fgets(Query[i],50,fp);
	}


}

void process(){
	int i,j;
	int flag[N+5]={0,},count=0;
	int getnum;
	int val=0;
	for (i=0;i<m;i++){
		for (j=0;j<n;j++){
			if (!strcmp(Engines[j],Query[i])){
				break;
			}
		}
		if (j<n){
			getnum = j;
			if (!flag[getnum]){
				count++;
				flag[getnum] = 1;
				if (count==n){
					val++;
					for (j=0;j<n;j++){
						flag[j] = 0;
					}
					count = 0;
					flag[getnum] = 1;
					count = 1;
				}
			}
		}
	}
	fprintf(fo,"Case #%d: %d\n",one,val);
}
