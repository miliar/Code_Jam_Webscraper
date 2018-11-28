#include "cstdio"

int tab[100][100];
int win[100];
int lose[100];
double wp[100];
double owp[100];
double oowp[100];
FILE *in=fopen("A-large.in","r");
FILE *out=fopen("outlarge","w");

int main(){
	int t,n;
	fscanf(in,"%d",&t);
	char napis[200];

	for(int k=1;k<=t;k++){		
		fscanf(in,"%d ",&n);
		
		// kasuj
		for(int i=0;i<n;i++){
			win[i]=0;
			lose[i]=0;
		}	

		// input
		for(int i=0;i<n;i++){
			fgets(napis,200,in);
			for(int j=0;j<n;j++){
				// not played
				if(napis[j]=='.') tab[i][j]=2;
				// lose
				else if(napis[j]=='0'){ 
					tab[i][j]=0;
					lose[i]++;
				}
				// win
				else{
					tab[i][j]=1;	
					win[i]++;
				}			
			}
			// wp
			wp[i]=(double)win[i]/(win[i]+lose[i]);
		}
		double sum;
		double count;

		// OWP 
		for(int i=0;i<n;i++){
			sum=0;
			count=0;
			for(int j=0;j<n;j++){
				if(i==j || tab[j][i]==2) continue;
				if(tab[j][i]==0)
					sum+=(double)win[j]/(win[j]+lose[j]-1);
				else if(tab[j][i]==1)
					sum+=(double)(win[j]-1)/(win[j]+lose[j]-1);
				count++;
			}
			owp[i]=sum/count;
		}


		// OOWP
		for(int i=0;i<n;i++){
			sum=0;
			count=0;
			for(int j=0;j<n;j++){
				if(tab[i][j]!=2){
					sum+=owp[j];
					count++;
				}
			}
			oowp[i]=(double)sum/count;
		}

			

		// print
		double x;
		fprintf(out,"Case #%d:\n",k);
		for(int i=0;i<n;i++){
			x=(double) 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			fprintf(out,"%.9lf\n",x);
		}
	}

return 0;
}