#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <vector>
#include <algorithm>
#include <map>

#define _USE_MATH_DEFINES

using namespace std;

typedef unsigned long long ull;

int N;
int d[10001],l[10001];
int dist=0;
int pass=0;
int diff=0;
int swing[10001][10001];

int main(int argc,char **argv){
	FILE *fin,*fout;
	int cases=0;

	int i=0,j=0;
	int cur=0,nxt=0,ref=0;
	
	clock_t t0;
	t0=clock();

	fin =fopen("A-small-attempt1.in","rt");
	fout=fopen("A-small-attempt1.out","wt");
	
	fscanf(fin,"%d\n",&cases);
	for(i=1;i<=cases;i++){
		fscanf(fin,"%d\n",&N);
		printf("case %d\n",i);
		for(j=1;j<=N;j++){
			fscanf(fin,"%d %d",&d[j],&l[j]);
		}
		fscanf(fin,"%d",&dist);
		pass=0;

		memset(swing,0x0,10001*10001*sizeof(int));

		swing[0][1]=min(d[1],l[1]);
		for(cur=1;cur<=N;cur++){
			for(ref=0;ref<cur;ref++){
				//printf("1\n");getchar();
				if(d[cur]+swing[ref][cur]>=dist){
					pass=1;cur=N+1;
				}
				//printf("%d\n",swing[ref][cur]);
				//printf("2\n");getchar();
				if(swing[ref][cur]==0)
					continue;
				//printf("3\n");getchar();
				for(nxt=cur+1;nxt<=N;nxt++){
					
					if(d[cur]+swing[ref][cur]<d[nxt])
						break;
					swing[cur][nxt]=min(d[nxt]-d[cur],l[nxt]);
					//printf("%d %d = %d\n",cur,nxt,swing[cur][nxt]);getchar();
				}
			}
		}

		if(pass==0)
			fprintf(fout,"Case #%d: NO\n",i);
		else
			fprintf(fout,"Case #%d: YES\n",i);
	}

	fclose(fin);
	fclose(fout);
	printf("Time taken = %lf\n",(double)(clock()-t0)/(double)CLOCKS_PER_SEC);
	return 0;
}