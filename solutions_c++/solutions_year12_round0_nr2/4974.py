#include <iostream>
#include <string>
#include <map>
#include <cmath>
#include <utility>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>


using namespace std;


const int longlinea = 1000;

bool diffesbuena(int a,int b,int c,int num){
int diff1=a-b;
int diff2=a-c;
int diff3=b-c;

if(diff1>num || diff1<-num) return false;
if(diff2>num || diff2<-num) return false;
if(diff3>num || diff3<-num) return false;
return true;
}

bool sonmayores(int a, int b, int c, int p){
if(a>=p || b>=p || c>=p){
//cout << " # " << a<<" " << b<<" " << c<< " " << a+b+c << endl;
return true;}
else return false;
}




bool comprueba(int a, int b, int c, int valor, int p,int num){
	if(diffesbuena(a,b,c,num)){
		if(a+b+c==valor){
			if (sonmayores(a,b,c,p)) 
				return true;
			else 
				return false;
		}

		if(comprueba(a+1,b,c,valor,p,num) || comprueba(a,b+1,c,valor,p,num) || comprueba(a,b,c+1,valor,p,num))
			return true; 
	}
	return false;
}


bool comprueba2(int valor, int p,int num){
if(valor<5)return comprueba(0,0,0,valor,p,num);
if(valor>=3*p-2*num){
	if(num==2)
		//cout << "comodin para: "<< valor<< " "<<p <<" "<< 3*p-2*num <<endl;
	return true;
}
else return false;
}



int main (int argc, char ** argv)
{
int numcasos;

cin >> numcasos;

for (int i=1;i<=numcasos;i++){
int googlers=0;
int sorpresa=0;
int p=0;
int total=0;
cin >> googlers >> sorpresa >> p;
	for(int j=1;j<=googlers;j++){
		int valor;
		cin>> valor;
		//if(comprueba(0,0,0,valor,p,1))total++;
		//else if (sorpresa>0 && comprueba(0,0,0,valor,p,2)){total++;sorpresa--;}
		if(comprueba2(valor,p,1))total++;
		else if(sorpresa>0 && comprueba2(valor,p,2)){total++;sorpresa--;}

	}
cout << "Case #" << i << ": "<<total <<endl;
}
}
