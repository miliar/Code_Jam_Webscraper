#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef string ret_t;

string subtract(string ret, string p) {
    // if result is negative, returns just "-"
    //cerr<<"\t\t"<<ret<<" - "<<p<<endl;
    if (ret == p)
        return "0";
    int sd = ret.size() - p.size();
    if (sd < 0)
        return "-";
    for (int j = 0; j < p.size(); ++j) {
        if (ret[sd + j] >= p[j])
            ret[sd + j] = ret[sd + j] - p[j] + '0';
        else {
            ret[sd + j] = ret[sd + j] + 10 - p[j] + '0';
            int k = sd + j - 1;
            while (k >= 0 && ret[k] == '0') {
                ret[k] = '9';
                --k;
            }
            if (k < 0)
                return "-";
            ret[k]--;
        }
    }
    //cerr<<"\t\t= "<<ret<<endl;
    return ret.substr(ret.find_first_not_of('0'));
}

string rem(string a, string b) {
    //cerr<<'\t'<<a<<" % "<<b<<endl;
    if (b.size() > a.size())
        return a;
    string tmp = a.substr(0, b.size());
    int j = b.size();
    while (true) {
        while (true) {
            string tmp2 = subtract(tmp, b);
            if (tmp2 == "-")
                break;
            tmp = tmp2;
        }
        if (j >= a.size())
            break;
        if (tmp == "0")
            tmp[0] = a[j];
        else
            tmp.push_back(a[j]);
        ++j;
    }
    //cerr<<"\t= "<<tmp<<endl;
    return tmp;
}

string gcd(string a, string b) {
    //cerr<<"GCD of "<<a<<", "<<b<<endl;
    if (a == "0")
        return b;
    if (subtract(a, b) == "-")
        b = rem(b, a);
    while (true) {
        if (b == "0")
            return a;
        a = rem(a, b);
        if (a == "0")
            return b;
        b = rem(b, a);
    }
}

class Solver {
public:
    ret_t solve(vector<string> t) {
        int n = t.size();
        for (int i = 1; i < n; ++i) {
            if (t[i].size() < t[0].size()
                || (t[i].size() == t[0].size() && t[i] < t[0])) {
                swap(t[0], t[i]);
            }
        }
        string g = subtract(t[1], t[0]);
        for (int i = 2; i < n; ++i) {
            g = gcd(g, subtract(t[i], t[0]));
        }
        //cerr<<"Period: "<<g<<endl;
        string rev = rem(t[0], g);
        if (rev == "0")
            return "0";
        return subtract(g, rev);
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
        vector<string> t;
        {
            stringstream A(s);
            A >> n;
            for (int i = 0; i < n; ++i) {
                string tt;
                A >> tt;
                t.push_back(tt);
            }
        }
        ret_t ret = solver.solve(t);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
