#include <iostream>
#include <fstream>
#include <cmath>


int main(){

  std::ifstream fp_in("A-large.in");
  std::ofstream fp_out("A-large.out");
  int T;
  fp_in>>T;
  
  long int N, K;
  long int result;
  int count = 1;
  while (fp_in>>N>>K){
    result = (K+1)%(static_cast<long int>(pow(2,N)));
    
    fp_out<<"Case #"<<count<<": ";
    if (result==0) fp_out<<"ON"<<std::endl;
    else fp_out<<"OFF"<<std::endl;
    count++;
  }
  fp_in.close();
  fp_out.close();


}
