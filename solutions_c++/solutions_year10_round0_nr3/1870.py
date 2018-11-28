#include <iostream>
#include <string>
#include <stdio.h>
#include <queue>
#include <vector>
#include <list>
#include <set>

#define FOR(a,b,c) for ( int a = b ; a < c ; a++ )
#define FORM(it,v) for( typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it )

using namespace std;

typedef unsigned long long ULL;

ULL r,k,n,tmp;
list<ULL> grupos;
list<ULL> cola;
set< list<ULL> > mark;

int main(){
   int casos;
   cin >> casos;
   FOR(caso,1,casos+1){
      grupos.clear();
      cola.clear();
      mark.clear();
      
      cin >> r >> k >> n;
      FOR(i,0,n){
         cin >> tmp;
         grupos.push_back(tmp);
         cola.push_back(tmp);
      }

      ULL respuesta = 0;
      FOR(i,0,r){

         if ( mark.find(cola) != mark.end()){
            //cerr << "Repetido " << endl;
            /*FORM(it,cola){
               cout << (*it) << " ";
            }cout << endl;*/
            
            list<ULL> inicio = cola;
            int tamCiclo = 0;
            ULL gananciaCiclo = 0;
            bool salir = false;
            while(i < r && !salir){
               if (cola  == inicio && tamCiclo != 0){
                  //cerr << "Tan Ciclo " << tamCiclo << " gananciaCiclo " << gananciaCiclo << " Se suma " << (r-(i-tamCiclo))/tamCiclo << " Con resto " << ((r-(i-tamCiclo))%tamCiclo) << endl;
                  respuesta += ((r-(i-tamCiclo))/tamCiclo)*gananciaCiclo;
                  int resto = ((r-(i-tamCiclo))%tamCiclo);
                  FOR(j,0,resto){
                     int gruposMontados = 0;
                     ULL montados = 0;
                     
                     while(cola.front() + montados <= k && gruposMontados < n){
                        montados += cola.front();
                        cola.push_back(cola.front());
                        cola.pop_front();
                        ++gruposMontados;
                     }
                     respuesta += montados;
                  }
                  salir = true;
                  i=r;
               }else{
                  int gruposMontados = 0;
                  ULL montados = 0;
                  while(cola.front() + montados <= k && gruposMontados < n){
                     montados += cola.front();
                     cola.push_back(cola.front());
                     cola.pop_front();
                     ++gruposMontados;
                  }
                  ++tamCiclo;
                  gananciaCiclo += montados;
               }
               ++i;
            }
            if (!salir){
               respuesta += gananciaCiclo;
            }
         }else{
         
            mark.insert(cola);
            ULL montados = 0;
            int gruposMontados = 0;
            while(cola.front() + montados <= k && gruposMontados < n){
               montados += cola.front();
               cola.push_back(cola.front());
               cola.pop_front();
               ++gruposMontados;
            }
            respuesta += montados;
         }
      }

      cout << "Case #" << (caso) << ": " << respuesta << endl;
      
   }
   fflush(stdout);
   return 0;
}
