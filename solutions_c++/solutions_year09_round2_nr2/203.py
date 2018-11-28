#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef string ret_t;

class Solver {
public:
    ret_t solve(string num) {
        string nextnum = num;
        next_permutation(nextnum.begin(), nextnum.end());
        string numsort = num;
        sort(numsort.begin(), numsort.end());
        bool desc = true;
        for (int i = 1; i < num.size(); ++i) {
            if (num[i-1] < num[i]) {
                desc = false;
                break;
            }
        }
        if (desc) {
            if (nextnum > num) cerr<<"Incorrect desc!"<<endl;
            //cerr<<"Add zero"<<endl;
            int i = 0;
            while (numsort[i] == '0') ++i;
            string ret(1, numsort[i]);
            numsort[i] = '0';
            sort(numsort.begin(), numsort.end());
            ret += numsort;
            return ret;
        }
        char c;
        int i = num.size() - 2;
        while (num[i] >= num[i+1])
            --i;
        int j = i + 1;
        for (int k = j + 1; k < num.size(); ++k)
            if (num[k] > num[i] && num[k] < num[j])
                j = k;
        //cerr<<i<<"<->"<<j<<endl;
        c = num[i];
        num[i] = num[j];
        num[j] = c;
        sort(num.begin() + i + 1, num.end());
        if (num != nextnum) cerr<<"Incorrect num!"<<endl;
        return num;
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
        string a, b, c;
        {
            stringstream A(s);
            A >> a;
        }
        ret_t ret = solver.solve(a);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
