#include<iostream>
#include<vector>

using namespace std;


int main(){

	int T;
	cin >> T;

	for(int i = 0; i < T; i++){
	
		int k;
		cin>>k;

		vector<int> v(k);

		for(int j = 0; j < k; j++){
			cin>> v[j];
		}

		int conta = 0;
		for(int j = 0 ; j < k; j++){
			
			if(v[j] != j+1) 
				conta++;
		}
		cout<<"Case #"<<i+1<<": "<<conta<<".000000"<<endl;
	}



	return 0;
}


