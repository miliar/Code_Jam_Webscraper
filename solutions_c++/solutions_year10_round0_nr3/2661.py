#include <iostream>
#include <fstream>
using namespace std;



int main()
{
ifstream archivo;
archivo.open("input2.txt");

int t,r,k,n, ans;
int grupos[1000];
archivo>>t;

int contador=0, aux=0, cantidadgrupos=0;

for(int i=0;i<t;i++) //para cada caso
{

   ans=0;
   archivo>>r>>k>>n;
   for (int j=0;j<=n;j++) //guardamos los grupos
      {
      
      if (j==n) {grupos[j]=0;} //el ultimo es cero
      else { archivo>>grupos[j]; }
      
      }
   
   for (int p=0, contador=0  ; p<r  ;  p++) // la cantidad de veces q funciona la montaña rusa
      {
      cantidadgrupos=0;
      aux=0;
      
        
      while ( (   aux+grupos[contador] <= k ) && (grupos[contador]!=0) && cantidadgrupos<n  )
            {
            aux=aux+grupos[contador];  //es la resp en cada vez q se juega
            cantidadgrupos++;
            
            if (contador==n-1) {contador=0; }//if (n==1) {p++;}  }
            else {contador++;}
            
            }
      
      ans=ans+aux; //resp total
      
      }
   
   






cout<<"Case #"<<i+1<<": "<<ans<<endl;  //OUTPUT
}
 

    
    
int p;
cin>>p;
return 0;
}






