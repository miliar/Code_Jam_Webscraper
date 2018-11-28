#include <stdio.h>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

typedef map<string,int> Diccionario;

int buscar(Diccionario& D, char *palabra) {
  Diccionario::iterator iter = D.find(palabra);
  if(iter == D.end()) return 0;
  return iter->second;
}

int main()
{

int N;
int contador;
int nswitch;
int nbusc;
int nqueries;
int *vector;
char *cadena;
int zeros;

Diccionario D[21];

ifstream entrada;
ofstream salida;

entrada.open("A-large.in");
salida.open("salida_large.txt");

entrada>>N;
entrada.getline(cadena,101);

for(int i=0;i<N;i++){
    nswitch=0;
    contador = 0;
    entrada>>nbusc;
    entrada.getline(cadena,101);
    vector=new int [nbusc];
    for(int j=0;j<nbusc;j++){
        entrada.getline(cadena,101);
        D[i][cadena]=contador;
        contador++;
        vector[j]=0;
    }
    entrada>>nqueries;
    entrada.getline(cadena,101);
    for(int j=0;j<nqueries;j++){
        entrada.getline(cadena,101);
        vector[buscar(D[i],cadena)]=1;
        zeros=nbusc;
        for(int k=0;k<nbusc;k++)
             if(vector[k]==1)zeros--;
        if(zeros==0){
             nswitch++;
             for(int k=0;k<nbusc;k++)vector[k]=0;
        }
        vector[buscar(D[i],cadena)]=1;
    }
    salida<<"Case #"<<i+1<<": "<<nswitch<<endl;
    delete vector;
}

entrada.close();
salida.close();
}
