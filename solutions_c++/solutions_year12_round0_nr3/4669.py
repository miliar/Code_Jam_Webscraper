
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<sstream>
#include<vector>
#include<queue>
#include<string>
#include<cctype>
#include<math.h>
using namespace std;

#define FOR(i,a,b) for ( int i = (a) ; i <= (int)(b) ; i ++ )
#define FRD(i,a,b) for ( int i = (a) ; i >= (int)(b) ; i -- )
#define FR(i,a) FOR(i,0,a)
#define FZ(i,a) FRD(i,a,0)
#define sz size()
#define pb push_back
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define FRV(i,v) FR( i , v.sz - 1 )
#define vi vector<int>
#define vf vector<float>
#define vd vector<double>
#define vs vector<string>
#define vc vector<char>
#define vb vector<bool>

#define mp make_pair
#define ii <int,int>
#define id <int,double>
#define ss stringstream
#define MAX_INT ((1<<31)-1)

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const long double eps = 1e-12;

int ni() { int n; cin >> n ; return n; }
string ns() { string s; cin >> s ; return s; }
char nc() { char c; cin >> c ; return c; }
long int nli() { long int n; cin >> n; return n; }
long long nll() { long long n; cin >> n; return n; }
string nline() { string n; do { getline(cin,n); } while(n == ""); return n;}

int gcd ( int a, int b ) { return ( a%b == 0 ? b : gcd(b,a%b) ) ; }

void main(){
	int T = 0;

	T = ni();

	FOR(tcn,1,T){
		ss res;
		int A = ni(), B = ni();
		int countres = 0;
		vector<vi> pairs;

		FOR(i,A,B){
			ss temps;

			temps << i << i ;
			
			string in_str=temps.str();
			int len = temps.str().size() / 2;

			FOR( j,1,in_str.size()-len){
				int num = 0;
				FR(k,len-1) num = num * 10 + in_str[j+k] - '0';
				if (num > i && num <= B ) {
					//res<<"("<< i <<","<< num <<")\n";
					ss ck1,ck2;
					ck1 << i; ck2 << num;

					if (ck1.str().size() == ck2.str().size()){
						vi item(2); item[0] = i;item[1] = num;
						if ( find(pairs.begin(),pairs.end(),item) == pairs.end()){
							countres ++;
							pairs.push_back(item);
						}
					}
				}
			}
		}

		res << countres;
		cout << "Case #" << tcn << ": "<<res.str()<<endl;
	}
}
