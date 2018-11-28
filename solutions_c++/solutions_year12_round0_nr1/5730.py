#include <stdio.h>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <utility>
#include <string>
#include <map>

using namespace std;

map<char,char> alf;

void llenarAlfabeto(){
		alf['a']='y';
		alf['b']='h';
		alf['c']='e';
		alf['d']='s';
		alf['e']='o';
		alf['f']='c';
		alf['g']='v';
		alf['h']='x';
		alf['i']='d';
		alf['j']='u';
		alf['k']='i';
		alf['l']='g';
		alf['m']='l';
		alf['n']='b';
		alf['o']='k';
		alf['p']='r';
		alf['q']='z';
		alf['r']='t';
		alf['s']='n';
		alf['t']='w';
		alf['u']='j';
		alf['v']='p';
		alf['w']='f';
		alf['x']='m';
		alf['y']='a';
		alf['z']='q';
}

string traducir(string f){
	string res=f;
	int x=f.length();
	for(int i=0;i<x;i++){
		if(res[i]!= ' '){
			res[i]=alf[f[i]];
		}
	}
	return res;

}


int main(int argc, char *argv[]){
	int cant;
	string Pal;
	char Frase[256];
	llenarAlfabeto();
	cin>>cant;
	cin.ignore(1);
	vector<string> Frases;
	for (int i=0;i<cant;i++){
		cin.getline(Frase,256,'\n');
		Frases.push_back(Frase);				
	}

	for (int i=1;i<=cant;i++){
		Pal=traducir(Frases[i-1]);
		cout<<"Case #"<<i<<": "<<Pal<<endl;
	}
}