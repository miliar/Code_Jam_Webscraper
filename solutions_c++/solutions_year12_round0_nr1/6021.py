#include <iostream>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
using namespace std;

void traslator(int x){
	 for(int k=0;k<x;k++){
		 
	char dicA[]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	char dicB[27];
	for(int i=97;i<123;i++){
		dicB[i-97]=i;
		}
	char array1[102];
	string to;
		cin>>to;
	strcpy(array1,to.c_str());
	int tam=strlen(array1);
	char array2[tam+1];
	
	for(int i=0;i<tam;i++){
		if(array1[i]==' '){
			array2[i]=array1[i];
			}else
		for(int j=97;j<123;j++)
		
		if(array1[i]==dicA[j-97]){
			
			array2[i]=dicB[j-97];
			}
		}

		cout<<"Case #"<<k+1<<": ";
		for(int i=0;i<tam;i++){
		cout<<array2[i];
		}
		cout<<endl;
		
	
}
}
	
	
int main(int argc, char **argv)
{
	
	int x=0;
	
	cin>>x;
	
	traslator(x);
	
	
	return 0;
}

