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
	
	cin >> nt;
	for(int it = 0; it<nt; it++){
		int C, D;
		cin >> C>>D;
		int P[C],V[C];
		
		for(int i = 0; i < C; i++){
			cin>>P[i]>>V[i];
		}
		for(int i = 0; i < C;i++){
			for(int j = 0; j < C-1; j++){
				if(P[j]>P[j+1]){
					int tem=P[j];
					P[j]=P[j-1];
					P[j-1]=tem;
					tem=V[j];
					V[j]=V[j-1];
					V[j-1]=tem;
				}	
			}
		}
		
		int pivot=P[0]+(V[0]-1)*D;
		int maxd=(V[0]-1)*D;
		for(int i = 1;i<C;i++){
			if(pivot+D<P[i]){
				pivot=P[i]+(V[i]-1)*D;
				int disp=(V[i]-1)*D;
				if(disp>maxd) maxd=disp;
			}else{
				
				int disp=pivot-P[i]+D+(V[i]-1)*D;
				pivot=pivot+V[i]*D;
				if(disp>maxd) maxd=disp;
			}
		} 
		float fdisp=((float)maxd)/2.0;
		
		
		cout<<"Case #"<<it+1<<": ";
		printf("%.1f\n",fdisp);
				
		
	}

	return 0;
}



