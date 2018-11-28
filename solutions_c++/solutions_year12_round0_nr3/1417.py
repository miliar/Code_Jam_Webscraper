#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef int ret_t;

class Solver {
public:
    ret_t solve(int A, int B) {
	int pw = 1;
	while (pw < B)
	    pw *= 10;
	pw /= 10;
	int ret = 0;
	for (int n = A; n < B; ++n) {
	    int m = n;
	    while (true) {
		//cerr << m << endl;
		m = (m % 10) * pw + m / 10;
		if (m == n)
		    break;
		//cerr << n << '\t' << m << '\t';
		if (m > n && m <= B) {
		    ++ret;
		    //cerr << "in";
		}
		//cerr << endl;
	    }
	}
	//cerr << "Returning" << endl;
	return ret;
    }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
	int a, b;
        {
            stringstream A(s);
            A >> a >> b;
        }
        ret_t ret = solver.solve(a, b);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
