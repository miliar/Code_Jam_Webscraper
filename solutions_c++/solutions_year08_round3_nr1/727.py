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

#define BUF 1001

char input[BUF];

ofstream fout("out1.txt");

int main()
{
    int test;
    cin>>test;
    gets(input);
    for(int tc=1;tc<=test;tc++)
    {
        long long int ans=0,N,K,L,tmp;
        cin>>N>>K>>L;
        vector<long long int> freq;
        gets(input);
        FOR(i,L)
        {
            cin>>tmp;
            freq.PB(tmp);
        }
        gets(input);    
        sort(BTOER(freq));
        set<int> chk;
        foreach(it,freq)
              chk.insert(*it);
/*        if(SZ(chk)==1)
            fout<<"Case #"<<tc<<": "<<"Impossible\n";   
        else*/
        {
            int cnt=1,lt=0;
            while(lt<L)
            {
                FOR(j,K)
                {
                  if(lt>=L)
                     break;
                   ans+=(freq[lt]*cnt);
                   lt++;
                }    
                cnt++;
            }    
            cout<<"Case #"<<tc<<": "<<ans<<endl;
         }     
    }
    system("PAUSE");
}
//Presto

