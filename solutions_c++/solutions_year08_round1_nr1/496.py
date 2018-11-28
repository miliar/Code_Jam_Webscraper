#include <stdio.h>
#include <string.h>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

int comparar(const void *arg1, const void *arg2)
{
 if(*(int *)arg1 < *(int *)arg2) return -1;
   else if(*(int *)arg1 > *(int *)arg2) return 1;
   else return 0;
}

int main()
{

ifstream entrada;
ofstream salida;

int N;
char cadena[20];
int *x,*y;
int tam;
int j;
long int prod;

entrada.open("A-small.in");
salida.open("salida2.txt");

entrada>>N;
entrada.getline(cadena,20);



for(int i=0;i<N;i++)
{
   entrada>>tam;
   entrada.getline(cadena,20);
   x=new int [tam];
   y=new int [tam];
   for(j=0;j<tam-1;j++)
   {
      entrada.getline(cadena,20,' ');
      x[j]=atoi(cadena); 
   }
   entrada.getline(cadena,20);;
   x[j]=atoi(cadena); 
    for(j=0;j<tam-1;j++)
   {
      entrada.getline(cadena,20,' ');
      y[j]=atoi(cadena); 
   }
   entrada.getline(cadena,20);
   y[j]=atoi(cadena); 
   
   
   qsort(x, tam, sizeof (int), comparar);
   qsort(y, tam, sizeof (int), comparar);
   
   prod=0;
   for(j=0;j<tam;j++){
     prod+=x[j]*y[tam-j-1];
   }
   salida<<"Case #"<<i+1<<": "<<prod<<endl;
   
   delete x;
   delete y;
}


entrada.close();
salida.close();
}
