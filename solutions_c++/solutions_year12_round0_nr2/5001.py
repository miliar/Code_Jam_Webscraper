#include<iostream>

#include<fstream>
#include<string.h>
int dividir (int *array, int inicio, int fin){
  int izq;
  int der;
  int pibote;
  int temp;
  pibote = array[inicio];
  izq = inicio;
  der = fin;
  while (izq < der){
   while (array[der] > pibote){
  der--;
   }
    while ((izq < der) && (array[izq] <= pibote)){
      izq++;
    }
 

  if(izq < der){
     temp= array[izq];
      array[izq] = array[der];
      array[der] = temp;
    }
  }


 temp = array[der];
 array[der] = array[inicio];
  array[inicio] = temp;
 return der;
}
void quicksort( int *array, int inicio, int fin)
{
  int pivote;
  if(inicio < fin){
    pivote = dividir(array, inicio, fin );
    quicksort( array, inicio, pivote - 1 );
    quicksort( array, pivote + 1, fin );
  }
}


using namespace std;
int tc,t[102], n,s,p, m, cont;

int main()
	{
ifstream myfile("B-large.in");
while(myfile.peek() != EOF)
{myfile>>tc;
	for(m=1;m<=tc;m++)
		{cont=0;
		myfile>>n;
		myfile>>s;
		myfile>>p;
		for(int x=0;x<n;x++)
		{myfile>>t[x];
if(s>0)
if(t[x]>=p)
{
if(t[x]==(p*3)-4 || t[x]==(p*3)-3)
{cont++; s--;}}

if(t[x]>=(p*3)-2 && t[x]>=p)
cont++;
}
	
if(myfile.peek()==EOF)
  return 0;
cout<<"Case #"<<m<<": "<<cont<<endl;}
return 0;}}
