#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

typedef struct nodo{
	vector<int> filhos;
	char valor;
}nodo;
int atual;
nodo arvore[100000];
nodo coloca(char a){
	nodo no;
	no.valor = a;
	no.filhos.clear();
	return no;
}
void insert(string temp,int pain){
	bool ind;
	for(unsigned int i = 0;i<temp.size();i++){
		ind  = 0;
		for(unsigned int j = 0;j < (arvore[pain].filhos).size();j++){
			if(arvore[arvore[pain].filhos[j]].valor == temp[i]){
				pain= arvore[pain].filhos[j];
				ind  = 1;	
				break;
			}
		}
		if(!ind){
			arvore[atual] = coloca( temp[i]);
			arvore[pain].filhos.push_back(atual);
			pain= atual++;
		}

	}
}


int procurar(char a, int pai){

	for(unsigned int i  = 0;i<arvore[pai].filhos.size();i++){
		if(arvore[arvore[pai].filhos[i]].valor == a){
			return arvore[pai].filhos[i];
		}
	}
	return -1;
}
int achar(string a,string b,int no, bool dentro){ 
	if(b.size() == 0) {
		return 1;
	}
	if(!dentro){
		if(b[0] != '('){

			int achado = procurar(b[0],no);
			if(achado == -1) return 0;
			a+=b[0];
			b.erase(b.begin());
			return achar(a,b,achado,0);
		}
		b.erase(b.begin());
	}
	if(b[0] == '(') b.erase(b.begin());
	string temp;
	temp.clear();
	while(b[0]!= ')'){
		temp+=b[0];


		b.erase(b.begin());
	}
	b.erase(b.begin());
	
	int soma = 0;
	for(unsigned int i = 0;i<temp.size();i++){
		soma+=achar(a,temp[i]+b,no,0);
	}
	return soma;




}


int main(){
	int L,D,N;
	string temp;
	scanf("%d %d %d",&L,&D,&N);
	atual = 1;
	for(int i = 0;i<D;i++){
		cin >> temp;
		insert(temp, 0);
	}
	
	for(int i = 0;i<N;i++){
		cin >> temp;
		printf("Case #%d: %d\n",i+1,achar("",temp,0,0));

	}
	
	
	
	return 0;
}

