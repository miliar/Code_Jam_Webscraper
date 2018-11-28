#include<iostream>

using namespace std;

int main(){

	int T;
	cin>>T;

	for(int i = 0 ; i < T; i++){
	
		int k;
		cin >> k;
		int menor = 1e8;
		int zero = 0;
		int soma = 0;

		for(int j = 0 ; j < k ; j++){
			int bla;
			cin>>bla;

			
			if(bla < menor){
				menor = bla;
			}

			zero ^= bla;
			soma += bla;
		
		}
	

		if(zero == 0)
			cout<<"Case #"<<i+1<<": "<<soma - menor<<endl;
		else
			cout<<"Case #"<<i+1<<": NO"<<endl;
	
	}



	return 0;

}

