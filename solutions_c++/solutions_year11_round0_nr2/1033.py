#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <string>
#include <cstring>


using namespace std;

#define NMAX 303
#define ZERO(X) memset(X, 0, sizeof(X))

class Problem {
    public:

    long cc, dc, nc;
    string in;

    char re[NMAX];  // magica string
    int cre[NMAX];  // magica count of chars
    int rec;        // magica string length

    bool opposed[NMAX][NMAX];
    char combine[NMAX][NMAX];

    Problem()
        : cc(0), dc(0), nc(0)
    {
        in="";
        magica_clear();
        ZERO(opposed);
        ZERO(combine);
    }


    void Input() {
        string s;

        cin>>cc;
        for(int i=cc; i-->0;) {
            cin>>s;
            combine[s[0]][s[1]]=s[2];
            combine[s[1]][s[0]]=s[2];
        }

        cin>>dc;
        for(int i=dc; i-->0;) {
            cin>>s;
            opposed[s[0]][s[1]]=true;
            opposed[s[1]][s[0]]=true;
        }

        cin>>nc;
        cin>>in;
    }

    string Solve() {
        for(int i=0; i<nc; ++i) {
            magica_one(in[i]);
        }

        stringstream ss;
        ss<<"[";
        for(int i=0; i<rec; ++i) {
            if(i>0) ss<<", ";
            ss<<re[i];
        }
        ss<<"]";
        return ss.str();
    }

    private:

    void magica_clear() {
        ZERO(re);
        ZERO(cre);
        rec=0;
    }

    void magica_one(char c) {
        bool is_opposed = magica_opposed(c);

        re[rec++] = c;
        ++cre[c];

        if(!magica_combine()) {
            if(is_opposed)
                magica_clear();
        }else{
            while(magica_combine()) ;
        }
    }

    bool magica_opposed(char c) {
        for(char x='A'; x<='Z'; ++x) {
            if(cre[x]>0 && opposed[c][x])
                return true;
        }
        return false;
    }

    bool magica_combine() {
        if(rec<2) return false;
        char a = re[rec-1], b = re[rec-2];
        char c = combine[a][b];
        if(!c) return false;

        --cre[a]; --cre[b]; rec-=2;
        re[rec++] = c;
        ++cre[c];

        return true;
    }

};

int main() {
    ios_base::sync_with_stdio(0);
    long Cases;
    cin>>Cases;
    for(int iCase=1; iCase<=Cases; ++iCase) {
        Problem* P = new Problem();
        P->Input();
        cout<<"Case #"<<iCase<<": ";
        cout<<P->Solve()<<endl;
        delete P;
    }
    return 0;
}

/*
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW

==

Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []



*/
