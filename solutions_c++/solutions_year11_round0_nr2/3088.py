#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

char opp[255];
vector<string> comb[255];

int main() {
    ifstream in("B-small-attempt0.in");
    ofstream out("b.out");
    int Z, C, D, N;
    string s;
    string tmp;
    string construct;
    string o;
    in >> Z;
    for(int z = 0; z < Z; z++) {
        for(int i = 'A'; i <= 'Z'; i++) {
            opp[i] = 0;
            comb[i].clear();
        }
        in >> C;
        for(int i = 0; i < C; i++) {
            in >> tmp;
            construct = tmp[1];
            construct += tmp[2];
            comb[tmp[0]].push_back(string(construct));
            construct[0] = tmp[0];        
            comb[tmp[1]].push_back(string(construct));
        }
        in >> D;
        for(int i = 0; i < D; i++) {
            in >> tmp;
            opp[tmp[0]] = tmp[1];
            opp[tmp[1]] = tmp[0];
        }
        in >> D;
        in >> s;
        
        o = s[0];
        int oi = 0;
        bool next;
        for(int i = 1; i < s.size(); i++) {
            next = false;
            //cout << s[i] << endl;
            for(int j = 0; j < comb[s[i]].size() && oi >= 0; j++) {
                if (comb[s[i]][j][0] == o[oi]) {
                    o[oi] = comb[s[i]][j][1];
                    next = true;
                    //cout << "combined to form " << comb[s[i]][j][1] << endl;
                    break;
                }
            }
            if (!next) {
                if (o.find(opp[s[i]]) != string::npos){
                    o = "";
                    oi = -1;
                    //cout << "cleared string" << endl;
                }
                else {
                    o += s[i];
                    oi++;
                    //cout << "appended char" << endl;
                }
            }
            //cout << o << endl << endl;
        }
        out << "Case #" << z + 1 << ": [";
        if (o.size() > 0) {
            for(int i = 0; i < o.size()-1; i++) out << o[i] << ", ";
            out << o[o.size()-1];
        }
        out <<"]" << endl; 
    }
    return 0;
}
