#include <iostream>

using namespace std;


struct state{
	int antal_kampe;
	int vundet;
	int tabt;
	double wp;
	int * spilet_imod;
};
struct testcase{
	int number_of_teams;
	state * statestik;
};

double* owp;
double* oowp;
double * rpi;

testcase *testcases;
int antal_cases=0;

void solve(int kampe,state * statestik);

void read();

int main(){
	read();
	FILE *fil = fopen("svar.txt","w");
	for (int i=0;i<antal_cases;i++){
		owp = new double[testcases[i].number_of_teams];
		oowp = new double[testcases[i].number_of_teams];
		rpi = new double[testcases[i].number_of_teams];
		
		solve(testcases[i].number_of_teams,testcases[i].statestik);
		//solve
		fprintf(fil,"Case #%u:\n",i+1);
		for (int y=0;y<testcases[i].number_of_teams;y++){
			fprintf(fil,"%f\n",rpi[y]);
		}
		delete owp;
		delete oowp;
		delete rpi;



	}

	return 0;


}

void solve(int kampe,state * statestik){
	// først regn OWP
	for (int a=0;a<kampe;a++){
		double samlet=0;
		for (int i=0;i<kampe;i++){
			if((statestik[a].spilet_imod[i]!=-1)){
				double temp =0;
		
				if(statestik[i].spilet_imod[a]==1){
					temp = (double)(statestik[i].vundet-1)/(double)(statestik[i].antal_kampe-1);
				}else{
					temp = (double)(statestik[i].vundet)/(double)(statestik[i].antal_kampe-1);
				}
				

				samlet+= temp;
			}
		}
		owp[a]= samlet/(double)(statestik[a].antal_kampe);

	}
	for (int a=0;a<kampe;a++){
		double samlet=0;
		for (int i=0;i<kampe;i++){
			if((statestik[a].spilet_imod[i]!=-1)){
				samlet+= owp[i];
			}
		}
		oowp[a]= samlet/(double)statestik[a].antal_kampe;

	}
	for (int a=0;a<kampe;a++){
		rpi[a]= ((double)0.25*statestik[a].wp )+ ((double)0.5*owp[a])+((double)0.25*oowp[a]);
	}

	return;
	
}





void read(){
	FILE *fil = fopen("input.txt","r");
	fscanf(fil,"%u",&antal_cases);
	testcases = new	testcase[antal_cases];
		for (int i=0;i<antal_cases;i++){
			fscanf(fil,"%u",&testcases[i].number_of_teams);
			testcases[i].statestik = new state[testcases[i].number_of_teams];
			
			for (int y=0;y<testcases[i].number_of_teams;y++){
				testcases[i].statestik[y].spilet_imod = new int[testcases[i].number_of_teams];
				int tabte =0;
				int vundet=0;
				for (int k=0;k<testcases[i].number_of_teams;k++){
					char temp =' ';
					fscanf(fil,"%c",&temp);
					switch (temp){
					
					case '1':
						vundet++;
						testcases[i].statestik[y].spilet_imod[k] =1;
						break;

					case '0':
						tabte++;
						testcases[i].statestik[y].spilet_imod[k] =0;
						break;
				
					case '.':
					
						testcases[i].statestik[y].spilet_imod[k] =-1;
						break;
					default:
						k--;	
						break;
					}
				
				}
				testcases[i].statestik[y].antal_kampe = vundet+tabte;
				testcases[i].statestik[y].tabt = tabte;
				testcases[i].statestik[y].vundet = vundet;
				testcases[i].statestik[y].wp = (double)vundet/(double) (vundet+tabte);
				
			}

		}

	return;
}