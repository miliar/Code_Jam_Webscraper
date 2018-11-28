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
    vector<long> candy;
    long all_xor, all_sum;

    Problem()
        : n(0), all_xor(0), all_sum(0)
    {
        candy.clear();
    }


    void Input() {
        cin>>n;
        for(int i=n; i-->0;) {
            long v;
            cin>>v;
            all_xor ^= v;
            all_sum += v;
            candy.push_back(v);
        }
    }

    string Solve() {
        if(all_xor!=0) {
            return "NO";
        }
        
        sort(BE(candy));
        long odp = all_sum - candy[0];
        

        stringstream ss;
        if(odp<=0) ss<<"NO";
        else ss<<odp;
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
2
5
1 2 3 4 5
3
3 5 6

==

Case #1: NO
Case #2: 11



*/
