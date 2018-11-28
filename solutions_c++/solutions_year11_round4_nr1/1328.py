#include <iostream>
#include <stdlib.h>
using namespace std;
struct way{
    long double dis;
    long double vel;
};
way camino[10000];

long double X,Vi,Vf;
int t,N;

long double Vdif;
long double res;
long double sob;
int compa(const void *a,const void *b){
    return (int)(((way*)a)->vel - ((way*)b)->vel);
}
void resuelve(){
    int ini,fin;
    long double vel;
    cin >> X >> Vi >> Vf >> t >> N;
    for(int i=0;i<N;i++){
        cin >> ini >> fin >> vel;
        camino[i].dis = fin-ini;
        X -= camino[i].dis;
        camino[i].vel = vel+Vi;        
    }
    Vdif = Vf -Vi;
    res = 0.0;
    if( X>0){
        camino[N].dis = X;
        camino[N].vel = Vi;
        N++;
    }
    qsort(camino,N,sizeof(way),compa);
    sob = (long double)t;
    long double velCor;
    long double tiempo;
    long double dis;
    for(int i=0;i<N;i++){
        if(  sob > 0){
            velCor = camino[i].vel + Vdif;
            tiempo = camino[i].dis / velCor;

            if( tiempo <= sob){
                res += tiempo;
                sob -= tiempo;
            }else{
                dis = velCor*sob;
                camino[i].dis -= dis;
                res +=sob;
                i--; 
                sob = -1.0;
           }    
        }else{
            tiempo = camino[i].dis / camino[i].vel;
            res += tiempo;
        }
    }
    cout.precision(9);
    cout << fixed <<res;

}
int main(){
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        cout << "Case #"<< i << ": ";
        resuelve();
        cout << endl;
    }
    return 0;
}
