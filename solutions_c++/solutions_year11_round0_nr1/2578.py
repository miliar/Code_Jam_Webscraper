#include <iostream>
#include <cmath>
#include <math.h>
#include <fstream>

using namespace std;


int main(){
    
    ifstream myf;
    myf.open("input.txt");
    
    int T;
    myf>>T;
    
    ofstream myfile;
    myfile.open("result.txt");
    
    for (int it = 0; it < T; it++){
        int n;
        myf>>n;
        
        char *R = new char[n];
        int *B = new int[n];
        
        for (int i = 0; i < n; i++) myf>>R[i]>>B[i];
        
        int c1 = 1, c2 = 1;
        int t1 = 0, t2 = 0;
        
        while(t1 < n && R[t1] != 'B'){t1++;}
        while(t2 < n && R[t2] != 'O'){ t2++;}
        
        int t = 0, tn = 0;
        
        int count = 0;
        
        while (t < n){
              count++;
              if (R[t] == 'B' && B[t] == c1){
                     tn=t+1;
                     t1++;
                     while(t1 < n && R[t1] != 'B'){t1++;}
                     
                     }
              else if (B[t1] > c1){
                   c1++;
                   }
              else if (B[t1] < c1) c1--;
              
              
              if (R[t] == 'O' && B[t] == c2){
              
                     tn = t+1;
                     t2++;
                     while(t2 < n && R[t2] != 'O'){ t2++;}
                     }
              else if (B[t2] > c2){
                   c2++;
                   }
              else if (B[t2] < c2) c2--;
                     
              
                     
              t = tn;
              
              
              
        } 
        
        myfile<<"Case #"<<it+1<<": "<<count<<endl;       
    
    }
    
    myfile.close();
    return 0;
}
