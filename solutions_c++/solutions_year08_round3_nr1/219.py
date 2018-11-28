#include <stdafx.h>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <set>
#include <list>
#include <map>

#define For(i,a,b) for (int i=a; i <= b; ++i)
#define Ford(i,a,b) for (int i = a; i >= b; --i)
#define Rep(i,n) For(i, 0, n -1)
#define Repd(i,n) For(i, n - 1, 0)
#define mp(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))
#define all(v) v.begin(), v.end()
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
const int INF=(1<<30);

using namespace std;

int main(int argc, char* argv[]) {
    string name = "a-large.in";//argv[1];
    string outName = name + ".out";
    ifstream in(name.c_str());
    
    ofstream out(outName.c_str());

    int N;
    in >> N;
    Rep(i, N) {

        
        out << "Case #" << i + 1<< ": ";

        long long P, K, L;
        in >> P >> K >> L;

        vector<long long> f;

        long long t;
        Rep(j, L) {
            in >> t;
            f.push_back(t);
        }
      //  cout << f;

        sort(all(f), greater<long long>());

        vector<long long> keys(K, 1);
        long long s = 0L;
        long long j = 0L;
        if (K * P < L) {
            out << "Impossible";
        } else {
            for (long long k = 0; k < L; ++k) {
                s += keys[j] * f[k];
                
                keys[j]++;
                ++j;
                if (j >= K) {
                    j = 0;                    
                }
            }

            out << s;
        }
        out << endl;
    }

}

