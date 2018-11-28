#include <iostream>
#include <stdio.h>
#define TAM 100

using namespace std;

int googlers[TAM];

void encontrar(int caso,int num_googlers,int num_sorprendete,int mayorequalto){

   int aux=0,contador=0;

   for(int i=0;i<num_googlers;i++){

       aux=googlers[i]/3;

       if(aux>=mayorequalto){
         contador++;
       }
       else{

            if(googlers[i]-3*aux==0 && aux+1>=mayorequalto && num_sorprendete>0 && aux!=0){
                contador++;
                num_sorprendete--;
            }
            if(googlers[i]-3*aux==1 && aux+1>=mayorequalto){
                contador++;
            }
            if(googlers[i]-3*aux==2){

                if(aux+1>=mayorequalto){
                   contador++;
                }
                if(aux+2>=mayorequalto && num_sorprendete>0) {
                    contador++;
                    num_sorprendete--;
                }
            }
        }

     }

   cout<<"Case #"<<caso<<": "<<contador<<endl;

}


int main()
{
    int num_casos=0,num_googlers=0,num_sorprendete=0,mayorequalto=0;

    scanf("%d",&num_casos);

    for(int i=0; i<num_casos; i++)
    {

        num_googlers=0;
        num_sorprendete=0;
        mayorequalto=0;

        cin>>num_googlers;
        cin>>num_sorprendete;
        cin>>mayorequalto;

        for(int j=0;j<num_googlers;j++){

           cin>>googlers[j];

        }

//        cout<<"caso "<<i+1<<" : "<<num_googlers<<" "<<num_sorprendete<<" "<<mayorequalto<<" ";
//
//        for(int j=0;j<num_googlers;j++){
//
//           cout<<googlers[j]<<" ";
//
//        }
//        cout<<endl;

        encontrar(i+1,num_googlers,num_sorprendete,mayorequalto);

    }
    return 0;
}
