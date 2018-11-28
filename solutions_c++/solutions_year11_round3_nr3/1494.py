#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv){
   ifstream inFile(argv[1],ios::in);
   ofstream outFile(argv[2],ios::out);
   
   int T;
   inFile >> T;
   
   for (unsigned int i = 0; i < T; i += 1)
   {
      outFile << "Case #" << i+1 << ": ";
      int N, L, H;
      inFile >> N >> L >> H;
      int ans = -1;
      int* n = new int[N];
      for(int j = 0 ; j < N ; j++){
         inFile >> n[j];
      }
      
      bool flag = false;
      for(int j = L ; j <= H ; j++){
         int k;
         for(k = 0 ; k < N ; k++){
            if(j < n[k]){
               if(n[k]%j) { 
                  break; 
               }else{
                  if(k == N-1){
                     flag = true;
                     ans = j;
                  }
               }
            }else{
               if(j%n[k]) {
                  break;
               }else{
                  if(k == N-1){
                     flag = true;
                     ans = j;
                  }
               }
            }    
         }
         if(flag) break;
      }
      if(flag){
         outFile << ans << endl;
      }else{
         outFile << "NO" << endl;
      }
   }

}
