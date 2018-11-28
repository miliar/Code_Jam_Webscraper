#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <map>
#include <iostream>

using namespace std;

char buffor[1000];

int main(){
 int N;
 scanf("%d", &N); //ilosc danych wejsciowych
 for(int n = 0; n < N; n++){
            int S = 0; //ilosc serwerów
            int Q = 0; //ilosc zapytan
            vector<string> Serwers; //tablica serwerów
            map<string, int> WskSerw; //mapa wskaŸników stringów na adresy
            scanf("%d\n", &S);
            for(int i = 0; i < S; i++){
                  //scanf("%s", buffor);
                  string a;
                  getline(cin, a);
                //  printf("->%s\n", a.c_str());
                  Serwers.push_back(a);  
                  WskSerw[a]=i;
            }
            //przetwarzanie danych w trybie on-line
            scanf("%d\n", &Q);
            bool used[S];
            int notused = S;
            int steps = 0;
            memset(used, 0, sizeof(used)); 
            for(int i = 0; i < Q; i++){
                    //scanf("%s", buffor);
                    string a;
                    getline(cin, a);
                    if(!used[WskSerw[a]]){
                                                              if(notused == 1){
                                                                          notused = S;
                                                                           memset(used, 0, sizeof(used));
                                                             steps++;           
                                                             }
                                          notused--;
                                          }   
                    used[WskSerw[a]] = 1;     
    //                for(int i = 0; i <S; i++) printf("%d ", used[i]);
    //                printf("\n");
            }
            printf("Case #%d: %d\n", n+1, steps);
                   
 }   
 //system("pause");
}
