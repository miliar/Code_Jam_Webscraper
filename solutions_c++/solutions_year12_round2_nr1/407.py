#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef vector<double> ret_t;

class Solver {
public:
    ret_t solve(int n, vector<int> J) {
	vector<int> J2(J);
	int sum = 0;
	for (int i = 0; i < n; ++i)
	    sum += J[i];
	//double low = (double)sum * 2 / n;
	int lo = 0;
	int hi = 200;
	do {
	    int mid = (lo + hi) / 2;
	    int votesReq = 0;
	    for (int i = 0; i < n; ++i)
		if (J[i] < mid)
		    votesReq += mid - J[i];
	    if (votesReq <= sum)
		lo = mid;
	    if (votesReq >= sum)
		hi = mid;
	} while (lo < hi - 1);
	int votesReq = 0;
	int numLow = 0;
	for (int i = 0; i < n; ++i)
	    if (J[i] <= lo)
		votesReq += lo - J[i], ++numLow;
	double low = lo + (double)(sum - votesReq) / numLow;
	cerr << " low = " << low << endl;

	vector<double> ret(n);
	for (int i = 0; i < n; ++i)
	    ret[i] = J[i] > low ? 0 : (double)100 * (low - J[i]) / sum;
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
        int n;
	vector<int> J;
        {
            stringstream A(s);
            A >> n;
	    J = vector<int>(n);
	    for (int i = 0; i < n; ++i)
		A >> J[i];
        }
        ret_t ret = solver.solve(n, J);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
        cout << "Case #" << no << ":";
	for (int i = 0; i < ret.size(); ++i)
	    cout << " " << fixed << setprecision(7) << ret[i];
	cout << endl;
    }
    return 0;
}
