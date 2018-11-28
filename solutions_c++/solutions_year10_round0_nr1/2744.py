#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;



int main()
{
ifstream archivo;
ofstream salida;
archivo.open("input2.txt");
salida.open("outputlargo.txt");

int t;
long double aux;
int n,resto, k;
string ans="OFF";
archivo>>t; 

for(int i=0;i<t;i++) //para cada caso
{
archivo>>n>>k;

k=k+1;
aux=(pow(2.00,n));   
resto=fmod(k,aux);

if (resto==0) {ans="ON"; } 
else {ans="OFF";}



salida<<"Case #"<<i+1<<": "<<ans<<endl;  //OUTPUT
}
 

cout<<"listo"<<endl;
    
int p;
cin>>p;
return 0;
}






