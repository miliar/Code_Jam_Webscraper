#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <cmath>
#include <boost/foreach.hpp>

#include <gmp.h>
#define foreach BOOST_FOREACH
using namespace std;
// Using gmp, (ubuntu libgmp3)




int main()
{
  int ncases;
  cin >> ncases;
  mpz_t dates[1000];
  mpz_t gcd;
  mpz_init(gcd);
  mpz_t mod, res;
  mpz_init(mod);
  mpz_init(res);
  mpz_t off;
  mpz_init(off);
  for (int i=0; i<1000; ++i)
    mpz_init(dates[i]);
  for (int i=0; i<ncases; ++i)
  {
    unsigned ndates;
    cin >> ndates;
    for (unsigned d=0; d<ndates;++d)
    {
      std::string v;
      cin >> v;
      gmp_sscanf(v.c_str(), "%Zd", dates[d]);
    }
    //mpz_gcd(res, a, b)
    //mpz_sub(res, a, b)
    if (mpz_cmp(dates[0], dates[1])>0)
      mpz_sub(gcd, dates[0], dates[1]);
    else
      mpz_sub(gcd, dates[1], dates[0]);
    mpz_t tmp, tmp2;
    mpz_init(tmp); mpz_init(tmp2);
    for (unsigned d=2; d<ndates;++d)
    {
      if (mpz_cmp(dates[0], dates[d])>0)
	mpz_sub(tmp, dates[0], dates[d]);
      else
	mpz_sub(tmp, dates[d], dates[0]);
      mpz_gcd(tmp2, tmp, gcd);
      mpz_set(gcd, tmp2);
    }
    //now we got the gcd, get the offset from any of the dates
    mpz_mod(mod, dates[0], gcd);
    if (mpz_cmp_ui(mod, 0) == 0)
    {
      mpz_set(res, mod);
    }
    else
    {
      mpz_set(off, gcd);
      // res =  gcd - d0 % gcd
      //gmp_printf("gcd %Zd mod %Zd\n", gcd, mod);
      mpz_sub(res, off, mod);
    }
    gmp_printf("Case #%d: %Zd\n", i+1, res);
  }
}
