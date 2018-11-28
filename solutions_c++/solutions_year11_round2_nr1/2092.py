#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>
#include <errno.h>
#include <float.h>
#include <limits.h>
#include <locale.h>
#include <string.h>
#include <time.h>
#include "string"
#include "vector"
#include "stack"
#include "queue"
#include "algorithm"
#include "map"
#include "memory.h"
#define inf 0x3f3f3f3f
using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for(int ncase=1;ncase<=T;ncase++){
		int n;
		scanf("%d",&n);
		char mat[n][n];
		int games[n], wins[n];
		double WP[n];
		double OWP[n];
		double OOWP[n];
		for(int i=0;i<n;i++){
			scanf("%s",mat[i]);
		}
		for(int i=0;i<n;i++){
			wins[i] = 0; games[i] = 0;
			for(int j=0;j<n;j++){
				if(mat[i][j] != '.'){
					games[i]++;
					wins[i] += mat[i][j]-'0';
				}
			}
		}
		//WP
		for(int i=0;i<n;i++)
			WP[i] = (double) ((double)wins[i]/(double)games[i]);
		
		//OWP
		for(int i=0;i<n;i++){
			int nums=0;
			double wp=0;
			for(int j=0;j<n;j++)
				if(mat[i][j] != '.'){
					nums++;
					wp+= (double)((double)(wins[j]-(mat[j][i]-'0'))/(double)(games[j]-1));
				}
			OWP[i] = (double)(wp/(double)nums); 
		}
		//OOWP
		for(int i=0;i<n;i++){
			int nums=0;
			double wp=0;
			for(int j=0;j<n;j++)
				if(mat[i][j] != '.'){
					nums++;
					wp+=OWP[j];
				}
			OOWP[i] = (double)(wp/nums);
		}
		printf("Case #%d:\n",ncase);
		for(int i=0;i<n;i++){
			double res = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
			printf("%lf\n",res);
		}
	}
	return 0;
}
