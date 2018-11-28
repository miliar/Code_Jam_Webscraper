#include <stdio.h>

struct Requirement {
	unsigned pos;
	char color;
};

static unsigned find_dest (const Requirement *req, unsigned j, unsigned N, char color)
{
	for (; j<N; ++j)
		if (req[j].color == color)
			return req[j].pos;
	return 0;
}

static unsigned work (void)
{
	unsigned N;
	Requirement req[120];
	scanf ("%u", &N);
	for (unsigned i=0; i<N; ++i)
		scanf (" %c%u", &req[i].color, &req[i].pos);

	unsigned sec = 0; // Current second.
	unsigned poso = 1, posb = 1;
	unsigned k = 0;
	unsigned desto = find_dest (req, 0, N, 'O');
	unsigned destb = find_dest (req, 0, N, 'B');

	while (k < N) {
		bool pushed = false;
		if (desto) {
			if (poso != desto) {
				if (poso > desto)
					--poso;
				else
					++poso;
			}
			else if (req[k].color == 'O') {
				pushed = true;
				++k;
				desto = find_dest (req, k, N, 'O');
			}
		}
		if (destb) {
			if (posb != destb) {
				if (posb > destb)
					--posb;
				else
					++posb;
			}
			else if (!pushed && (req[k].color == 'B')) {
				pushed = true;
				++k;
				destb = find_dest (req, k, N, 'B');
			}
		}
		++sec;
	}
	return sec;
}

int main ()
{
	unsigned T;
	scanf ("%u", &T);
	for (unsigned j=1; j<=T; ++j) {
		printf ("Case #%u: %u\n", j, work ());
	}
	return 0;
}
