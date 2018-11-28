#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
const double eps = 1e-11;
const double pi = acos(-1.0);
const double inf = 1e17;
#define swap(a,b) {a^=b;b^=a;a^=b;}
#define two(X) (1<<(X))
#define pair <int,int> pii
#define SZ(x) ((int)x.size())
template<class T> T gcd(const T &a,const T &b) {return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(const T &a,const T &b) {return a*(b/gcd(a,b));}
template<class To, class From> To castToFrom(From arg) {To ret;std::stringstream ss(""); ss << arg; ss >> ret; return ret; }//castToFrom<int,string>("1234")
vector<string> split(string& str ) {
	vector< string > ret;
	string::iterator from( str.begin() );
    int i = 0;
    while( true ) {
		string::iterator to = find( from, str.end(), ' ');
        if( to == str.end() ) {
            string temp(from,to);
			ret.push_back( temp );
            break;
        } else {
			string temp(from,to);
            ret.push_back( temp );
            from = ++to;
        }
        i++;
    }
	return ret;
}
template<class T>
void MSG_HELPER(const T& arg) {
	std::cout << arg;
}
#define MSG(X) std::cout << #X << " = ", MSG_HELPER(X), std::cout << std::endl
#define out(x) (cout << #x << ": " << x << endl)
int main()
{
        //freopen("A-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
        freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
        int i,T,N;
        __int64 K,C;
        cin >> T;
        for ( i = 1; i <= T; i ++ ){
              cin >> N >> K;
              C = two(N);
              cout << "Case #" << i << ": " ;
              if ( (K + 1) % C == 0  && (K + 1)/C > 0 ) cout << "ON" << endl;
              else cout << "OFF" << endl;
        }
        //system("pause");
        return 0;
}


//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
    //	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);


// memset(E,0,sizeof(E));

