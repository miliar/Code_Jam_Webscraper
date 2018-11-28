#include<iostream>
#include<fstream>
#include<cmath> 
using namespace std; 
int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out"); 
    int T, N, K, R; 
    while(fin >> T){
       for(R = 1; R <= T; R++){
          fin >> N >> K;
          N = (int)pow((double)2, N);
          K %= N;
          fout << "Case #" << R << ": ";  
          if(K == N - 1) fout << "ON\n";
          else           fout << "OFF\n"; 
       }
       break; 
    }
    return 0;
} 
