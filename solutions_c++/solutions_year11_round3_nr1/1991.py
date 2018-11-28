#include <iostream>
#include <fstream>

using namespace std;

int main (int argc, char const* argv[])
{
   ifstream inFile(argv[1],ios::in);
   ofstream outFile(argv[2],ios::out);
   
   int T;
   inFile >> T;
   
   for (unsigned int i = 0; i < T; i += 1)
   {
      outFile << "Case #" << i+1 << ": "<<endl;
      int R,C;
      inFile >> R >> C;
      string* str;
      str = new string[R];
      for(int j = 0 ; j < R ; ++j){
         inFile >> str[j];
      }
      bool flag = true;
      for(int j = 0 ; j < R-1 ; ++j){
         for(int k = 0 ; k < C-1 ; ++k){
            cout<<k<<endl;
               if(str[j][k] == '#'){
//                  cout<<j<<k<<str[j][k+1]<<str[j+1][k]<<str[j+1][k+1]<<endl;
                  if(str[j][k+1] == '#' && str[j+1][k] == '#' && str[j+1][k+1] == '#'){
                     str[j][k] = '/';
                     str[j][k+1] = '\\';
                     str[j+1][k] = '\\';
                     str[j+1][k+1] = '/';
//                     cout<<j<<k<<str[j][k+1]<<str[j+1][k]<<str[j+1][k+1]<<endl;
                  }          
               }
         }
      }
         for(int j = 0; j < R ; ++j){
            for(int k = 0 ; k < C ; ++k){
               if(str[j][k] == '#') flag = false;
            }
         }
         if(flag){
            for(int j = 0 ; j < R ; ++j){
               outFile<<str[j]<<endl;
            }
         }else{
            outFile << "Impossible" << endl;
         }
   }
   return 0;
}
