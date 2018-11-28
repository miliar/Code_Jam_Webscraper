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

#define contest 1

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
		string doit(VS,VS,string);
};

string answer::doit(VS com,VS opp,string seq){
	string ret="";
	string temp="";
	temp.PB(seq[0]);
	FOR(i,1,SZ(seq)){
		bool f1,f2;
		f1=f2=true;
		temp.PB(seq[i]);
		if(SZ(temp) >=2){
		FOR(j,0,SZ(com)){
			if((temp[SZ(temp)-1]==com[j][0] && temp[SZ(temp)-2]==com[j][1]) || (temp[SZ(temp)-1]==com[j][1] && temp[SZ(temp)-2]==com[j][0])){
				temp.erase((SZ(temp)-2),2);
				temp.PB(com[j][2]);
				f1=false;
				break;
			}
		}
		if(f1){
			FOR(j,0,SZ(opp)){
				FOR(k,0,SZ(temp)-1){
					if((temp[SZ(temp)-1] == opp[j][0] && temp[k]==opp[j][1]) || (temp[k]==opp[j][0] && temp[SZ(temp)-1]==opp[j][1])){
						temp="";
						f2=false;
					}
					if(f2==false)
						break;
				}
			}
		}
	}
	}
	ret.PB('[');
	ZFOR(i,SZ(temp)){
		if(i==SZ(temp)-1) ret.PB(temp[i]);
		else{
			ret.PB(temp[i]);
			ret.PB(',');
			ret.PB(' ');
		}
		
	}
	ret.PB(']');
	return ret;
}


int main(int argc, char** argv)
{
	
	freopen("B-large.in","r",stdin);
	if(contest)
		freopen("B-large.out","w",stdout);
	int TC = getInt();
	FOR(i,1,TC+1) {
			string ret;
			int c,d,n;
			VS com,opp;
			string temp;
			cin>>c;
			ZFOR(j,c){
				cin>>temp;
				com.PB(temp);
			}
			cin>>d;
			ZFOR(j,d){
				cin>>temp;
				opp.PB(temp);
			}
			cin>>n;
			cin>>temp;
			answer * obj = new answer();
		 	ret = obj->doit(com,opp,temp);
			cout<<"Case #"<<i<<": "<<ret<<endl;
		}
	return 0;
}
