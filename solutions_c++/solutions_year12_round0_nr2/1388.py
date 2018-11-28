#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef int ret_t;

class Solver {
public:
    ret_t solve(int n, int S, int p, vector<int> t) {
	int ret = 0;
	vector<bool> done(n, false);
	vector<int> nonsur(n);
	vector<int> sur(n);
	for (int i = 0; i < n; ++i) {
	    int tar = t[i] / 3;
	    switch (t[i] % 3) {
	    case 0:
		nonsur[i] = tar;
		sur[i] = tar + 1;
		break;
	    case 1:
		nonsur[i] = tar + 1;
		sur[i] = tar + 1;
		break;
	    case 2:
		nonsur[i] = tar + 1;
		sur[i] = tar + 2;
		break;
	    }
	    if (t[i] < 2 || t[i] > 28)
		sur[i] = -9;
	    //cerr << nonsur[i] << '\t' << sur[i] << endl;
	}
	for (int i = 0; i < n && S > 0; ++i) {
	    if (sur[i] >= p && nonsur[i] < p) {
		++ret;
		done[i] = true;
		--S;
	    }
	}
	for (int i = 0; i < n; ++i){
	    if (!done[i]) {
		done[i] = true;
		if (nonsur[i] >= p)
		    ++ret;
	    }
	}
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
	int n, S, p;
	vector<int> t;
        {
            stringstream A(s);
            A >> n >> S >> p;
	    t = vector<int>(n, 0);
	    for (int i = 0; i < n; ++i)
		A >> t[i];
        }
	//cerr << n << '\t' << S << '\t' << p << endl;
        ret_t ret = solver.solve(n, S, p, t);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
