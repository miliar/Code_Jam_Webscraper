#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef ll ret_t;

class Solver {
public:
    ret_t solve(int runs, int cap, vector<int> g) {
        int n = g.size();
        //for (int i = 0; i < n; ++i)
        //cerr<<' '<<g[i];
        //cerr<<endl;
        ll s = 0;
        for (int i = 0; i < n; ++i)
            s += g[i];
        if (s <= cap) {
            return ((ll)runs) * s;
        }
        vector<ll> earns(n, -1);
        vector<int> rounds(n, -1);
        int r = 0;
        ll earn = 0;
        int pos = 0;
        earns[0] = 0;
        rounds[0] = 0;
        while (r < runs) {
            ++r;
            //cerr<<"Round "<<r<<":\t";
            int riders = 0;
            while (riders + g[pos] <= cap) {
                //cerr<<'+'<<g[pos];
                riders += g[pos];
                earn += g[pos];
                ++pos;
                if (pos >= n)
                    pos -= n;
            }
            //cerr<<endl;
            if (earns[pos] >= 0)
                break;
            earns[pos] = earn;
            rounds[pos] = r;
        }
        if (r == runs)
            return earn;
        int cycleruns = r - rounds[pos];
        ll cycleearn = earn - earns[pos];
        int todo = runs - rounds[pos];
        int cycles = todo / cycleruns;
        todo = todo % cycleruns;
        cerr<<"Head:\t"<<rounds[pos]<<endl
            <<"Cycle:\t"<<cycles<<"x "<<cycleruns<<endl
            <<"Tail:\t"<<todo<<endl;
        ll ret = earns[pos] + cycles * cycleearn;
        for (int i = 0; i < n; ++i) {
            if (rounds[i] == rounds[pos] + todo) {
                ret += earns[i] - earns[pos];
                break;
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
        int R, k, n;
        {
            stringstream A(s);
            A >> R >> k >> n;
        }
        vector<int> g(n);
        getline(cin, s);
        stringstream A(s);
        for (int i = 0; i < n; ++i) {
            A >> g[i];
        }
        ret_t ret = solver.solve(R, k, g);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
