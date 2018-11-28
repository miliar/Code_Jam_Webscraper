#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

struct p{
    int a, b, c;
    bool surp;
};

vector<vector<p> > v(31, vector<p> (100));
vector<int> it(31);

int ab(int a) {
    if(a < 0) return a*-1;
    else return a;
}

int main() {
    ifstream fin ("a.in");
    ofstream fout ("a.out");    
    
    for(int a = 0; a <= 10; ++a) {
        for(int b = 0; b <= 10; ++b) {
            for(int c = 0; c <= 10; ++c) {
                if(a < b or b < c or a < c) continue;
                if(ab(a - b) <= 2 and ab(a-c) <= 2 and ab(b - c) <= 2) {
                    v[a + b + c][it[a + b + c]].a = a; v[a + b + c][it[a + b + c]].b = b; v[a + b + c][it[a + b + c]].c = c;
                    if(ab(a - b) == 2 or ab(a-c) == 2 or ab(b - c) == 2) v[a + b + c][it[a + b + c]].surp = true;
                    ++it[a + b + c];
                }
            }
        }
    }
    int n;
    fin >> n;
    for(int i = 0; i < n; ++i) {
        int a,b,c;
        fin >> a >> b >> c;
        vector<int>r(a);
        int total = a;
        vector<pair<bool,bool> > pa(a);
        for(int ii = 0; ii < a; ++ii) fin >> r[ii];
        int sur = 0, nsur = 0;
        for(int ii = 0; ii < a; ++ii) {
            for(int j = 0; j < it[r[ii]]; ++j) {
                if(v[r[ii]][j].a >= c or v[r[ii]][j].b >= c or v[r[ii]][j].c >= c){
                    if(v[r[ii]][j].surp) pa[ii].first = true;
                    else pa[ii].second = true;
                }
            }
            if(pa[ii].first and !pa[ii].second) ++sur;
            else if(!pa[ii].first && pa[ii].second) ++nsur;
            else if(!pa[ii].first && !pa[ii].second) total--;
        }
        a = total;
        int nada = a - sur - nsur;
        if(b <= sur) fout << "Case #" << i+1 << ": " << a + b - sur << endl;
        else {
            b -= sur;
            if(b <= nada) fout << "Case #" << i+1 << ": " << a << endl;
            else {
                b -= nada;
                if(nsur < b) nsur = b;
                fout << "Case #" << i+1 << ": " << nada + sur + (nsur - b) << endl;
            }
        }
    }
}
