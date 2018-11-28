#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

typedef long long i64;
void main(int argc, char* argv[]) {
    ifstream inf("c:\\temp\\in.txt");
    ofstream out("c:\\temp\\out.txt");
    int ncs;
    inf >> ncs;
    for (int i = 0 ; i != ncs ; i++) {
        int nv;
        inf >> nv;
        vector<i64> a,b;
        for (int j = 0 ; j != nv ; j++) {
            int t;
            inf >> t;
            a.push_back(t);
        }
        for (int j = 0 ; j != nv ; j++) {
            int t;
            inf >> t;
            b.push_back(-t);
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        i64 res = 0;
        for (int j = 0 ; j != nv ; j++) {
            res -= a[j]*b[j];
        }
        out << "Case #" << (i+1) << ": " << res << endl;
    }
    inf.close();
    out.close();
}