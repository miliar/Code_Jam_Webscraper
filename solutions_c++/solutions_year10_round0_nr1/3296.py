#include <cstdio>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
	
ifstream entrada("A-small.in");
ofstream salida("A-small.out");
	
unsigned int t=0;
entrada>> t;

for(unsigned int i=1;i<=t;++i){
	
	unsigned int n;	
	unsigned int k;	
	entrada>>n;
	entrada>>k;
	bool snappers[n];
	for(unsigned int j=0;j<n;++j)snappers[j]=false;


	
	for(unsigned int r=0;r<k;++r){
		bool b=true;
		for(unsigned int d=0;d<n && b;++d){
			b =snappers[d];
			snappers[d]= not snappers[d];
		}
	//for(unsigned int r=0;r<n;++r) cout<<snappers[r];
	//cout<<endl;
	}
	

	
	//Salida
	bool res=true;
	for(unsigned int re=0; re<n;re++) res= res and snappers[re];
	salida<<"Case #"<<i;
	if(res) salida <<": ON"<<endl;
	else salida <<": OFF"<<endl;
	


	
	
	
	
}




return 0;	
}
