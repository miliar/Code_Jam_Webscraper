#include <stdio.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <utility>
#include <string>
#include <map>

/*
istringstream buffer(x.first);
int a; buffer >> a;

int some_int;
ostringstream buffer;
buffer << some_int;
string some_string = buffer.str();
*/

using namespace std;

typedef pair <string,string> par;
vector<par> nums;

string cambiarNumeros(int cantD, string n){
	string temp;

	switch(cantD){
		case 1:
			temp=n.substr(n.length()-1,n.length())+n.substr(0,n.length()-1);
			break;

		case 2:
			temp=n.substr(n.length()-2,n.length())+n.substr(0,n.length()-2);
			break;

		case 3:
			temp=n.substr(n.length()-3,n.length())+n.substr(0,n.length()-3);
			break;	
	}

	return temp;

}

int sacarCasos(par AB){
	map<int,int> c;
	int a,b,numc,casos;
	string num,numCambiado;
	istringstream A(AB.first);
	istringstream B(AB.second);
	A >> a; B >> b;
	casos=0;
	for(int i=a;i<b-1;i++){
		ostringstream buffer; //
		buffer << i;          // Convierto el numero a string
		num =buffer.str();    //
		if(num.length()==2){
			//Si tiene 2 digitos
			numCambiado=cambiarNumeros(1,num);
			istringstream nc(numCambiado);
			nc >> numc;
			if(numc<=b && numc>i){
				//c[numc]=numc;
			//	cout<<num<<"/"<<numc<<endl; //QUITAR
				casos++;
			}
		}else if(AB.first.length()==3){
			//Si tiene 3 digitos
			for(int j=0;j<2;j++){
				numCambiado=cambiarNumeros(j+1,num);
				istringstream nc(numCambiado);
				nc >> numc;
				if(numc<=b && numc>i){
				//	c[numc]=numc;
				//	cout<<num<<"/"<<numc<<endl; //QUITAR
					casos++;
				}
			}
		}else if(AB.first.length()==4){
			//Si tiene 4 digitos
			for(int j=0;j<3;j++){
				numCambiado=cambiarNumeros(j+1,num);
				istringstream nc(numCambiado);
				nc >> numc;
				if(numc<=b && numc>i){
				//	c[numc]=numc;
					
				//	cout<<num<<"/"<<numc<<endl; //QUITAR
					casos++;
				}
			}
		}	
	}
	return casos;
}

int main(int argc, char *argv[]){
	int cant;
	par x;
	string Pal;
	cin>>cant;	
	vector <par> Numeros;
	//Leyendo los numeros A y B
	for (int i=0;i<cant;i++){
		cin>>Pal;
		x.first=Pal;		
		cin>>Pal;
		x.second=Pal;
		Numeros.push_back(x);
	}

	for(int i=0;i<cant;i++){
		cout<<"Case #"<<i+1<<": "<<sacarCasos(Numeros[i])<<endl;
	}

}