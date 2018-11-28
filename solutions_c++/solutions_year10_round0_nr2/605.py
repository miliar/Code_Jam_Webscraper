/* 
Google Codejam 2010
B. Fair Warning

C++ Solution by:
 Marco Chiesi
 chiesi@gmail.com
*/

#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
// Using C++ Big integer library by Matt McCutchen
// http://mattmccutchen.net/bigint/
#include "bigint/BigIntegerLibrary.hh"
 
using namespace std;

/**
 * Class for a single instance of the problem
 */
class Instance {
    private:
        BigInteger solution;
        int N;
        BigInteger *t;

    public:
	void readInput(istream &in) {
        in >> N;
        t = new BigInteger[N];
		for (int i = 0; i < N ; i++) {
            string num;
            in >> num;
            t[i] = stringToBigInteger(num);
        }
	}
	
	BigInteger GCD(BigInteger a, BigInteger b) {
        while( 1 ) {
            a = a % b;
    		if( a == 0 ) {
    			return b;
            }
    		b = b % a;
            if( b == 0 ) {
    			return a;
            }
        }
    }

	void solve() {
        BigInteger gcd_diff = max(t[0]-t[1],t[1]-t[0]);
        BigInteger min_num = t[0];
        for (int i = 0; i + 1 < N; i++) {
            if (t[i+1] < min_num) {
                min_num = t[i+1];
            }
            for (int j = i + 1; j < N; j++) {
                BigInteger curr_diff = max(t[i]-t[j],t[j]-t[i]);
                if (curr_diff != 0) {
                    if (gcd_diff != 0) {
                        gcd_diff = GCD(gcd_diff, curr_diff);
                    }
                    else {
                        gcd_diff = curr_diff;
                    }
                }
            }
        }
    	solution = gcd_diff > 1 && (min_num % gcd_diff != 0) ? gcd_diff - (min_num % gcd_diff) : 0;
	}

	string getSolution() {
    	stringstream ss;
        ss << solution;
		return ss.str();
	}
};

/**
 * Class for a problem
 */
class Problem {
	private:
        Instance *instances;
	    int cases;
	
	public:
	void readInput(istream &in) {
		in >> cases;
		instances = new Instance[cases];
		for (int i = 0; i < cases; i++) {
			instances[i].readInput(in);
		}
	}
	
	void solve() {
		for (int i = 0; i < cases; i++) {
			instances[i].solve();
		}
	}
	
	void writeOutput(ostream &out) {
		for (int i = 0; i < cases; i++) {
			out << "Case #" << i+1 << ": " << instances[i].getSolution() << endl;
		}
	}
};

/**
 * Main function
 */
int main(int argc, char *argv[]) {
    istream *in;
    ostream *out;
    if (argc > 1) {
        in = new fstream(argv[1], fstream::in);
    }
    else {
        in = &cin;
    }
    if (argc > 2) {
        out = new fstream(argv[2], fstream::out);
    }
    else {
        out = &cout;
    }
    Problem *problem = new Problem();
    problem->readInput(*in);
    problem->solve();
    problem->writeOutput(*out);
    return 0;
}
