#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
  ifstream myfile("A-large.in");

  if (myfile.is_open())
  {
     int T,N,K;
     myfile >> T;
     
     for (int i=0; i<T; ++i) {
         string mo;
         myfile >> N;
         myfile >> K;
         int x = 1 << N;
         int on = x - 1;
         if ( (K == on) || (K % x == on) ) mo = "ON";
         else mo = "OFF";
         cout << "Case #" << i+1 << ": " << mo << endl; 
     } 
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}


