#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;

typedef long long ll;

#define ALL(a)	(a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define CLR(a) memset((a), 0 ,sizeof(a))

const double EPS = 1e-10;
const double PI  = acos(-1.0);

inline ll toInt(const string& s) {ll v; istringstream sin(s);sin>>v;return v;}
template<class T>inline T gcd(T a,T b){T tmp;while(b){tmp=a%b;a=b;b=tmp;}return a;}
template<class T>inline T lcm(T a,T b){return a / gcd(a,b) * b;}
template<class T>inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T>inline T sqr(T x) {return x*x;}

#define dump(x) cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;


template<class T> void print(int test_case,T answer){
	cout << "Case #" << test_case+1 << ": " << answer << endl;
}
#define primeSize 10000000
bool primeFlag[primeSize];
vector<long long>primeNum;

vector<long long> prime(){
	memset( primeFlag,0,sizeof(primeFlag) );
	vector<long long>primeNum;
	primeNum.push_back(2);
	primeFlag[0] = primeFlag[1] = true;
	for(int i=3;i<primeSize;i+=2){
		if( primeFlag[i] == false ){
			primeNum.push_back(i);
			for(int j=i*3;j<primeSize;j+=i*2)primeFlag[j] = true;
		}
	}
	return primeNum;
}

// 0 <= num < primeSize=10000000(1000–œ)‚ÌŽž
bool isPrime(long long num){
	if( num == 2 )return true;
	return num&1 && !primeFlag[num];
}

// primeSize < num < rt*rt ‚Ì‚Æ‚«
// primeSize=1000000(100–œ) => 1000000000000(1’›–¢–ž)
bool isPrime2(long long num){
	for(int i=0;i<primeNum.size()&&primeNum[i]*primeNum[i]<=num;i++){
		if( num % primeNum[i] == 0 )return false;
	}
	return num>=2;
}

int main(){
	int T;
	cin >> T;
	for(int i=0;i<T;++i){
		ll n,l,h,tmp;
		
		cin >> n >> l >> h;
		
		set<ll>se;
		for(int j=0;j<n;++j){
			cin >> tmp;
			se.insert( tmp );
		}
		
		for(int j=l;j<=h;++j){
			bool flag = true;
			
			set<ll>::iterator it = se.begin();
			for(;it!=se.end();++it){
				ll a = *it;
				if( a%j == 0 || j%a == 0 ){
					flag = true;
				}else{
					flag = false;
					break;
				}
			}
			if( flag ){
				print(i,j);
				goto exit;
			}
		}
		print(i,"NO");
		
		exit:;
		
		
	}
	return 0;
}
