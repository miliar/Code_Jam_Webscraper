/* 
 * File:   main.cpp
 * Author: joao
 *
 * Created on 8 de Maio de 2010, 14:08
 */

#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

/*
 */
 int total = 0;
 queue<int> fila;

 int ride(int k){
     //cout << "i'm riding " << endl;
     //copia fila
     queue<int> proxima_fila = fila;
     int remaing = k;
     
     int next_group = fila.front();
     
     //enquanto o proximo grupo ainda cabe
     while(next_group <= remaing){

         //actualiza lugares disponiveis
         remaing -= next_group;
         
         fila.pop();
         proxima_fila.pop();
         proxima_fila.push(next_group);

         if(!fila.empty()){
            next_group = fila.front();
         }
         else break;
         if(next_group > remaing) break;
         
         
     }
     
     fila = proxima_fila;

     return k-remaing;
 }
 int main(int argc, char** argv) {

    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        int R,k,N;
        cin >> R >> k >> N;
        
        for(int l=1; l<=N; l++){
            int temp;
            cin >> temp; 
            fila.push(temp);
        }
       // cout << "read everything" << endl;
        
        while(R > 0){
            total += ride(k);
            R--;
        }
        cout << "Case #" << i << ": " << total << endl;
        total = 0;
        while(!fila.empty()) fila.pop();
    }

    return (EXIT_SUCCESS);
}

