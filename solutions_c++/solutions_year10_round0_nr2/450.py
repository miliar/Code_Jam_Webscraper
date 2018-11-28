// NOTE: Requires a public domain Big Integer library from http://mattmccutchen.net/bigint/
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <string>
#include "BigIntegerLibrary.hh"

using namespace std;

BigUnsigned abs(const BigInteger &X)
{
    if (X.getSign() == BigInteger::negative)
        return (-X).getMagnitude();
    return X.getMagnitude();
}

istream &operator>>(istream &S, BigInteger &V)
{
    string s;
    int c;
    while (isspace((c=S.get()))) ;
    while (c=='-' || c=='+' || isdigit(c)) {
	s.append(1, c);
        c = S.get();
    }
    V = stringToBigInteger(s);
    return S;
}

static BigInteger Solve(const vector<BigInteger> &V)
{
    BigUnsigned T = abs(V[1] - V[0]);
    for (size_t i=2; i<V.size(); ++i)
	T = gcd(abs(V[i] - V[i-1]), T);
    BigInteger Y = (-V[0]) % T;
    while (Y < 0)
        Y += T;
    Y %= T;
    return Y;
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
    for (size_t TestCase=1; TestCase<=NumTestCases; ++TestCase) {
        unsigned int N;
	Input >> N;
	vector<BigInteger> V(N);
	for (unsigned int i=0; i<N; ++i)
	    Input >> V[i];
	cout << "Case #" << TestCase << ": " << Solve(V) << endl;
    }
}
