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

#define EPS 0.00000001
#define MAX 210

using namespace std;

int C,D,T;
int p[MAX];
int qtd[MAX];
int qtd2[MAX];


bool valido(double tempo){

	int atual=C-1;
	double posAtual=p[C-1]+tempo;
	qtd2[C-1]--;
	
	while(atual>=0){
		
		if(qtd2[atual] == 0){
			atual--;
			continue;
		}
		
		if(posAtual-p[atual]>=D){

			double a=posAtual-D;
			double b=p[atual]+tempo;
			qtd2[atual]--;

			if(a<b) posAtual=a;
			else posAtual=b;

			continue;
		}

		if(posAtual-D<p[atual]-tempo) return false;
		
		posAtual=posAtual-D;

		qtd2[atual]--;


	}


	return true;

}


int main(void){


	scanf("%d",&T);


	for(int i=1;i<=T;i++){

		printf("Case #%d: ",i);


		scanf("%d %d",&C,&D);

		for(int j=0;j<C;j++){
			scanf("%d %d",&p[j],&qtd[j]);
		}
		

		double fim=1000000.0;
		double ini=0;
		double tempo=0;

		while(ini-fim<=EPS){

			//printf("aaaa\n");

			//tempo+=0.1;


			for(int j=0;j<C;j++) qtd2[j]=qtd[j];

			
			tempo=(ini+fim)/2;

			
			if(valido(tempo)){
				fim=tempo-EPS;
				//printf("bbb\n");
			}
			else{
				//printf("cccc\n");	
				ini=tempo+EPS;
			}

		}

		printf("%.10lf\n",tempo);

		
		

	}
	
	

	return 0;

}
