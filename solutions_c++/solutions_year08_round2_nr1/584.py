#include <iostream>
#include <vector>
#include <algorithm>


#define IN(x)   {std::cin x;}
#define OUT_(x) {std::cout x;}
#define OUT(x)  {std::cout x << std::endl;}
#define LOG_(x) {std::cerr x;}
#define LOG(x)  {std::cerr x << std::endl;}


int main(int argc, char** argv){
  unsigned int N;
  IN(>> N);

  for (unsigned int i = 1; i <= N; i++) {
    // input
    unsigned int n;
    unsigned long int A, B, C, D, x0, y0, M;
    IN(>> n >> A >> B >> C >> D >> x0 >> y0 >> M);

    std::vector<unsigned long int> X, Y;
    X.push_back(x0);
    Y.push_back(y0);
    for (unsigned int i = 0; i < n-1; i++) {
      X.push_back((A * X[i] + B) % M);
      Y.push_back((C * Y[i] + D) % M);
    }
    LOG(<<"# "<< X.size() <<"\t"<< n);
    
#if false
    std::vector<unsigned long int> distinctX, distinctY;
    for (unsigned int i = 0; i < n; i++) {
      LOG(<< X[i] <<"\t"<< Y[i]);
      unsigned int j = 0;
      for (;j < i; j++) {
	if ((X[i] == X[j]) && (Y[i] == Y[j])) break;
      }
      LOG(<<"## "<< i <<"\t"<< j);
      if (i == j) {
	distinctX.push_back(X[i]);
	distinctY.push_back(Y[i]);
      }
    }
#endif

    unsigned long long int ans = 0;
    for (unsigned int k = 0; k < n; k++) {
      for (unsigned int j = 0; j < k; j++) {
	for (unsigned int i = 0; i < j; i++) {
	  LOG(<< i <<"\t"<< j <<"\t"<< k);
	  if (((X[i]+X[j]+X[k]) % 3 == 0) && ((Y[i]+Y[j]+Y[k]) % 3 == 0))
	    ans++;
	}
      }
    }

    // output
    OUT_(<< "Case #" << i << ": ");
    
    // answer
    OUT(<< ans);
  }
  

}
  
