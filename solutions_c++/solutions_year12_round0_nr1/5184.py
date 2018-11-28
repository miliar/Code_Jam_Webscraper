#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

char letra[256];

int main()
{
	for(int i=0;i<256;i++)
		letra[i] = '*';
		
	letra['q'] = 'z';
	letra['z'] = 'q';

	char frase[256];
	char frase2[256];
	int quant;
	
	for(int i=0;i<3;i++){
	
		cin.getline(frase,256);
		//scanf("%s",frase);
		cin.getline(frase2,256);
		//scanf("%s",frase2);
		
		for(int i=0;frase[i]!='\0';i++){
			cout<<frase[i];
		}
		cout<<endl;
		
		for(int i=0;frase2[i]!='\0';i++){
			letra[frase[i]] = frase2[i];
			letra[frase[i]] = frase2[i];
		}
	}
	
	for(int i=0;i<256;i++){
		if(letra[i]!='*'){
			cout<<(char)i<<" => "<<letra[i]<<endl;
		}
	}
	
	
	
	for(int i=0;i<30;i++){
		cin.getline(frase,256);
		
		/*for(int k=0;frase[k]!='\0';k++){
			cout<<frase[k];
		}
		cout<<endl;*/
	
		printf("Case #%d: ",i+1);
		for(int j=0;frase[j]!='\0';j++){
			if(letra[frase[j]]!='*'){
				cout<<letra[frase[j]];
			}else{
				cout<<"&";
			}
		}
		cout<<endl;
	}
	
	
	
    return 0;
}
