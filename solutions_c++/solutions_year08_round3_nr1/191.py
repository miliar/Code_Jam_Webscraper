#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
using namespace std;

ifstream fin("in.in");
ofstream fout("out.out");

unsigned long long i,j,n,m,T,P,K;

int main() {
    fin >> T;
    for (unsigned long long t=1;t<=T;t++) {
        vector<unsigned long long> in;
        unsigned long long SOL(0);
        fin >> P >> K >> n;
        if (P*K < n) { fout << "Impossible" << endl; return 0; }
        for (i=0;i<n;i++) in.push_back( (fin>>j)?j:0 );
        sort(in.rbegin(),in.rend());
        unsigned long long tr = 0;
        for (i=0;i<n;i++) 
            SOL += in[i] * (tr++ / K + 1);
        fout << "Case #" << t << ": " << SOL << endl;
        }
    system("pause");
}
