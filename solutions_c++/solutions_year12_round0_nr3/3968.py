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
/*****************************************macros************************************/
#define TYPE(m,a) __typeof(a) m = a
#define FOR(i,a,b) for(TYPE(i,(a)); i < (b); ++i)
#define DFOR(i,a,b) for(TYPE(i,(a)); i >= (b); --i)
#define ZFOR(i,N) FOR(i,0,N)
#define DZFOR(i,N) FOR(i,N,0)
#define SORT(x) sort((x).begin() , (x).end())
#define PB(x) push_back((x))
#define FORALL(it,v) for(TYPE(it, (v).begin()); it != (v).end(); ++it)
#define S2C(st, c) for(int i=0;i<st.size();i++) c[i] = st[i];
#define IA2CA(ia, ca, l) for(int i=0;i<l;i++) ca[i] = i2c(ia[i]);
#define CA2IA(ca, ia, l) for(int i=0;i<l;i++) ia[i] = c2i(ca[i]);
#define fout(x) cout<<"Case #"<<i+1<<": "<<x<<endl;
#define cfout(x) {cout<<"Case #"<<i+1<<": "<<x<<endl; continue;}
#define repeach(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define repreach(it,x) for(typeof(x.rbegin()) it=x.rbegin(); it!=x.rend(); ++it)
#define SIZE(x) x.size()
/****************************************typedefs**********************************/
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<VI> VVI;
typedef vector<VD> VVD;
typedef vector<VS> VVS;
typedef vector<long long> VL;
typedef vector<VL> VVL;
typedef vector<bool> VB;
typedef vector<VB> VVB;
/*****************************************Math************************************/
bool isPrime(long long a){ if(a <= 1) return false; if(a == 2) return true;
	if(a%2 == 0) return false; for(long long i=3;i<=sqrt(a);i+=2) if(a%i == 0) return false; return true; }
int GCD(int a,int b){ if(b==0) return a; return GCD(b,a%b);}
int LCM(int a,int b){return a*b/GCD(a,b);}
int getInt() { int x=0; scanf("%d",&x); return x;}

/*************************************Input Output*******************************/
char getChar(){ char x=' '; scanf("%c",&x); return x;}
string getString(){char c[1024]=""; scanf("%s",c); return c;}
long long getLong(){long long x= 0; scanf("%lld",&x); return x;}
void fileIO(){freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);}
void sfileIO(){freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);}
void lfileIO(){freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);}
string getLineasS(){ string s; getline(cin,s); return s; }
vector<string> getLineasV(){ vector<string> vs;string s; while(cin>>s) {vs.PB(s);} return vs; }
/********************************char, int, string, array************************/

//vector< vector<int> > vec2(100, vector<int> (50,0));

int main(int argc, char** argv)
{
    lfileIO();
    int T;
    cin>>T;
    
    for(int t=0;t<T;t++)
        {
            int start, end;
            cin>>start>>end;
            set< pair<int ,int > > mp;
            int n=start, digit=0;
            while(n)
                {
                    n = n/10;
                    digit++;
                }
            int p10 = pow(10,digit-1);
            
            
            for(int i=start;i<=end;i++)
                {
                    int tdigit = digit-1;
                    int x=i;
                    n = i;
                    int m=0;
                    while(tdigit)
                        {
                            m = n%10;
                            n = (n/10 + (m*p10));
                            if(n<=end && n>=start && n!=x)
                                {
                                    mp.insert(make_pair(min(x,n), max(x,n)));
                                    //cout<<x<<"  "<<n<<endl;
                                    //mp.insert(make_pair(max(x,n), min(x,n)));
                                }
                            tdigit--;
                        }
                }
            cout<<"Case #"<<t+1<<": "<<mp.size()<<endl;
        }
    return 0;
}
