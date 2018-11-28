#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	int n;
	cin>>n;
	int cont = 0;
	
	for(int i=0; i<n; i++){
		int cont = 0;
		
		int s;
		cin>>s;
		
		char searchs[100][100];
		char querys[1000][100];
		string auxi;
		int aux[100];
		int ind = s;
		
		for(int j=-1; j<s; j++){
			cin.getline((char*)auxi.c_str(), 100);
			strcpy(searchs[j], auxi.c_str());
		}
		for(int j=0; j<s; j++){
			aux[j] = 0;
		}
		
		int q;
		cin>>q;
		
		for(int j=-1; j<q; j++){
			cin.getline((char*)auxi.c_str(), 100);
			strcpy(querys[j], auxi.c_str());
		}
		
		for(int j=0; j<q; j++){
			int k = 0;
			
			while(strcmp(searchs[k], querys[j]) != 0){
				k++;
			}
			
			if( (strcmp(searchs[k], querys[j]) == 0) && (aux[k] == 0) ){
				aux[k] = 1;
				ind--;
			}
			
			if(ind < 1){
				for(int l=0; l<s; l++){
					aux[l] = 0;
				}
				aux[k] = 1;
				ind = s - 1;
				cont++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<cont<<endl;
	}
	return 0;
}
