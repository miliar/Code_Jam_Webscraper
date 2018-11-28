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
void sfileIO(){freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);}
void lfileIO(){freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);}
string getLineasS(){ string s; getline(cin,s); return s; }
vector<string> getLineasV(){ vector<string> vs;string s; while(cin>>s) {vs.PB(s);} return vs; }
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
string di2s(int i){string s=""; int p; char c; while(i){ p = i%10; c = '0'+ (char)p; s = c + s; i=i/10;} if(s=="") s=s+'0';return s;}
void di2ca(int i,char *c){int p; int j=1; while(i){ p = i%10; c[j] = '0'+ (char)p; j++; i=i/10;} if(j==1) c[0]=0; else c[0]=j; c[j]='\0'; } //reverse and c[0] = length
int s2i(string s) {int i,l; l=s.length(); i= (int)(s[0] - '0') ;for(int j=1;j<l;j++) i = i*10 + (int)(s[j] - '0'); return i; }
//macro for string to character array

/****************************************cases************************************/
char toup(char c){ if(c>='a' && c<='z') return c-' '; return NULL;}
char tolo(char c){ if(c>='A' && c<='Z') return c+' '; return NULL;}
char toswap(char c){ if(c>='A' && c<='Z') return c+' '; else if(c>='a' && c<='z') return c-' '; return NULL;}

const int INFIN = 1000000000;
//vector< vector<int> > vec2(100, vector<int> (50,0));

int color[100000], no_nodes;
int pi[100000], reach[100000], covered[100000];
int tme = 0;
bool Graph[1000][1000];
bool result;
vector<int> ordered_nodes;
vector< vector<int> > cyclic_nodes;
int end = 0;
int q=0;


void DFS_VISIT(int u)
{
   color[u] = 1;
   //cout<<u<<"<=";
   if(result)
    return;
   for(int v=0;v<no_nodes;v++)
        {
            if(Graph[u][v] && color[v] == 0)
                {
                    ordered_nodes.PB(v);
                    DFS_VISIT(v);
                }
            else 
            if(Graph[u][v] && color[v] == 2)
                {
                    result = true;
                    //cout<<"("<<u<<", "<<v<<")";
                    return ;
                }
            if(result)
                return ;
        }
    color[u] = 2;
    ordered_nodes.erase(ordered_nodes.end()-1, ordered_nodes.end());
    return ;
}
void init()
    {
        for(int u=0;u<no_nodes;u++)
        {
            color[u] = 0;
            pi[u] = 0;
            reach[u] = 0;
            pi[u]= 0;
        }
        if(ordered_nodes.size()>=1)
            ordered_nodes.erase(ordered_nodes.begin(), ordered_nodes.end());
        tme = 0;
    }

void DFS()
{
    
    for(int i=0;i<no_nodes;i++)
        {
            init();
            DFS_VISIT(i);
            //cout<<i;
            if(result)
                return ;
        }
    return ;
}

int main()
{
    fileIO();
    int no_edges;
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
        {
            memset(Graph, false, sizeof(Graph));
            result = false;
            int n;
            cin>>n;
            //cout<<endl;
            no_nodes = n;
            for(int i=0;i<n;i++)
            {
                int x;
                cin>>x;

                for(int j=0;j<x;j++)
                    {
                        int ted;
                        cin>>ted;
                        Graph[i][ted-1] = true;
                    }
            }
            DFS();
            if(result)
                cout<<"Case #"<<t+1<<": "<<"Yes"<<endl;
            else 
                cout<<"Case #"<<t+1<<": "<<"No"<<endl;
        }
    
}
