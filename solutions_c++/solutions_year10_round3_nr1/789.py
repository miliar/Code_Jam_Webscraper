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
#define pis pair<int,string>
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define MSG(X) std::cout << #X << " = ", MSG_HELPER(X), std::cout << std::endl
#define out(x) (cout << #x << ": " << x << endl)
template<class T> T gcd(const T &a,const T &b) {return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(const T &a,const T &b) {return a*(b/gcd(a,b));}
template<class To, class From> To castToFrom(From arg) {To ret;std::stringstream ss(""); ss << arg; ss >> ret; return ret; }//castToFrom<int,string>("1234")
vector<string> split(string& str ) {
	vector< string > ret;
	string::iterator from( str.begin() );
    int i = 0;
    while( true ) {
		string::iterator to = find( from, str.end(), '/');
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
void MSG_HELPER(const std::vector<T>&  arg) {
	const int SIZE = arg.size();
	std::cout << "vector[" << SIZE << "]{";
	for (int i = 0; i < SIZE; i ++)
		std::cout << arg[i] << ',';
	std::cout << '}';
}
template<class T>
void MSG_HELPER(const T& arg) {
	std::cout << arg << endl;
}
int main(){
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	int N;
	int A[1000],B[1000];
	int rst;
	int k;
	bool flag;
	string temp;
	scanf("%d",&testcase);
    for (int caseId=1;caseId<=testcase;caseId++){
        memset(A,0,sizeof(A));
        memset(B,0,sizeof(B));
		cin >> N;
		rst = 0;
		for ( int i = 0; i < N; i ++ )
		    cin >> A[i] >> B[i];
        for ( int i = 0; i < N; i ++ ){
            for ( int j = i ; j < N; j ++ ){
                if ( (A[i] > A[j] && B[i] < B[j]) || (A[i] < A[j] && B[i] > B[j]) )
                   rst ++ ;
            }
        }
		printf("Case #%d: ",caseId);
		cout << rst << endl;
	}
	//system("pause");
	return 0;
}
