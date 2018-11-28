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

char buff[256];



vector<long long > d;
vector<long long> e;
long long seq(vector<long long>& vi) {
    //memset(d, 0, sizeof(d));
    d = vector<long long >(vi.size(), 0);
    e = vector<long long >(vi.size(), 0);
    
    long long res = 0;
    Rep(i, vi.size()) {
        d[i] = 1;
        e[i] = 1;
        res += 1;
        Rep(j, i)
            if (vi[j] < vi[i]) {
                res += e[j];
                e[i] += e[j];
                res %= 1000000007;
                e[i]%= 1000000007;
                
                if (d[i] < 1 + d[j]) {
                    
                    d[i] = 1 + d[j];
                }
            }

           
            //checkMax(res, dp[i]);
        }
    
    //cout << res<< " ";
    //res = 0;
 //   for(int i = 0; i < e.size(); ++i) {
   //     res += e[i];
    //}
   // cout << res % 1000000007;

    return res % 1000000007;
}


int main(int argc, char* argv[]) {
    string name = "c-small-attempt1.in";//argv[1];
    string outName = name + ".out";
    ifstream in(name.c_str());
   //ofstream out(outName.c_str());

  freopen(outName.c_str(), "w", stdout);


    int N;
    in >> N;
    Rep(i, N) {
        cout << "Case #" << i + 1<< ": ";
        
        long long n, m, X, Y, Z;
        in >> n >> m >> X >> Y >> Z;
        vector<long long> A(m, 0);
        for (int j = 0; j < m; ++j) {
            in >> A[j];
        }


        //cout << A;
        
        vector<long long> vi;
        vi.reserve(10000);
        for (int j = 0; j < n; ++j) {
           // cout << A[j % m] << " ";
            vi.push_back(A[j % m]);
            A[j%m] = ( X * A[j %m] + Y * (j + 1)) % Z;
 
        }

        //cout << vi;
        //if ( i > 0)
        cout << seq(vi);

        cout << endl;
    }
    
}

