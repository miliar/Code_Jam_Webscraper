#include <stdio.h>
#include <stdint.h>
#include <algorithm>

namespace {

template <unsigned F>
unsigned factor_n (unsigned V)
{
	unsigned n = 0;
	while (V % F == 0) {
		V /= F;
		++n;
	}
	return n;
}

bool work (unsigned long long N, unsigned PD, unsigned PG)
{
	if (PD == 0)
		return (PG != 100);
	if (PD == 100)
		return (PG != 0);
	if (PG == 0)
		return false;
	if (PG == 100)
		return false;
	// Get smallest possible D
	unsigned twos = 2 - std::min(2u,factor_n<2>(PD));
	unsigned fives = 2 - std::min(2u,factor_n<5>(PD));
	unsigned D = 1;
	if (twos) {
		D *= 2;
		if (twos == 2)
			D *= 2;
	}
	if (fives) {
		D *= 5;
		if (fives == 2)
			D *= 5;
	}
	if (D > N)
		return false;
	// PD OK. Check if PG possible.
	// D PD <= G PG
	// D    <= G
	return true;
}

}

int main ()
{
	unsigned T;
	scanf ("%u", &T);
	for (unsigned i=1; i<=T; ++i) {
		unsigned long long N;
		unsigned PD, PG;
		scanf ("%llu%u%u", &N, &PD, &PG);
		printf ("Case #%u: %s\n", i, work (N, PD, PG) ? "Possible" : "Broken");
	}
	return 0;
}
