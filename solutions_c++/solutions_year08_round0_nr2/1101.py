#include <stdio.h>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

int main()
{

ifstream entrada;
ofstream salida;

int N;
int turnaround;
int NA,NB;
int TA,TB;
char cadena[100];
int *salidaA,*llegadaA,*salidaB,*llegadaB;
char hora[3],min[3];
int dif,kdel;

entrada.open("B-large.in");
salida.open("salida_large.txt");

entrada>>N;
entrada.getline(cadena,100);

for(int i=0;i<N;i++)
{
    entrada>>turnaround;
    entrada.getline(cadena,100);
    entrada>>NA>>NB;
    entrada.getline(cadena,100);
    salidaA=new int [NA];
    llegadaA=new int [NA];
    salidaB=new int [NB];
    llegadaB=new int [NB];
    
    for(int j=0;j<NA;j++){
        entrada.getline(hora,100,':');
        entrada.getline(min,100,' ');
        salidaA[j]=atoi(hora)*60 + atoi(min);
        entrada.getline(hora,100,':');
        entrada.getline(min,100);
        llegadaA[j]=atoi(hora)*60 + atoi(min);
    }
    for(int j=0;j<NB;j++){
        entrada.getline(hora,100,':');
        entrada.getline(min,100,' ');
        salidaB[j]=atoi(hora)*60 + atoi(min);
        entrada.getline(hora,100,':');
        entrada.getline(min,100);
        llegadaB[j]=atoi(hora)*60 + atoi(min);
    }   
    
    TA=NA;
    TB=NB;
    
    for(int j=0;j<NA;j++){
       dif=1440;
        for(int k=0;k<NB;k++){
            if(llegadaA[j]+turnaround <= salidaB[k] && salidaB[k] - (llegadaA[j]+turnaround) < dif){
               dif=salidaB[k] - (llegadaA[j]+turnaround);
               kdel=k;
            }
        }
        if(dif!=1440){
            salidaB[kdel]=0;
            TB--;
        }
    }
    
    for(int j=0;j<NB;j++){
        dif=1440;
        for(int k=0;k<NA;k++){
            if(llegadaB[j]+turnaround <= salidaA[k] && salidaA[k] - (llegadaB[j]+turnaround) < dif){
               dif=salidaA[k] - (llegadaB[j]+turnaround);
               kdel=k;
            }
        }
        if(dif!=1440){
            salidaA[kdel]=0;
            TA--;
        }
    }
    
    salida<<"Case #"<<i+1<<": "<<TA<<" "<<TB<<endl;
    
    delete salidaA;
    delete llegadaA;
    delete salidaB;
    delete llegadaB;
}
entrada.close();
salida.close();
}
