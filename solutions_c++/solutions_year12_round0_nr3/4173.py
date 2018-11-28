#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
using namespace std;
int main(int argc, char *argv[]) {
	int casos,a,b,aux,contador;
	
	freopen( "input_s.txt", "r", stdin );
	freopen( "output_s.txt", "w", stdout );
	cin>>casos;
	for(int i=0;i<casos;i++){
		cin>>a>>b;contador=0;
		for(int j=a;j<b;j++){
			aux=j;
			int aux2=aux;
			int mult2=1;
			int c_it=1;
			while(aux2>=10){mult2*=10;aux2/=10;c_it++;}
			//cout<<j<<" "<<aux2<<" "<<mult2<<"\n";
			while(c_it>1){
				c_it--;
				aux=(aux%10)*mult2+aux/10;
		
				if(aux<=b && aux>j ){
					
					contador++;//cout<<j<<";"<<aux<<" "<<contador<<"\n";
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<contador<<"\n";
	}
	return 0;
}

