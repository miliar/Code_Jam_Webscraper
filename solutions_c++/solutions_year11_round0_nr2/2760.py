#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <map>
using namespace std;

int main(int argc, char** argv)
{
    fstream in, out;
    in.open("b.in", ios_base::in);
    out.open("b.out", ios_base::out);
    int T;
    in >> T;
    for (int t = 0; t < T; t++) {
        int C, D, N;
        map< pair<char, char>, char > to;
        map< pair<char, char>, bool > opp;
        in >> C;
        for (int i = 0; i < C; i++) {
            string s;
            in >> s;
            pair<char, char> p1(s[0], s[1]);
            pair<char, char> p2(s[1], s[0]);
            to[p1] = s[2];
            to[p2] = s[2];
        }
        in >> D;
        for (int i = 0; i < D; i++) {
            string s;
            in >> s;
            pair<char, char> p1(s[0], s[1]);
            pair<char, char> p2(s[1], s[0]);
            opp[p1] = true;
            opp[p2] = true;
        }
        in >> N;
        list<char> L;
        for (int i = 0; i < N; i++) {
            char c;
            in >> c;
            if (L.empty()) {
                L.push_back(c);
                continue;
            }

            // Combination
            char l = L.back();
            pair<char, char> p(c, l);
            if (to.find(p) != to.end()) {
                L.pop_back();
                L.push_back(to[p]);
                continue;
            }

            // Opposite
            bool ex = false;
            for (list<char>::iterator it = L.begin(); it != L.end(); it++) {
                pair<char, char> p(c, *it);
                if (opp.find(p) != opp.end()) {
                    L.clear();
                    ex = true;
                    break;
                }
            }
            if (ex) continue;

            // Else
            L.push_back(c);
        }
        out << "Case #" << t + 1 << ": [";
        bool fst = true;
        for (list<char>::iterator it = L.begin(); it != L.end(); it++) {
            if (!fst) {
                out << ", ";
            }
            fst = false;
            out << *it;
        }
        out << "]" << endl;
    }
    in.close();
    out.close();
	return 0;
}

