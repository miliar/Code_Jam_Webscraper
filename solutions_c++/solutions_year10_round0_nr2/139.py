#include <cstdio>
#include <cassert>
#include <gmp.h> // GNU GMP library (http://gmplib.org)
#include <algorithm>

using namespace std;

struct ZZ {
  ZZ(long x = 0)                        {mpz_init_set_si(data, x);}
  ~ZZ()                                 {mpz_clear(data);}
  ZZ(const ZZ& z)                       {mpz_init_set(data, z.data);}
  void operator=(const ZZ& z)           {mpz_set(data, z.data);}
  bool operator<(const ZZ& z) const     {return mpz_cmp(data, z.data) < 0;}
  bool operator==(const ZZ& z) const    {return mpz_cmp(data, z.data) == 0;}
  void read(FILE* file)                 {mpz_inp_str(data, file, 10);}
  void write(FILE* file)                {mpz_out_str(file, 10, data);}

  void sub(const ZZ& z1, const ZZ& z2)  {mpz_sub(data, z1.data, z2.data);}
  void mul(const ZZ& z1, const ZZ& z2)  {mpz_mul(data, z1.data, z2.data);}
  void cdiv(const ZZ& z1, const ZZ& z2) {mpz_cdiv_q(data, z1.data, z2.data);}
  void gcd(const ZZ& z1, const ZZ& z2)  {mpz_gcd(data, z1.data, z2.data);}

  mpz_t data;
};

const int MAX_EVENTS = 1005;

ZZ events[MAX_EVENTS];

int main() {
  int nCases, nEvents;

  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%d", &nEvents);
    for (int i = 0; i < nEvents; i++) {
      events[i].read(stdin);
    }

    sort(events, events + nEvents);
    nEvents = unique(events, events + nEvents) - events;
    assert(nEvents >= 2);

    ZZ deltaEvents, gcdDelta = 0;
    for (int i = 1; i < nEvents; i++) {
      deltaEvents.sub(events[i], events[0]);
      gcdDelta.gcd(gcdDelta, deltaEvents);
    }

    ZZ optAnniv;
    optAnniv.cdiv(events[0], gcdDelta);
    optAnniv.mul(optAnniv, gcdDelta);
    optAnniv.sub(optAnniv, events[0]);

    printf("Case #%i: ", iCase);
    optAnniv.write(stdout);
    printf("\n");
  }
  return 0;
}
