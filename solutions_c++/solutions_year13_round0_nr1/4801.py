#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <utility>

using namespace std;

inline int win(map<char, int>& stat){
    int res = 0;
    if (stat['X'] == 4 || ((stat['X'] == 3) && (stat['T'] == 1))){
        res = 1;
    }
    else if (stat['O'] == 4 || ((stat['O'] == 3) && (stat['T'] == 1))){
        res = 2;
    }else if (stat['.'] != 0) res = 3;
    return res;
}
int calcstat(vector<map<char, int> >& v)
{
   int res = 0;
   for (int i = 0; i < v.size(); i++){
       int w = win(v[i]);
       if ((1 == w) || (2 == w)) return w;
       if (3 == w) res = w;
   }
   return res;
}
int main(int argc, char** argv)
{
    istream* is = &cin;
    ostream* os = &cout;

    if (argc >= 2) is = new ifstream(argv[1]);
    if (argc == 3) os = new ofstream(argv[2]);
    
    int T;
    *is >> T;
    vector<vector<char> > G(4,vector<char>(4, '.'));

    for (int i = 1; i <= T; i++){
        vector<map<char, int> > rowstat(4);
        vector<map<char, int> > colstat(4);
        vector<map<char, int> > diagstat(2);

        for (int r = 0; r < 4; r++){
            for (int c = 0; c < 4; c++){
                char p;
                *is >> p;
                G[r][c] = p;
                rowstat[r][p] += 1;
                colstat[c][p] += 1;
                if (r == c){
                    diagstat[0][p] += 1;
                }
                if (r +c == 3){
                    diagstat[1][p] += 1;
                }
            }
        }
        int res = 0;
        res = calcstat(rowstat);
        string out;
        if ((1 == res) || (2 == res)){
            out += (1 == res) ? "X" : "O";
            out += " won";
        }else{
            int cc = calcstat(colstat);
            if ((1 == cc) || (2 == cc)){
                out += (1 == cc) ? "X" : "O";
                out += " won";
            }else{
                int dc = calcstat(diagstat);
                if ((1 == dc) || (2 == dc)){
                    out += (1 == dc) ? "X" : "O";
                    out += " won";
                }else{
                    if ( res == 3) out = "Game has not completed";
                    else out = "Draw";
                }
            }
        }
        *os << "Case #" << i <<": "<< out << endl;
    }


    if (is != &cin) delete is;
    os->flush();
    if (os != &cout) delete os;
    return 0;
}
