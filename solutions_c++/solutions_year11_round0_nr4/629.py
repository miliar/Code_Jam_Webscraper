#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <algorithm>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>


using namespace std;

#define SZ(a) int((a).size())
#define isThere(a,x) ((a).find(x) != (a).end())
#define TYPE(m,a) __typeof(a) m = a
#define FOR(i,a,b) for(TYPE(i,(a)); i < (b); ++i)
#define DFOR(i,a,b) for(TYPE(i,(a)); i >= (b); --i)
#define ZFOR(i,N) FOR(i,0,N)
#define DZFOR(i,N) FOR(i,N,0)
#define SORT(x) sort((x).begin() , (x).end())
#define PB(x) push_back((x))
#define FORALL(it,v) for(TYPE(it, (v).begin()); it != (v).end(); ++it)

#define contest 0

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<VI> VVI;
typedef vector<VD> VVD;
typedef vector<VS> VVS;
typedef vector<long long> VL;
typedef vector<VL> VLL;
typedef vector<bool> VB;
typedef vector<VB> VBB;
typedef long long int64;
typedef unsigned long long uint64;

bool isUpperCase(char c){return c>='A' && c<='Z';}
bool isLowerCase(char c){return c>='a' && c<='z';}
bool isLetter(char c){return (c>='A' && c<='Z') || (c>='a' && c<='z');}
bool isDigit(char c){return c>='0' && c<='9';}
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
VS explodeString(string s,char a){VS ret;ZFOR(i,SZ(s)){int j=i;string temp="";while(s[j]!=a && j<SZ(s)){temp.PB(s[j]);j++;
		}ret.PB(temp);i=j;}return ret;}

bool isPrime(int a){ if(a <= 1) return false; if(a == 2) return false;
	if(a%2 == 0) return false; for(int i=3;i<sqrt(a);i+=2) if(a%i == 0) return false; return true; }
int GCD(int a,int b){ if(b==0) return a; return GCD(b,a%b);}
int LCM(int a,int b){return a*b/GCD(a,b);}
int getInt() { int x=0; scanf("%d",&x); return x;}
char getChar(){ char x=' '; scanf("%c",&x); return x;}
string getString(){char c[1024]=""; scanf("%s",c); return c;}
long long getLong(){long long x= 0; scanf("%lld",&x); return x;}

const int INFIN = 1000000000;
const double pi=acos(-1.0);

class answer {
	public:
		double doit(VI);
};

double answer::doit(VI list) {
	double ret;
	double misplaced=0;
	FOR(i,0,SZ(list)){
		if(list[i] != i+1)
		 misplaced++;
	}
	ret = misplaced;
	return ret;
}



int main(int argc, char** argv)
{
	freopen("D-large.in","r",stdin);
	if(1)
		freopen("D-large.out","w",stdout);
	
	int TC = getInt();
	FOR(i,1,TC+1) {
			double ret;
			int n;
			int temp;
			VI list;
			cin>>n;
			ZFOR(j,n){
				cin>>temp;list.PB(temp);
			}
			/*ZFOR(j,n){
				cout<<list[j]<<" ";
			}*/
			answer * obj = new answer();
		 	ret = obj->doit(list);
		 	printf("Case #%d: %6f\n",i,ret);
			//cout<<"Case #"<<i<<":"<<ret<<endl;
		}
	return 0;
}
