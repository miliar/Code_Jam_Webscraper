
#include <iostream>
#include <vector>
#include <algorithm>
#include <gmpxx.h>

mpz_class gcd(const mpz_class& a,const mpz_class& b)
{
  mpz_class c;
  mpz_gcd(c.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());
  return c;
}

int main(int,char**)
{
  int C;
  std::cin >> C;
  for(int n=0;n<C;++n){
    int N;
    std::cin >> N;

    std::vector<mpz_class> t(N);
    for(int i=0;i<N;++i)
      std::cin >> t[i];
    std::swap(t.front(),*std::min_element(t.begin(),t.end()));
    for(auto itr=t.begin()+1;itr!=t.end();++itr)
      *itr -= t.front();

    mpz_class g = t[1];
    for(int i=2;i<N;++i)
      g = gcd(g,t[i]);

    std::cout << "Case #" << (n+1) << ": " << (g-(t.front()%g))%g << std::endl;
  }
  return 0;
}

