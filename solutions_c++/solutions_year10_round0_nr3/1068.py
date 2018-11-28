#include <deque>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>

using namespace std;

double SimulateRollerCoaster(unsigned long R, unsigned long k, deque<unsigned long> &Q)
{
    double S = 0.0;

    while (R-- > 0) {
        unsigned int N = Q.size();
	double Ppl = 0.0;
        while (Ppl + Q.front() <= k && N > 0) {
            Ppl += Q.front();
            Q.push_back(Q.front());
            Q.pop_front();
            --N;
        }
	S += Ppl;
    }

    return S;
}

int main(int argc, char *argv[])
{
    if (argc < 2) {
        cerr << "Usage: " << argv[0] << " input_file\n";
	return EXIT_FAILURE;
    }

    ifstream Input(argv[1]);
    if (!Input) {
        cerr << "Unable to open " << argv[1] << " for reading!\n";
	return EXIT_FAILURE;
    }

    size_t NumTestCases;
    Input >> NumTestCases;
    for (size_t i=1; i<=NumTestCases; ++i) {
        unsigned long R, k;
	unsigned int N;
	Input >> R >> k >> N;
        deque<unsigned long> Q;
	for (unsigned int j=0; j<N; ++j) {
	    unsigned long G;
	    Input >> G;
	    Q.push_back(G);
	}
	double S = SimulateRollerCoaster(R, k, Q);
	cout << "Case #" << i << ": " << fixed << setprecision(0) << S << "\n";
    }
}
