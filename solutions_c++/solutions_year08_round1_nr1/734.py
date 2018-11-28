#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <fstream>
#include <functional>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
using namespace std;

        //My Macro's
#define FOR(i,n) for(int i=0;i<(int)n;i++)
#define FORN(i,st,end) for(int i=st;i<end;++i)
#define FORD(i,n) for(int i=(int)n;i>=0;i--)
#define SZ(n) ((int)n.size())
#define RET return
#define BTOE(a) a.begin(),a.end()
#define foreach(it,a) for(__typeof(a.begin()) it=a.begin();it!=a.end();++it)
#define BTOER(a) a.rbegin(),a.rend()
#define SORT(a) (sort(BTOE(a)))
#define PB push_back
#define SET(a,i) (memset(a,i,sizeof(a)))
       //End of Macro's
typedef vector<string> VS;
typedef vector<int> VI;
typedef stringstream SS;
typedef long long LL;
typedef map<string ,int > MPSI;
typedef map<int ,string > MPIS;
typedef pair<int ,int > PII;

//Helper Functions
string itos(int i)
{SS ss;ss<<i;return ss.str();}
int stoi(string s)
{SS ss;ss<<s;int i;ss>>i;return i;}
//End of helper function

ofstream fout("out1.txt");

#define BUF 1001

char input[BUF];

int main()
{
    int test;
    cin>>test;
    for(int tc=1;tc<=test;tc++)
    {
       long long int N,ans=0;
       cin>>N;
       gets(input);
       VI array1,array2;
       int tmp;
       FOR(i,N)
       {
           cin>>tmp;
           array1.PB(tmp);
       }
       gets(input);    
       FOR(i,N)
       {
           cin>>tmp;
           array2.PB(tmp);
       }
       sort(BTOE(array1));
       sort(BTOE(array2));
       FOR(i,N)
         ans+=(array1[i]*array2[N-1-i]);
       cout<<"Case #"<<tc<<": "<<ans<<endl;
    }
    system("PAUSE");
}
//Presto



