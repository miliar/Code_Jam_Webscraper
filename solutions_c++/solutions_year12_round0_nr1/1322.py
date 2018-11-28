#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef string ret_t;

class Solver {
public:
    string dec;
    void make_dec() {
	dec = string(256, '?');
	string goog("yeq ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv");
	string   en("aoz our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up");
	for (int i = 0; i < goog.size(); ++i) {
	    if (dec[goog[i]] == '?' || dec[goog[i]] == en[i])
		dec[goog[i]] = en[i];
	    else {
		cerr << "Input is inconsistent: "
		     << goog[i] << " can be decoded as " << dec[goog[i]]
		     << " or as " << en[i] << endl;
	    }
	}
	dec['z'] = 'q';
    }
    ret_t solve(string goog) {
        string ret(goog);
	for (int i = 0; i < goog.size(); ++i)
	    ret[i] = dec[goog[i]];
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
    Solver solver;
    solver.make_dec();
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        // *** get input ***
        getline(cin, s);
        /*string a;
        {
            stringstream A(s);
            A >> a;
	    }*/
        ret_t ret = solver.solve(s);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
