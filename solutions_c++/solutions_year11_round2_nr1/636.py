#include <iostream>
#include<stdio.h>

using namespace std;


int gcd(long long int a, long long int b){
	if (b>a){
		long long int c = b;
		b=a;
		a=c;
	}

	while (b>0){
		long long int c = a%b;
		a=b;
		b=c;

	}
	return a;

}


int main(){
	int nt;
	
	long long int pg,pd,N;
	cin >> nt;
	for(int it = 0; it<nt; it++){
		cin >> N;
		
		char p[N][N];
		float WP[N];
		float OWP[N], OOWP[N];
		int k[N];
		for(int i = 0; i < N; i++){
			float sum=0;
			k[i]=0;
			for(int j = 0; j < N; j++){
				cin >> p[i][j];
				if (p[i][j] == '1') sum+=1;
				if (p[i][j] != '.') k[i]++;
			}
			WP[i]=sum/k[i];
			//cout<<WP[i]<<" "<<sum<<" "<<k[i]<<endl;	
			
		}
		for(int i = 0; i < N; i++){
			float sum=0;
			for(int j = 0; j < N; j++){
				if (p[i][j]!='.') {
					if(p[j][i]=='0')
						sum+= WP[j]*k[j]/(k[j]-1);
					else
						sum+= (WP[j]*k[j]-1)/(k[j]-1);
				}
			}
			
			OWP[i]=sum/k[i];	
			//cout<<OWP[i]<<endl;	
		}
		for(int i = 0; i < N; i++){
			float sum=0;
			for(int j = 0; j < N; j++){
				if (p[i][j]!='.') {
					sum+=OWP[j];
				}
			}
			
			OOWP[i]=sum/k[i];	
			//cout<<OOWP[i]<<endl;	
		}
		
		cout<<"Case #"<<it+1<<":"<< endl;
		
		for(int i = 0; i < N; i++){
			printf("%.8f\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}
		
		
		
		
		
		
	}

	return 0;
}



