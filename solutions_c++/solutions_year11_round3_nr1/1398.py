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
#define fout cout<<"Case #"<<i+1<<": "
#define cfout(x) {cout<<"Case #"<<i+1<<": "<<x<<endl; continue;}
#define PRINT1D(x,n){cout<<endl; for(int kk=0;kk<n;kk++) cout<<x[kk]; cout<<endl;}
#define PRINT2D(x,m,n){cout<<endl; for(int kk=0;kk<m;kk++){ for(int ll=0;ll<n;ll++)cout<<setw(7)<<x[kk][ll]; cout<<endl;} }
/****************************************typedefs**********************************/
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
/*****************************************Math************************************/
bool isPrime(int a){ if(a <= 1) return false; if(a == 2) return false;
	if(a%2 == 0) return false; for(int i=3;i<sqrt(a);i+=2) if(a%i == 0) return false; return true; }
int GCD(int a,int b){ if(b==0) return a; return GCD(b,a%b);}
int LCM(int a,int b){return a*b/GCD(a,b);}
int getInt() { int x=0; scanf("%d",&x); return x;}

/*************************************Input Output*******************************/
char getChar(){ char x=' '; scanf("%c",&x); return x;}
string getString(){char c[1024]=""; scanf("%s",c); return c;}
long long getLong(){long long x= 0; scanf("%lld",&x); return x;}
void fileIO(){freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);}
void sfileIO(){freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);}
void lfileIO(){freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);}

/********************************char, int, string, array************************/
int c2i(char c){int i=0; i=(int)c; i=i-48; if(i>=0 && i<=9) return i; else return -1;}
char i2c(int i){char c; c=(char)i; c=c+'0'; if(i>=0 && i<=9) return c; else return '0';}

//char* c2i(char c){int i=0; i=(int)c; i=i-48; if(i>=0 && i<=9) return i; else return -1;}

int countchar(string s,char c){int i=0;for(int j=0;j<s.length();j++) if(s[j] == c) i++; return i; }
vector<string> ex2v(string s, char c){vector<string> vs; string tmp=""; for(int i=0;i<s.length();i++){
    if(s[i]==c){vs.PB(tmp); tmp=""; continue;} tmp=tmp+s[i];} if(tmp!="") vs.PB(tmp); return vs;}

string ia2s(int a[],int sz){string c=""; stringstream ss; for(int i=0;i<sz;i++){ss<<a[i];} ss>>c; return c;}
int* s2ia(string s,int ar[50]){ar[0]=0;for(int i=1;i<=s.length();i++){ ar[i]=c2i(s[i-1]); ar[0]++;} return ar;}

string ca2s(char a[],int sz){string c=""; stringstream ss; for(int i=0;i<sz;i++){ss<<a[i];} ss>>c; return c;}
//macro for string to character array

/****************************************cases************************************/
char toup(char c){ if(c>='a' && c<='z') return c-' '; return NULL;}
char tolo(char c){ if(c>='A' && c<='Z') return c+' '; return NULL;}
char toswap(char c){ if(c>='A' && c<='Z') return c+' '; else if(c>='a' && c<='z') return c-' '; return NULL;}

const int INFIN = 1000000000;
/*********************************************************************************
WELCOME TO CODING

*********************************************************************************/
/*****************************user defined functions*****************************/


/***********************************main*****************************************/

int main(int argc, char** argv)
{
    int i=0,cases;
    lfileIO();
    cin>>cases;
    int r,c;

   string board[51];
    FOR(index,0,cases){
        cin>>r>>c;

        FOR(i,0,r)
            {
                board[i]=getString();
               // cout<<board[i]<<endl;
            }

        int flag=0;
        FOR(i,0,r)
            {   flag=0;
                FOR(j,0,c){
                    if(board[i][j]=='#')
                        {
                            if(i+1<r && j+1<c && board[i+1][j]=='#' && board[i+1][j+1]=='#' && board[i][j+1]=='#')
                                        {
                                        board[i][j]='/';
                                        board[i+1][j+1]='/';
                                        board[i][j+1]='\\';
                                        board[i+1][j]='\\';
                                        j++;
                                        }
                            else
                                {
                                    flag=1;
                                    break;
                                }

                        }

                    }
                     if(flag)
                        {
                            cout<<"Case #"<<index+1<<": "<<endl<<"Impossible"<<endl;
                            break;
                        }
            }
            if(flag)
                continue;

        cout<<"Case #"<<index+1<<": "<<endl;
       FOR(i,0,r)
        {
            FOR(j,0,c)
                cout<<board[i][j];
            cout<<endl;
        }


    }

    return 0;
}
