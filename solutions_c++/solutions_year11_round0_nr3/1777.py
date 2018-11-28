#include <iostream>
#include <list>
const int MAX = 1000;

long long XOR(long long a, long long b) {
  return (a&~b)^(b&~a);
}

int main() {

  int T;
  std::cin>>T;
  for(int i = 1; i <= T; i++) {
    int N, sum = 0, temp;
    std::list<long long> Clist;
    std::list<long long>::iterator it;
    std::cin>>N;
    for(int j = 0; j < N; j++) {
      std::cin>>temp;
      sum = XOR(sum, temp);
      Clist.push_back(temp);
    }

    Clist.sort();
    int j;
    long long total = 0, C[MAX] = {0,};
    long long  sum_XOR1 = 0, sum_XOR2 = 0;
    for(j=0, it=Clist.begin(); it!=Clist.end(); j++, it++) {
      C[j] =  *it;
      sum_XOR2 = XOR(sum_XOR2, C[j]);
      total += *it;
    }

    if ( sum != 0 ) std::cout<<"Case #"<<i<<": "<<"NO"<<std::endl;
    
    else {
      long long sum1 = C[0], sum2 = total - C[0];
      sum_XOR1 = C[0]; sum_XOR2 = XOR(C[0], sum_XOR2);
      
      for(int k = 1; k < N - 1; k++) {
	if ( sum_XOR1 == sum_XOR2 ) break;
	else {
	  sum1 += C[k]; sum2 -= C[k];
	  sum_XOR1 = XOR(sum_XOR1, C[k]);
	  sum_XOR2 = XOR(sum_XOR2, C[k]);
	}
      }
      
      //  if ( sum1 > sum2 ) 
      //	std::cout<<"Case #"<<i<<": "<<sum1<<std::endl;
      //      else
        std::cout<<"Case #"<<i<<": "<<sum2<<std::endl;
      
    }
  }


  return 0;
}
