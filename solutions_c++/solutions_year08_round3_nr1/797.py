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
#define SIZE(x) (int)x.size()

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }


int main()
{
    ofstream fout ("a.out");
    ifstream fin ("a.in");
    string temp;
    
    int N;           // Number of test cases


    //vector<int> map[2000];
    vector<int> freq;
    
    int p,k,l;
    int t, s, j;

    int press = 0;
    if (fin.is_open())
    {

       fin >> N;
       REP(q,N)
       {                              
               fin >> p >> k >> l;
               freq.clear();
               REP(i,l)
               {
                       fin >> t;
                       freq.PB(t);
                       
               }
               sort(ALL(freq));
               reverse(ALL(freq));
               
               press = 0;
               s = 0; j = 1;
               //cout << "!!!!" << p << endl;
               REP(i,l)
               {
                       
                         press += freq[i] * j ;    
                         //cout << j << "*" << freq[i] << endl; 
                         
                         s++;
                         if (s == k)
                         {
                               s = 0;
                               j++;
                         }
                       
               }
               
               
               fout << "Case #" << (q+1) << ": " << press;  
               
               fout << endl;      
       }


    }
    system("PAUSE");
    return 0;
}
