#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv){
   ifstream inFile(argv[1],ios::in);
   ofstream outFile(argv[2],ios::out);
   
   int T;
   inFile >> T;
   
   for (unsigned int i = 0; i < T; i += 1)
   {
      cout << "Case #" << i << ": ";
      outFile << "Case #" << i+1 << ": ";
      int N;
      inFile >> N;
      int temp = 0;
      int min = 2147483647;
      int sum = 0;
      for (unsigned int j = 0; j < N; j += 1)
      {
         int in;
         inFile >> in;
         temp = temp ^ in;
         if(in < min) min = in;
         sum += in;
      }
      if(temp != 0){
         cout << "NO" << endl;
         outFile << "NO" << endl;
      }else{
         cout << sum - min << endl;
         outFile << sum - min << endl;
      }
   }
}



