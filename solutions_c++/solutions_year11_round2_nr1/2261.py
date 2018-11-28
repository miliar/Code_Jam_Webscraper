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

typedef long double data;
 
const int INFIN = 1000000000;
const double pi=acos(-1.0);

class answer {
	public:
		vector<data> doit(VS);
};

vector<data> answer::doit(VS input) {
	vector<data> ret;
	data __ret[SZ(input)][3];
    FOR(i,0,SZ(input)){
       data tp= 0.0;
       data tw=0.0;
       FOR(j,0,SZ(input[i])){
          if(input[i][j] != '.') tp+=1.0;
          if(input[i][j] == '1') tw+=1.0;
       }
       data OW =0.0;
       if(tp!=0)
         OW = tw/tp;
       __ret[i][0] = OW;
       data OWC = 0.0;
       FOR(j,0,SZ(input[i])){
         if(input[i][j]!='.'){
            data ow=0.0;
            data owct=0.0;
            FOR(k,0,SZ(input[j])){
              if(k!=i && input[j][k]=='1')
                 ow+=1.0;
              if(k!=i && input[j][k]!='.')
                 owct+=1.0;
            }
            OWC += ow/owct;
         }
       }
       __ret[i][1] = OWC/tp;
    }
    FOR(i,0,SZ(input)){
      data OOWC =0.0;
      data tp =0.0;
      FOR(j,0,SZ(input[i])){
         if(input[i][j]!= '.'){
            OOWC += __ret[j][1];
            tp+=1.0;
         }
      }
      __ret[i][2] = OOWC/tp;
    }
    FOR(i,0,SZ(input)){
      data push = 0.25 * __ret[i][0] + 0.50 * __ret[i][1] + 0.25 * __ret[i][2];
      ret.PB(push);
    }
    return ret;
}



int main(int argc, char** argv)
{
	
	freopen("A-large.in","r",stdin);
	if(1)
		freopen("A-large.out","w",stdout);
	
	int TC = getInt();
	FOR(i,1,TC+1) {
			vector<data> ret;
            int n;
			VS input;
			cin>>n;
			string s="";
			FOR(j,0,n){
                 cin>>s;
                 input.PB(s);
             }
			answer * obj = new answer();
		 	ret = obj->doit(input);
			cout<<"Case #"<<i<<":"<<endl;
			FOR(j,0,SZ(ret)){
                 printf("%.12Lf\n", (double) ret[j]);
             }
		}
	getchar();
	getchar();
	return 0;
}
