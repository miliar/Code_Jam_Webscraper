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
void fileIO(){freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);}

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


int main(int argc, char** argv)
{
    fileIO();
    int cases=getInt();
    vector<string> vcomb;
    vector<string> vopp;
    string s;
    string m="";
    string st;
    int icomb,iopp,ilen;

    for(int i=0;i<cases;i++){
        icomb=getInt();
        cout<<"Case #"<<i+1<<": ";
        vcomb.erase(vcomb.begin(),vcomb.end());
        vopp.erase(vopp.begin(),vopp.end());
        for(int j=0;j<icomb;j++)
            {st=getString();
                vcomb.PB(st);
            //cout<<endl<<vcomb[0];
            }

        iopp=getInt();
        for(int j=0;j<iopp;j++)
            vopp.PB(getString());


        ilen=getInt();
        s=getString();
        //cout<<"-->"<<s<<endl;
        m="";
        int p=0;
        for(int j=0;j<ilen;j++){

                if(p==0)
                    {m=s[j];
                    p=1;}
                else m=m+s[j];

                if(m.length()>1)
                    {
                        char c1=m[m.length()-1];
                        char c2=m[m.length()-2];

                        for(int k=0;k<icomb;k++)
                            {
                                if((c1==vcomb[k][0] && c2==vcomb[k][1]) || (c1==vcomb[k][1] && c2==vcomb[k][0]))
                                        {
                                            m.erase(m.end()-1);
                                            m.erase(m.end()-1);
                                            if(m.length()==0)
                                               p=0;
                                            if(p==0)
                                                {m=vcomb[k][2];
                                                p=1;
                                                }
                                            else m=m+vcomb[k][2];
                                            break;
                                        }
                            }
                        if(m.length()<2)
                            continue;
                        c1=m[m.length()-1];
                        for(int k=0;k<iopp;k++)
                            {
                                if((c1==vopp[k][0]) || (c1==vopp[k][1]))
                                    {
                                        int z;
                                        if(c1==vopp[k][0])
                                            z=1;
                                        else z=0;

                                        for(int l=0;l<m.length()-1;l++)
                                            {
                                                if(m[l]==vopp[k][z])
                                                        {
                                                            //m="";
                                                            m.erase(m.begin(),m.end());
                                                            m='0';
                                                            p=0;
                                                       break;
                                                        }

                                            }
                                    }
                            }

                    }

        }

    cout<<"[";
    if(m.length()>0)
        {
            if(m[0]!='0') cout<<m[0];
            for(int k=1;k<m.length();k++)
                {
                    if(m[k]!='0')
                    cout<<", "<<m[k];
                }
        }
    cout<<"]"<<endl;





    }

    return 0;
}
