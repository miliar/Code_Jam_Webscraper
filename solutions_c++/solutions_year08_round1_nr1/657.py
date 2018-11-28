#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;

int comp(const void *p1, const void *p2)
{
	int *a = (int*)p1;
	int *b = (int*)p2;

	return *a - *b;
}


int main(int argc, char *argv[])
{
	int T;
	int n;
	int64_t *a;
	int64_t *b;
	int64_t produtoEscalar;
	int64_t tmp;
	ifstream in("A-large.in");
	in >> T;
	for (int caso=1 ; caso <= T ; caso++)
	{
		in >> n;
		a = new int64_t[n];
		b = new int64_t[n];
		produtoEscalar = INT_MAX;
		for (int i=0 ; i<n ; i++)
			in >> a[i];
		for (int i=0 ; i<n ; i++)
			in >> b[i];
		qsort(a, n, sizeof(int64_t), comp);
		qsort(b, n, sizeof(int64_t), comp);

		tmp = 0;
		for (int i=0 ; i<n ; i++)
		{
			tmp += a[i]*b[n-i-1];
		}

		cout << "Case #" << caso << ": " << tmp << endl;
		delete a;
		delete b;
	}
	return 0;
}
