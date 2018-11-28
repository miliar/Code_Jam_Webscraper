#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main (int argc, char const* argv[])
{
   ifstream inFile(argv[1],ios::in);
   ofstream outFile(argv[2],ios::out);
   
   int T;
   inFile >> T ;
   
   for(int i = 0 ; i < T ; ++i){
//      cout<<"Case #"<<i+1<<": "<<endl;
      outFile<<"Case #"<<i+1<<": "<<endl;
//   Case #1:
      int N;
      inFile >> N;
      
      float* wp;
      float* owp;
      float* oowp;
      
      int* num;
      int* win; 
      
      wp = new float[N];
      owp = new float[N];
      oowp = new float[N];
      
      num = new int[N];
      win = new int[N];
      
      string str[N];
      
      for (int j = 0; j < N; ++j){
         inFile>>str[j];
      }
      
      for(int j = 0 ; j < N ; ++j){
         num[j] = 0;
         win[j] = 0;
         for(int k = 0 ; k < N ; ++k){
            if(str[j][k] == '1'){
               num[j]++;
               win[j]++;
            }else if(str[j][k] == '0'){
               num[j]++;
            }
         }
      }

      for(int j = 0 ; j < N ; ++j){
         wp[j] = float(win[j])/float(num[j]);
      }
      for(int j = 0 ; j < N ; ++j){
         owp[j] = 0;
         for(int k = 0; k < N ; ++k){
            if(str[j][k] != '.'){
               if(str[j][k] == '1'){
                  owp[j] += float(win[k])/float((num[k]-1));
               }else{
                  owp[j] += float(win[k]-1)/float(num[k]-1);
               }
            }
         }
         owp[j] /= num[j];
      }
      for(int j = 0 ; j < N ; ++j){
         oowp[j] = 0;
         for(int k = 0 ; k < N ; ++k){
            if(str[j][k] != '.'){
               oowp[j] += owp[k];
            }
         }
         oowp[j] /= num[j];
      }
      for(int j = 0 ; j < N ; ++j ){
//         cout<<0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j]<<endl;
         outFile<<0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j]<<endl;
      }
      delete wp;
      delete owp;
      delete oowp;
      delete num;
      delete win;
   }
   return 0;
}
