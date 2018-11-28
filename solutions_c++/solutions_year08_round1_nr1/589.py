#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<ctype.h>
using namespace std;
int main(int argc, char **argv){
    char salida[25];
    int i, veces, n, j, z=1;
    long long arreglo1[900], arreglo2[900], tmp, respuesta1, respuesta2;
    freopen(argv[1], "r", stdin);
    for(i=0; i<strlen(argv[1])-2; i++){
        salida[i]=argv[1][i];   
    }
    salida[i++]='o';
    salida[i++]='u';
    salida[i++]='t';
    salida[i++]=0;
    freopen(salida, "w", stdout);
    /**************************************************/
    cin>>veces;
    while(veces--){
           cin>>n;
           for(i=0; i<n; i++)cin>>arreglo1[i];
           for(i=0; i<n; i++)cin>>arreglo2[i];
           for(i=n-1; i>=0; i--){
                for(j=1; j<=i; j++){
                    if(arreglo1[j-1]>arreglo1[j]){
                        tmp=arreglo1[j];
                        arreglo1[j]=arreglo1[j-1];
                        arreglo1[j-1]=tmp;   
                    }   
                } 
           }
    
           for(i=n-1; i>=0; i--){
                for(j=1; j<=i; j++){
                    if(arreglo2[j-1]>arreglo2[j]){
                        tmp=arreglo2[j];
                        arreglo2[j]=arreglo2[j-1];
                        arreglo2[j-1]=tmp;   
                    }   
                } 
           }
           respuesta1=respuesta2=0;
           for(i=0, j=n-1; i<n; i++, j--){
                respuesta1+=arreglo1[i]*arreglo2[j];
                respuesta2+=arreglo1[j]*arreglo2[i]; 
           }
           if(respuesta1<respuesta2){
                cout<<"Case #";
                cout<<z++;
                cout<<": ";
                cout<<respuesta2<<endl;
            }else{
                cout<<"Case #";
                cout<<z++;
                cout<<": ";
                cout<<respuesta1<<endl;
            }
    }
    return 0;
}
