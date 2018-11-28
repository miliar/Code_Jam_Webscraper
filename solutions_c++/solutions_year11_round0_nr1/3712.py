#include<iostream>
#include<stdio.h>

#define maximo 200

using namespace std;

int main () {
    char cor[maximo];
    int botao[maximo], iazul, ilaranja, posazul, poslaranja, t, n, i, caso;
    
    scanf(" %d", &t);
    for (caso = 1; caso <= t; caso++) {
        scanf(" %d", &n);
        for (i = 0; i < n; i++) {
              scanf(" %c %d", &cor[i], &botao[i]);
        }
        
        posazul = poslaranja = 1;
        for (iazul = 0; iazul < n && cor[iazul] != 'B'; iazul++);
        for (ilaranja = 0; ilaranja < n && cor[ilaranja] != 'O'; ilaranja++);
        int segundos, atual;
        for (segundos = 0, atual = 0; iazul < n || ilaranja < n; segundos++) {
              if (cor[atual] == 'B') {
                 //aperta
                 if (botao[atual] == posazul) {
                    atual++;
                    for (iazul++; iazul < n && cor[iazul] != 'B'; iazul++);
                    //cout<<"azul apertou e foi para o indice: "<<iazul<<endl;
                 }
                 //ou anda
                 else {
                      if (posazul > botao[atual])
                          posazul--;
                      else
                          posazul++;
                 }
                 if (ilaranja < n) {
                    if (poslaranja > botao[ilaranja])
                       poslaranja--;
                    else if (poslaranja < botao[ilaranja])
                       poslaranja++;
                 }
              }
              else { // é laranja o atual
                 //aperta
                 if (botao[atual] == poslaranja) {
                    atual++;
                    for (ilaranja++; ilaranja < n && cor[ilaranja] != 'O'; ilaranja++);
                    //cout<<"laranja apertou e foi para o indice: "<<ilaranja<<endl;
                 }
                 //ou anda
                 else {
                      if (poslaranja > botao[atual])
                          poslaranja--;
                      else
                          poslaranja++;
                 }
                 if (iazul < n) {
                    if (posazul > botao[iazul])
                       posazul--;
                    else if (posazul < botao[iazul])
                       posazul++;
                 }
              }
              //cout<<"pos azul: "<<posazul<<endl;
              //cout<<"pos laranja: "<<poslaranja<<endl;
              //cout<<"atual: "<<atual<<" botao atual: "<<botao[atual]<<endl<<endl;
        }
        printf("Case #%d: %d\n", caso, segundos);
    }
    return 0;
}
