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
vector<string> ex2s(string s, char c){vector<string> vs; string tmp=""; for(int i=0;i<s.length();i++){
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
vector<string> board;
int nor = 4, noc = 4;
char calcStatus(int stX, int stY, char c, int rw, int cl)
{
    if(c=='T')
        {
            char x = calcStatus(stX, stY, 'X', rw, cl);
            if(x=='X') return x;
            
            char o = calcStatus(stX, stY, 'O', rw, cl);
            if(o=='O') return o;
            
            return 'N';
        }
        
    else if(c=='X')
            {
                int i = stX;
                int j = stY;
                char ret = 'X';
                while(i<nor && j<noc && i>=0 && j>=0){
                    if(board[i][j] == 'O' || board[i][j]=='.')
                    {
                        return 'N';
                    }
                    i = i + rw;
                    j = j + cl;
                        
                }
                return 'X';
            }
        else {
            
                int i = stX;
                int j = stY;
                char ret = 'O';
                while(i<nor && j<noc && i>=0 && j>=0){
                    if(board[i][j] == 'X' || board[i][j]=='.')
                    {
                        return 'N';
                    }
                    i = i + rw;
                    j = j + cl;
                }
                return 'O';
        }
}


void init(){
    if(board.size())
    {
        board.erase(board.begin(), board.end());
    }
}
int main(int argc, char** argv)
{
    sfileIO();
  int cases;
    cin>>cases;
    
    for(int eachCase = 0; eachCase<cases; eachCase++){
        init();
        //cin>>nor>>noc;
        string s;
        for(int i=0;i<nor;i++)
        {
            cin>>s;
            board.PB(s);
        }
        string opt = "xo";
        char r = 'N';
        for(int i=0;i<nor;i++)
        {
            r = calcStatus(i, 0, board[i][0], 0, 1);
            if(r != 'N')
            {
                break;
            }
        }
        
        if(r != 'N')
        {
            cout<<"Case #"<<eachCase+1<<": "<<r<<" won"<<endl;
             continue;
        }
        
        for(int i=0;i<nor;i++)
        {
            r = calcStatus(0, i, board[i][0], 1, 0);
            if(r != 'N')
            {
                break;
            }
        }
        
        if(r != 'N')
        {
            cout<<"Case #"<<eachCase+1<<": "<<r<<" won"<<endl;
            continue;
        }
         
        r = calcStatus(0, 0, board[0][0], 1, 1);
        if(r != 'N')
        {
            cout<<"Case #"<<eachCase+1<<": "<<r<<" won"<<endl;
            continue;
        }
        r = calcStatus(0, noc-1, board[0][noc-1], 1, -1);
        if(r != 'N')
        {
            cout<<"Case #"<<eachCase+1<<": "<<r<<" won"<<endl;
            continue;
        }
        
        for(int i=0;i<nor;i++)
            for(int j=0;j<noc;j++)
        {
            if(board[i][j]=='.')
            {
               r = '.';
               break;
            }
        }
        
        if(r=='.')
        {
            cout<<"Case #"<<eachCase+1<<": "<<"Game has not completed"<<endl;
            continue;
        }
         cout<<"Case #"<<eachCase+1<<": "<<"Draw"<<endl;
        
    }
}
