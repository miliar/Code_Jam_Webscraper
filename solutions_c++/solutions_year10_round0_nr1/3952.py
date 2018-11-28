#include <cstdio>
#include <iostream>

using namespace std;

unsigned int t, n, k;

int main()
{
	FILE* reader = fopen("A-large.in", "r");
	FILE* printer = fopen("A-large.out", "w");

	fscanf(reader, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		fscanf(reader, "%d %d", &n, &k);
		k = k % (1 << n);
		bool mego = (k + 1 == (1 << n));
		fprintf(printer, "Case #%d: ", i);
		fprintf(printer, mego ? "ON\n" : "OFF\n", i);
	}

	fclose(printer);
	fclose(reader);
}
