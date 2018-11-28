#include <iostream>
#include <stdlib.h>
#include <fstream>


using namespace std;

int  main(){
     int T,N,L[2][200],O[100],B[100],tmp,step,ll,Ol,Bl,Bll,Oll;
     char c;
     
     ifstream in("1.in");
     ofstream out("1.out");
     
     in >> T;
     
     for (int i = 0;i < T;i++){
         
         in >> N;
         
         O[0] = 0;
         B[0] = 0;
         
         for (int j = 0;j < N;j++){
             in >> c;
             in >> tmp;
             if (c == 'O'){
                L[0][j] = 0;
                L[1][j] = tmp;
                O[++O[0]] = tmp;
             }
             else{
                L[0][j] = 1;
                L[1][j] = tmp;
                B[++B[0]] = tmp;                  
             }
         }
         
         step = 0;
         Ol = 1;
         Bl = 1;
         Oll = 0;
         Bll = 0;
         ll = 0;
         
         while (1){
               
            step++;
            if (L[0][ll] == 0){
               if (Bl < B[Bll+1]){
                  Bl++;
               }
               else if (Bl > B[Bll+1]){
                  Bl--;
               }
               
               if ( Ol < L[1][ll] ){
                  Ol++;
               }
               else if ( Ol > L[1][ll] ){
                  Ol--;
               }
               else if (Ol == L[1][ll]){
                  ll++;
                  Oll++;
               }
            }
            else{
                 
               if (Ol < O[Oll+1]){
                  Ol++;
               }
               else if (Ol > O[Oll+1]){
                  Ol--;
               }
               
               
               if ( Bl < L[1][ll] ){
                  Bl++;
               }
               else if ( Bl > L[1][ll] ){
                  Bl--;
               }
               else if (Bl == L[1][ll]){
                  ll++;
                  Bll++;
               }                
            }
            if (ll == N ) break;
         }
         out <<"Case #"<<i+1<<": "<< step<<endl;
     }
     system("pause");
}
