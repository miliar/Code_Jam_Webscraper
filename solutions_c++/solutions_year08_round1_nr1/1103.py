#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define REPD(i,n) for (int i((n)-1); i >= 0; --i)
#define FILL(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define ALL(v) (v).begin(), (v).end()
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define ST first
#define ND second

#define ISFOUND(vec,f) (find(vec.begin(), vec.end(), f) != vec.end())
#define SORT(vec) sort(vec.begin(),vec.end());
template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }


int main()
{
    ofstream fout ("a.out");
    ifstream fin ("a2.in");
    string temp;
    char t;
    
    int N;           // Number of test cases
    int n;
    vi v1, v2, v3;
    int v;
    const long int INF = 999999999;
    long int m;
    long int tmp;
    
    
    
    if (fin.is_open())
    {

       fin >> N;
       //getline(fin, temp);
       REP(q,N)
       {                              
               fin >> n;
               v1.clear();
               v2.clear();
               v3.clear();
               
               REP(i,n)
               {
                       fin >> v;
                       v1.PB(v);
               }
                       
               REP(i,n)
               {
                       fin >> v;
                       v2.PB(v);
               }
               m = INF;
               v3 = v2;

               SORT(v2);
               do {

                   
                       tmp = 0;
    
                       REP(u,n)
                       {
                           tmp  += v1[u] * v2[u];
                           //cout << v1[u] << "*" << v2[u] << endl;
                       }
                       
                       //cout << "=====" <<  endl << m << endl << tmp << endl << endl;
                       if (tmp < m)
                          m = tmp;  
                            
                  
              } while(next_permutation(v2.begin(), v2.end()));

               
               fout << "Case #" << (q+1) << ": ";  
               fout << m << endl;
               
       }


    }
    system("PAUSE");
    return 0;
}
