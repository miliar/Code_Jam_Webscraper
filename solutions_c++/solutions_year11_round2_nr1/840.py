#include <cstdio>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <vector>

#define MAX 110


using namespace std;


char tabela[MAX][MAX];
int N,T;
double M1[MAX];
double M2[MAX];


double WP(int j,int menos){


	int total=0;
	int wins=0;
		
	for(int k=0;k<N;k++){

		if(k==menos) continue;

		if(tabela[j][k]=='.') continue;
			total++;
		if(tabela[j][k]=='1') wins++;			

	}	

	return (double)wins/total;

	

}


double OWP(int j){

	if(M1[j]!=-1.0) return M1[j];

	double total=0;
	int count=0;

	for(int k=0;k<N;k++){
		
		if(tabela[j][k]=='.') continue;
		
		total+=WP(k,j);
		count++;
	}

	return (M1[j]=(total/count));
		

}

double OOWP(int j){

	if(M2[j]!=-1.0) return M2[j];

	double total=0;
	int count=0;

	for(int k=0;k<N;k++){
		
		if(tabela[j][k]=='.') continue;
		
		total+=OWP(k);
		count++;
	}

	return (M2[j]=(total/count));
	

}

int main(void){


	scanf("%d",&T);


	for(int i=1;i<=T;i++){

		printf("Case #%d:\n",i);

		
	
		scanf("%d\n",&N);

		for(int j=0;j<N;j++){
			M1[j]=M2[j]=-1.0;		
		}

		for(int j=0;j<N;j++){
			gets(tabela[j]);	
		}
		
		for(int j=0;j<N;j++){

			
			
			double rpi=0.25*WP(j,-1);

			rpi+=0.5*OWP(j);

			rpi+=0.25*OOWP(j);

			printf("%.10lf\n",rpi);

		
		}			

	}

	

	return 0;

}
