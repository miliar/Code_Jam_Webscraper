#include <iostream>
#include <fstream>
using namespace std;

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}

int main (int argc, char * const argv[]) {
    ifstream input(argv[1]);
	ofstream output("output.txt");
	int T, N;
	input >> T;
	int *a, *b;
	for (int i = 0; i < T; i++) {
		input >> N;
		a = new int[N];
		b = new int[N];
		for (int j = 0; j < N; j++) {
			input >> a[j];
			b[j] = a[j];
		}
		qsort(&b[0], N, sizeof(int), compare);
		float sortedCount = 0.0;
		for (int j = 0; j < N; j++) {
			sortedCount+=(a[j] != b[j]);
		}
		output.setf(ios::fixed);
		output << "Case #" << i+1 << ": " << sortedCount << endl;
		sortedCount = 0;
	}
    return 0;
}

