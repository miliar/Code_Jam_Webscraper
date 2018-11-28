#include <stdio.h>
#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

int main(){
    
    ifstream in("a.in");
    ofstream out("a.out");  
    char ch;
    int t,n,win[101][101];
    double wp[101][101],owp[101],oowp[101],rpi;
    
    in >> t;
    for(int i=0;i<t;i++){
       in >> n;
       for(int j=0;j<n;j++){
         for(int k=0;k<n;k++){
                in >> ch;
                if (ch == '1'){
                   win[j][k] = 1;
                }
                else if (ch =='0'){
                   win[j][k] = 0;  
                }
                else
                    win[j][k] = -1;
         }      
       }
       
       for(int j=0;j<n;j++){
         for(int h=0;h<n;h++){
         int a = 0;
         int b = 0;      
         
         for(int k=0;k<n;k++){
                if (k != h){
                if (win[j][k] == 1){
                   b++;
                   a++;
                   }
                else if (win[j][k] == 0){
                   b++;
                }
                }
         }  
         wp[j][h] = (double)a / (double)b ;    
         }
       }
       
       for(int j=0;j<n;j++){
         double a = 0;
         int b = 0;      
         for(int k=0;k<n;k++){
                if (win[j][k] != -1){
                   b++;
                   a += wp[k][j];
                }
         }  
         if (b>0) 
            owp[j] = (double)a / (double)b ; 
         else   
            owp[j] = 0;    
       }
       
       for(int j=0;j<n;j++){
         double a = 0;
         int b = 0;      
         for(int k=0;k<n;k++){
                if (win[j][k] != -1){
                   b++;
                   a += owp[k];
                }
         }  
         if (b>0) 
            oowp[j] = (double)a / (double)b ;    
         else 
            oowp[j] = 0;
       }
       out << "Case #" << i+1<<':'<<endl;
       for(int j=0;j<n;j++){
         rpi = (double)(0.25 * wp[j][j] + 0.50 * owp[j] + 0.25 * oowp[j]);
         out << rpi <<endl;
       }
       
       
    }
    
    system("pause");
    return 0;
}
