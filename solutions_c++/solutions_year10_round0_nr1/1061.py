#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;
						    
inline bool Snap(unsigned int N, unsigned long K)
{
    const unsigned long Mask = (1UL << N) - 1UL;
    return (K & Mask) == Mask;
}

int main(int argc, char *argv[])
{
    if (argc < 2) {
        cerr << "Usage: " << argv[0] << " input_file\n";
	return EXIT_FAILURE;
    }

    ifstream Input(argv[1]);
    if (!Input) {
        cerr << "Unable to open " << argv[0] << " for reading!\n";
	return EXIT_FAILURE;
    }

    size_t NumTestCases;
    Input >> NumTestCases;
    for (size_t i=1; i<=NumTestCases; ++i) {
        unsigned int N;
	unsigned long K;
	Input >> N >> K;
	const bool B = Snap(N, K);
	cout << "Case #" << i << ": " << (B ? "ON" : "OFF") << "\n";
    }
}
