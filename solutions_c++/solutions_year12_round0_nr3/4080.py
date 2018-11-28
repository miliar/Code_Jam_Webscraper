#include <iostream>
#include <stdio.h>
using namespace std;

struct arreg{

    int a;
    int b;

}arreglo[2000000];

int serepite(int numero,int otro,int cant){
  int band=0;
  if(cant==0){
       arreglo[0].a=numero;
       arreglo[0].b=otro;
  }
  else{
     for(int i=0;i<cant;i++){
         if(numero==arreglo[i].a && otro==arreglo[i].b){
            band=1;
         }
     }
     if(band==0){
         arreglo[cant].a=numero;
         arreglo[cant].b=otro;
    }
  }
  return band;
}

int pot(int indice){
   int a=1;
   while(indice>0){
      a=a*10;
      indice--;
   }
   return a;
}

int numDigitos( int numero ){
    int cuentaDigitos = 0;
    while ( numero ) {
               ++cuentaDigitos;
               numero /= 10;
    }
    return cuentaDigitos;
}

void encontrar(int caso,int numero1,int numero2){

    int contador=0,cant_cifras=0,numero_cambiado=0;
    cant_cifras=numDigitos(numero1);
    for(int i=1;i<cant_cifras;i++)
    {
        for(int numero=numero1;numero<numero2;numero++){
            numero_cambiado=(numero%pot(i))*pot(cant_cifras-i) + (numero/pot(i));
            if(numero<numero_cambiado && numero_cambiado<=numero2){
               if(serepite(numero,numero_cambiado,contador)){
                  contador--;
               }
               contador++;
            }
        }
    }
    cout<<"Case #"<<caso<<": "<<contador<<endl;
}

int main()
{
    int num_casos=0,numero1,numero2;
    scanf("%d",&num_casos);
    for(int i=0; i<num_casos; i++)
    {
        cin>>numero1;
        cin>>numero2;
        encontrar(i+1,numero1,numero2);
    }
    return 0;
}
