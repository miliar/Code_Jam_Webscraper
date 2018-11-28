#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
    
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t,i,j,stat,a=1;
    char mat[4][4],x;
    cin>>t;
    while(t--){
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>mat[i][j];
            }
        }
        stat = -1;
        for(i=0;i<4;i++){
            x=mat[i][0];
            if(x == 'T') x = mat[i][1];
            for(j=1;j<4;j++){
                if(x == mat[i][j] || mat[i][j] == 'T');
                else break;
            }
            if(j==4){
                  if(x == 'X') stat = 1;
                  else if(x == 'O') stat = 2;
            }
        }
        for(i=0;i<4;i++){
            x=mat[0][i];
            if(x == 'T') x = mat[1][i];
            for(j=1;j<4;j++){
                if(x == mat[j][i] || mat[j][i] == 'T');
                else break;
            }
            if(j==4){
                  if(x == 'X') stat = 1;
                  else if(x == 'O') stat = 2;
            }
        }
         x=mat[0][0];
         if(x == 'T') x = mat[1][1];
         for(j=1;j<4;j++){
             if(x == mat[j][j] || mat[j][j] == 'T');
             else break;
         }
         if(j==4){
             if(x == 'X') stat = 1;
             else if(x=='O') stat = 2;
         }
         x=mat[0][3];
         if(x == 'T') x = mat[1][2];
         for(j=1;j<4;j++){
             if(x == mat[j][3-j] || mat[j][3-j] == 'T');
             else break;
         }
         if(j==4){
             if(x == 'X') stat = 1;
             else if(x == 'O') stat = 2;
         }
         if(stat == -1){
             for(i=0;i<4;i++){
                 for(j=0;j<4;j++){
                     if(mat[i][j]=='.') stat=4;
                 }
             }
             if(stat==-1) stat = 3;
         }
         cout<<"Case #"<<a<<": ";
         a++;
         switch(stat){
             case 1: cout<<"X won\n";
                     break;
             case 2: cout<<"O won\n";
                     break;
             case 3: cout<<"Draw\n";
                     break;
             case 4: cout<<"Game has not completed\n";
         }
     }
     
}                   
        
                  
