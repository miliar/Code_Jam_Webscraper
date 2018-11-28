#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int abs(int a){
    int res;
    a>=0 ? res = a: res = -a;
    return res;
}

int main() {
    ifstream entrada("A-large.in");
    ofstream salida("A-large.out");
    int Casos;
    entrada >> Casos;
    for(int caso=1; caso<=Casos; caso++){
        int buttons;
        entrada >> buttons;
        char actual;
        entrada >> actual;
        int uo,ub,seguidos;
        int res;
        entrada >> res;
        res--;
      //  cout << abs(-1) << endl;
        if(actual == 'O') {uo = res+1;ub=1;} else {ub = res+1;uo=1;}
        res++;
        seguidos = res;
        //cout << "1: uo,ub,seguidos, actual, res: " << uo << ", " << ub << ", " << seguidos << ", " << actual << ", " << res << endl;
        for(int i=1;i<buttons; i++){
            char prox;
            int aux;
            entrada >> prox;
            if(prox == actual){
                entrada >> aux;
                if(actual == 'O') {
                    res += abs(aux-uo)+1;
                    seguidos += abs(aux-uo)+1;
                    uo=aux;
         //   cout << i+1 << ": uo,ub,seguidos, actual, res" << uo << ", " << ub << ", " << seguidos << ", " << actual << ", " << res << endl;cout << i+1 << ": uo,ub,seguidos, actual, res" << uo << ", " << ub << ", " << seguidos << ", " << actual << ", " << res << endl;

                }else{
                    res+= abs(aux-ub)+1;
                    seguidos += abs(aux-ub)+1;
                    ub=aux;
         //   cout << i+1 << ": uo,ub,seguidos, actual, res" << uo << ", " << ub << ", " << seguidos << ", " << actual << ", " << res << endl;

                }
            } else {
                actual = prox;
                entrada >> aux;
                if(actual=='O'){
                    int pasos = abs(aux-uo) - seguidos;
                    if(pasos>=0){
                    res += pasos + 1;
                    seguidos = pasos+1;
                    }else{seguidos = 1;res++;}
                    uo = aux;
        //    cout << i+1 << ": uo,ub,seguidos, actual, res" << uo << ", " << ub << ", " << seguidos << ", " << actual << ", " << res << endl;
                }else{
                    int pasos = abs(aux-ub) - seguidos;
                    if(pasos>=0)
                    {res += pasos+1;
                    seguidos = pasos+1;}
                    else{seguidos=1;res++;}
                    ub = aux;
        //    cout << i+1 << ": uo,ub,seguidos, actual, res" << uo << ", " << ub << ", " << seguidos << ", " << actual << ", " << res << endl;
                }
            }

        }
        salida << "Case #" << caso << ": " << res << endl;
    }
    return 0;
}
