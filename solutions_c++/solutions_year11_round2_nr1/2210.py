// for  problem a
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main()
{
	int T,N;
	char *map;
	double *WP, *L, *W, *OWP, *OOWP,*S;
	cin>>T;
	for(int i = 1; i <=T; i++){
		cin>> N;
		map = new char[N*N];
		WP  = new double[N];
		L  = new double[N];
		W  = new double[N];
		OWP = new double[N];
		OOWP= new double[N];
		S   = new double[N];	
		for(int j = 0; j < N; j++){
			WP[j] = 0;
			L[j] = 0;
			W[j] = 0;
			OWP[j] = 0;
			OOWP[j] = 0;
			S[j] = 0;
			for(int k = 0; k < N; k++){
				cin>> map[j*N+k];
				if(map[j*N+k]=='0') L[j]++;
				if(map[j*N+k]=='1') W[j]++; 
			}			
			WP[j] = W[j]/(W[j]+L[j]);
		}
		
		for(int j = 0; j < N; j++){
			bool flag = 0;
			for(int k = 0; k < N; k++){
				 if(map[j*N+k]!='.'){
					
					  if(map[j*N+k]=='0') OWP[j] += (W[k]-1)/(W[k]+L[k]-1);
					  if(map[j*N+k]=='1') OWP[j] += (W[k])/(W[k]+L[k]-1);
				} 
					
			}
			OWP[j] = OWP[j]/(W[j]+L[j]); 
		}

		 for(int j = 0; j < N; j++){
                        for(int k = 0; k < N; k++){
                                if(map[j*N+k]!='.') OOWP[j] += OWP[k];
                        }
                        OOWP[j] = OOWP[j]/(W[j]+L[j]);
                }
		 cout<<"Case #"<<i<<":\n";
		for(int j = 0; j < N; j++){

			S[j] = 0.25*WP[j] + 0.50*OWP[j] + 0.25* OOWP[j];
			cout<<setprecision(9)<<S[j]<<endl;
		}
		
		delete [] map;
		delete [] WP;
		delete [] W;
		delete [] L;
		delete [] OWP;
		delete [] OOWP;
	}
}
