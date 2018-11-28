#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#define MAX 35

using namespace std;

int pessoa_ponto[MAX];
bool marca[MAX];

struct Surprise{
	int pontos;
	int quant;
};

bool compare ( const Surprise& a, const Surprise& b ){
    return a.quant > b.quant;
}

int main(){
	vector<Surprise> vetor;
	int N,S,P;
	int soma;
	int quantidade;
	
	cin>>quantidade;
	
	for(int inst=1;inst<=quantidade;inst++){
	
		cin>>N>>S>>P;
		//cout<<N<<" "<<S<<" "<<P<<endl;
		
		for(int i=0;i<MAX;i++){
			pessoa_ponto[i] = 0;
			marca[i] = false;
		}
			
		soma = 0;
			
		vetor.clear();
		
		//Pegar pontos
		int pp;
		for(int i=0;i<N;i++){
			cin>>pp;
			pessoa_ponto[pp]++;
		}
		
		//Possibilidades
		Surprise temp;
		for(int a=10;a>=0;a--){
			if(a<P) break;
			for(int b=a;b>=0;b--){
				if(b<a-1) break;
				for(int c=a;c>=0;c--){
					if(c<b-1 || c<a-1) break;
					if(!marca[a+b+c]){
						//cout<<a<<" "<<b<<" "<<c<<" == "<<a+b+c<<endl;
						marca[a+b+c] = true;
						soma += pessoa_ponto[a+b+c];
					}
				}
			}
		}
		
		for(int a=10;a>=0;a--){
			if(a<P) break;
			for(int b=a;b>=0;b--){
				if(b<a-2) break;
				for(int c=a;c>=0;c--){
					if(c<b-2 || c<a-2) break;
					if(b==a-2 || c==b-2 || c==a-2){
						if(!marca[a+b+c]){
							//cout<<a<<" "<<b<<" "<<c<<" == "<<a+b+c<<" (*)"<<endl;
							marca[a+b+c] = true;
							temp.pontos = a+b+c;
							temp.quant = 0;
							vetor.push_back(temp);
						//}
						}
					}
				}
			}
		}
		
		//cout<<"SOMA PARCIAL: "<<soma<<endl;
		
		//Carregar o vetor
		for(int i=0;i<vetor.size();i++){
			vetor[i].quant = pessoa_ponto[vetor[i].pontos];
		}
		
		sort(vetor.begin(),vetor.end(),compare);
		
		/*for(int i=0;i<vetor.size();i++){
			cout<<vetor[i].quant<<" "<<vetor[i].pontos<<endl;
		}
		cout<<endl;*/
		
		//Somar
		for(int i=0;i<S && i<vetor.size();i++){
			//if(i>vetor.size()) break;
			if(vetor[i].quant>S-i){
				soma+=S-i;
			}else{
				soma+=vetor[i].quant;
			}
		}
		
		
		/*for(int i=0;i<31;i++){
			if(marca[i]){
				cout<<i<<" ";
			}
		}*/
		
		printf("Case #%d: %d\n",inst,soma);
	}
	
	return 0;
	
}