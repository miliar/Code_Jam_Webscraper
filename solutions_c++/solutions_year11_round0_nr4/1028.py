#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <string>
#include <algorithm>
#include <cstring>


using namespace std;

#define NMAX 1000100
#define CMAX 1001
#define ZERO(X) memset((X), 0, sizeof(X))
#define BE(X) (X).begin(), (X).end()

class Problem {
    public:

    long n;
    long diff;

    Problem()
        : n(0), diff(0)
    {
    }


    void Input() {
        cin>>n;
        for(int i=1; i<=n; ++i) {
            long v;
            cin>>v;
            if(v!=i) ++diff;
        }
    }

    string Solve() {
        stringstream ss;
        ss<<diff;
        return ss.str();
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
3
2
2 1
3
1 3 2
4
2 1 4 3

==

Case #1: 2.000000
Case #2: 2.000000
Case #3: 4.000000



*/
