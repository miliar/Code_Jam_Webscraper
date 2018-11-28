#include <iostream>
#include <stdio.h>

using namespace std;

#define MAX 100
int main(int argc , char *argv[]){
	int cases;

	FILE *fin = fopen(argv[1],"r");
	fscanf(fin, "%d\n",&cases);

	double RPI[MAX];
	double WPI[MAX];
	double OWPI[MAX];
	double OOWPI[MAX];
	char plays[MAX][MAX];

	for(int cas=1;cas<=cases;++cas){
		int N;
		
		fscanf(fin, "%d\n", &N);
		for(int i=0;i<N;++i){
			for(int j=0;j<N;++j){
				fscanf(fin, "%c",&plays[i][j]);
			}

			
			fscanf(fin,"\n");
			RPI[i]=0.0;
			WPI[i]=0.0;
			OWPI[i]=0.0;
			OOWPI[i]=0.0;
			
			
			int cont=0,win=0;
			for(int j=0;j<N;++j){
				if(plays[i][j]!= '.'){
					++cont;
					if(plays[i][j]=='1'){
						++win;
					}
				}
			}
			WPI[i]=(double)win/cont;
		}

		for(int i=0;i<N;++i){
			int total = 0;
			int cont=0, win=0;
			double aux = 0.0;
			for(int j=0;j<N;++j){
				if(i==j) continue; // same team
				if(plays[j][i]=='.') continue; // they do not play against each other
				for(int k=0;k<N;++k){
					if(i==k) continue;
					if(plays[j][k]=='.') continue;
					if(plays[j][k]=='1') ++win;
					++cont;
				}
				++total;
				if(win>0)
					aux += (double)win/cont;
				else 
					aux += 0;
				win=0; cont=0;
			}
			//fprintf(stdout,"segun %d tiene %f (win %d - cont %d)\n",i,aux, win,cont);
			OWPI[i] = aux/total;
			
		}

		for(int i=0;i<N;++i){
			int total = 0;
			for(int j=0;j<N;++j){
				if(plays[j][i]!='.'){
					total++;
					OOWPI[i]+=OWPI[j];
				}
			}
			OOWPI[i]/=total;
		}
	
	

		for(int i=0;i<N;++i){
			RPI[i] = 0.25*WPI[i] + 0.5*OWPI[i]+0.25*OOWPI[i];
		}
		// Output
		fprintf(stdout,"Case #%d:\n",cas);
	
		for(int i=0;i<N;++i)
			fprintf(stdout,"%.15f\n",RPI[i]);

	}
	return 0;
}
