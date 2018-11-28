#include<iostream>
#include<vector>
#include<string>

using namespace std;

string dicionario[5010], bloco, inteiro;
vector <string> palavra;

int main(){
	int l,d,n,j,soma,caso=1;
	char temp;
	cin>>l>>d>>n;
	for(int i=0; i<d; i++) cin>>dicionario[i];
	//cout<<"Término dicionario\n";
	for(int i=0; i<n; i++){
		palavra.clear();
		//cout<<"Entrou\n";
		cin>>inteiro;
		//cout<<"Inteiro: "<<inteiro<<endl;
		j=0;
		while(j<inteiro.length()){	
			if(inteiro.at(j)=='('){
				bloco="";
				j++;
				while(inteiro.at(j)!=')'){
					j++;
					//cout<<"ok\n";
					bloco.append(inteiro,j-1,1);

				}
				j++;
				palavra.push_back(bloco);
			}
			else{
				bloco=""; bloco.append(inteiro,j,1);
				palavra.push_back(bloco);
				j++;
			}
		}
		//for(int k=0; k<palavra.size(); k++) cout<<palavra[k]<<endl;
		soma=0;
		for(int k=0; k<d; k++){
			//cout<<"Palavra: "<<dicionario[k]<<endl;
			j=0;
			while(j<dicionario[k].length()){
				if(palavra[j].find(dicionario[k].at(j))==string::npos) break;
				else j++;
			}
			//cout<<"J final= "<<j;
			if(j==l) soma++;
		}
			cout<<"Case #"<<caso<<": "<<soma<<endl;
			caso++;
	}	
}
