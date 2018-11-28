#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cassert>

#include <memory.h>
using namespace std;

const char iname[] = "A-small.in";
const char oname[] = "A-small.out";

const int MAXN = 1024;

double P[MAXN];
string F[MAXN];

double DF(int n, set <string>& features) {
    if (P[n] == 0)  return 1.0;
    if (features.find(F[n]) != features.end())
        return DF(2 * n, features) * P[n];
    return DF(2 * n + 1, features) * P[n];
}

int getdouble(string& str, int i, double &dbl) {
    dbl = 0;
    for (; str[i] >= '0' && str[i] <= '9'; ++ i)
        dbl = dbl * 10 + double(str[i] - '0');

    assert(str[i] == '.');
    i ++;
    for (double ten = 1.0 / 10; str[i] >= '0' && str[i] <= '9'; ++ i, ten /= 10.0)
        dbl += ten * double(str[i] - '0');
    return i - 1;
}

int getfeature(string &str, int i, string &feature) {
    feature = "";
    for (; 'a' <= str[i] && str[i] <= 'z'; ++ i)
        feature += str[i];
    return i - 1;
}

int main(void) {
    ifstream in(iname);
    ofstream out(oname);
    int runs;

    in >> runs;
    for (int iruns = 0; iruns < runs; ++ iruns) {
        for (int i = 0; i < MAXN; ++ i)
            P[i] = 0, F[i] = "";

        int cntlines;
        in >> cntlines;
        string line, lines;

        in.get();

        for (int i = 0; i < cntlines; ++ i)
            getline(in, line),
            lines += line;

        stack < pair <int, int> > stk;
        for (size_t i = 0; i < lines.size(); ++ i) {
            if (lines[i] == ' ')
                continue ;
            if (lines[i] == '(') {
                if (stk.size())
                    stk.push(make_pair(stk.top().first * 2 + stk.top().second, 0));
                else
                    stk.push(make_pair(1, 0));
                continue ;
            }
            if (lines[i] == ')') {
                stk.pop();
                if (stk.size())
                    stk.top().second ++;
                continue ;
            }
            // cout << "Nod: " << stk.top().first << "\n";

            if ('0' <= lines[i] && lines[i] <= '9')
                i = getdouble(lines, i, P[stk.top().first]);
            //    cout << P[stk.top().first] << "\n";
            else if ('a' <= lines[i] && lines[i] <= 'z')
                i = getfeature(lines, i, F[stk.top().first]);
            //    cout << F[stk.top().first] << "\n";
            else
                assert(false);
        }

    //    for (int i = 1; i <= 15; ++ i) if (P[i])
    //        cout << i << " " << P[i] << " " << F[i] << "\n";
    //    cout << "\n";

        out << "Case #" << (iruns + 1) << ":\n";
        int animals;
        for (in >> animals; animals --; ) {
            string name, feature;
            int n;
            set <string> features;
            in >> name >> n;
            for (int i = 0; i < n; ++ i)
                in >> feature,
                features.insert(feature);

            out << DF(1, features) << "\n";
        }
    }
    in.close();
    out.close();
    return 0;
}
