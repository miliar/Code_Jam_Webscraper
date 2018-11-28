#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define maxn 1100
#define maxp 1100000

string toUpperString(string text)
{
string toReturn(text); // duplicate input for manipulation

for(int i=0;i<text.length();++i) // for each character in string
{
toReturn[i]=toupper(text[i]); // convert char to uppercase
}

return toReturn; // return in upper case
}


string t1[110],t2[1100],tr[500000];

int main()
{string line;
        int w=0,acc=0;
  ifstream jam;
  jam.open("C:/A-small-attempt2.in", ios::in);
  if (jam.is_open())
  {
    while (! jam.eof() )
    {
      getline (jam,line);
      tr[w] = line;
      w++;
    }
    jam.close();
  }
  
  ofstream jam_o;
  jam_o.open("C:/A-small-attempt2.out.txt", ios::out);
   
  int T;
  T = atoi(tr[acc].c_str());
  //cout << T;
  acc++;//acc=1
  for(int C=1; C<=T; C++) 
  {  
    int s,q,eng=500,eng1=500,pos=0,sw=0,p=0;
    s = atoi(tr[acc].c_str());
    acc++;  //acc=2
    for(int i=0;i<s;i++)
    {                    
            t1[i] = toUpperString(tr[i+acc]);
    }
    acc += s; //acc =5
    q = atoi(tr[acc].c_str());
    acc++; //acc=6
    for(int j=0;j<q;j++)
    {    
            t2[j] = toUpperString(tr[j+acc]);
    }
    acc += q; //=11
 for( p=0;p<q;p++)
 {
    for(int k=0;k<s;k++)
    {    
        if( k == eng1)
         {    
              goto l1;
         }
         else
     	{
           
             for(int l=p;l<q;l++)
             {       
                     int compar = t1[k].compare(t2[l]);
                     if( compar == 0)
                     {   if(l >= pos )
                         {        eng=k;
                                  pos=l;                
                                  goto l1;
                          }
                          goto l1;
                     }
                     else if( l == q-1)
                     {    
                          goto l2;                            
                     }
             }
         }      
l1: ; }
    sw += 1;
    p = pos;
    eng1 = eng;
  }
l2:  jam_o << "Case #"<<C<< ": "<< sw<<endl;
 // system("PAUSE"); 
  }
    jam_o.close();           
  }