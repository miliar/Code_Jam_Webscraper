/*
 * Tutorial:
 * Question:
 * Author: Anshul Goel
 * Date:
 *
 */
#include <iostream>
#include <fstream>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cassert>
#include <sstream>
#include <cmath>

using namespace std;

#define FOR(i, l, u) for(LET(i, l); i < (u); ++i)
#define REP(i, u) FOR(i, 0, u)
#define LET(x, a) __typeof(a) x(a)
#define IFOR(it, b, e) for(LET(it,b); it != e; ++it)
#define SHIFTL(i, n) ((i) << (n))
#define SHIFTR(i, n) ((i) >> (n))
#define POW2(n) (1 << (n))
#define MP(x, y) (make_pair(x, y))
#define SET(x, v) memset(&x, v, sizeof(x))
#define PB(x) push_back(x)
#define IPRINT(s, e) copy(s, e, ostream_iterator<__typeof(*s)>(cout, " "))
#define INRANGE(x, l, u) (x >= l && x < u)

#define DEBUG(x) if(_DEBUG) { x; }
#define PDBG(x) DEBUG(cerr << x << endl)
#define _DEBUG 1

typedef vector<int> v_i;
typedef vector<string> v_s;
typedef set<int> set_i;
typedef set<string> set_s;
typedef map<string,int> map_si;
typedef pair<int,int> p_i;

long gcd(long m,long n)
{
     while(n!=0)
     {
                long rem=m%n;
                m=n;
                n=rem;
                }
                return m;
}

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	ifstream cin("B-small-attempt0.in");
        ofstream cout("outputB.txt");
        

       long M,C,N,*A,G;
        cin>>C;
        M=C;
        while(C--)
        {
         cin>>N;
         A=new long[N];
         cin>>A[0];
         G=0;
         FOR(i,1,N){
                    cin>>A[i];G=gcd(abs(A[i]-A[i-1]),G);
                  //  cout<<"GCD :"<<G<<endl;
                    }
        
        long res=A[0]%G==0?0:(G-A[0]%G);
         cout<<"Case #"<<M-C<<": "<<res<<endl;
                // system("pause");
         
        delete[] A;
        }

        system("pause");
	//return 0;
}

