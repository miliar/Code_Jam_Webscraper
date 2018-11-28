#include <stdio.h>
#include <cstring>


int main(){
	int cases;
	scanf("%d",&cases);
	int nteams;
	char data[200][200];
	double WP[200];
	double OWP[200];
	int NP[200];
	double OOWP[200];
	for(int c = 1;c<=cases;c++){
		scanf("%d",&nteams);

		memset(NP,0,sizeof(NP));
		memset(OWP,0,sizeof(OWP));
		memset(OOWP,0,sizeof(OOWP));
		memset(WP,0,sizeof(WP));
		for(int i =0;i<nteams;i++){
			scanf(" %s",data[i]);	
			for(int j = 0;j<nteams;j++){
				if(data[i][j] != '.'){
					if(data[i][j] == '1')
						WP[i]+=1;
				//	else
				//		OWP[i]+=1;
					NP[i]++;
				}
			}
			WP[i]/=NP[i];
//			OWP[i]/=NP[i];
		}
		double sumOWP = 0;

		for(int i = 0;i<nteams;i++){
			int numOp = 0;
			for(int j = 0;j<nteams;j++){
				if(data[i][j] != '.'){

					double withoutme = WP[j]*NP[j];
					if(data[i][j] == '0'){
						withoutme-=1;
						withoutme/=(NP[j]-1);	
					}else{
//						withoutme+=1;
						withoutme/=(NP[j]-1);	

					}

//					printf("%d %d ---> %lf\n",i,j,withoutme);
					OWP[i]+=withoutme;
					numOp++;	
				}
			}
			OWP[i]/=numOp;
		}


		for(int i = 0;i<nteams;i++){
			int numOp = 0;
			for(int j = 0;j<nteams;j++){
				if(data[i][j] != '.'){
					OOWP[i]+=OWP[j];
					numOp++;
				}
			}
			OOWP[i]/=numOp;
		}


		printf("Case #%d:\n",c);

//		for(int i = 0;i<nteams;i++){
//			printf("%lf %lf %lf \n",WP[i],OWP[i],OOWP[i]);
//		}

		for(int i = 0;i<nteams;i++){
			printf("%.7lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}

		
	}
	return 0;
}
