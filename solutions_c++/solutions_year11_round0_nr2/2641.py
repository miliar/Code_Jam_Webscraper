#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define fi(n,i)         for(int i=0;i<(int)n;i++)
#define fab(a,b,i)      for(int i=a;i<=b;i++)
#define max(a,b)        (a>b?a:b)
#define min(a,b)        (a<b?a:b)
#define _abs(x)         (x<0?(-1)*x:x)
#define all(c)          (c).begin(),(c).end()
#define contains(c,x)	(find(all(c),(x))!=(c).end())

#define fs              first
#define sc              second
#define pb              push_back
#define mp              make_pair
#define D(x)		cout << #x << " -> "<<x << endl;

typedef long long int64;
typedef unsigned long long uint64;
#define two(x)		(1<<(x))
#define twoL(x)		(((uint64)(1))<<(x))


const double oo = (1<<30);

const double eps = 1e-9;

using namespace std;

template<class T>
ostream& operator<<(ostream& out,vector<T> v)
{
    int sz = v.size();
    out <<"[";
    for(int i=0;i<sz;i++)
    {
	out<<v[i];
	if(i+1<sz)cout << ", ";
    }
    out<<"]";
    return out;
}

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;

map< pair<char,char> , char > mix;
set< pair<char,char> > opposite;
vector< char > elements;
void insertmix(char a , char b, char c)
{
    mix[mp(a,b)] = c;
    mix[mp(b,a)] = c;
}
void insertopp(char a , char b)
{
    opposite.insert(mp(a,b));
    opposite.insert(mp(b,a));
}

int main()
{
   ios_base::sync_with_stdio(0);
   freopen("2011/B.in","r",stdin);
   freopen("2011/B.out","w",stdout);

   int T,C,D,N;
   char x,y,z;
   cin>>T;
   fi(T,c)
   {
       mix.clear();
       elements.clear();
       opposite.clear();
       cin>>C;
       fi(C,j)
       {
	   cin>>x>>y>>z;
	   insertmix(x,y,z);
       }
       cin>>D;
       fi(D,j)
       {
	   cin>>x>>y;
	   insertopp(x,y);
       }

       map<pair<char,char> , char>::iterator it;
       set< pair<char,char> >::iterator is;

//       for(it=mix.begin();it!=mix.end();it++)
//	   cout <<it->fs.fs<<" + "<<it->fs.sc<<" = "<<it->sc<<endl;
//       cout << endl;
//       for(is=opposite.begin();is!=opposite.end();is++)
//       	   cout << is->fs<<" , "<<is->sc<<endl;
//       cout << endl;

       cin>>N;
       bool cool = true;
       fi(N,i)
       {
	   cin>>x;
//	   cout << "Processing "<<x<<endl;
	   if(elements.empty())
	   {
	       elements.pb(x);
	       continue;
	   }
	   char &b = elements.back();
//	   cout << "Back: "<<b<<endl;
	   pair<char,char> act = mp(b,x);
	   if(mix.find(act) != mix.end())
	   {
	       elements.pop_back();
	       elements.pb(mix[act]);
	       x = mix[act];
	       cool = false;
	   }

	   fi(elements.size(),i)
	   {
	       act = mp(elements[i],x);
	       if(opposite.find(act)!=opposite.end())
	       {
		   elements.clear();
		   cool = false;
	       }

	   }
//	   cout <<"Its "<<boolalpha<<cool<<" that we're cool " <<endl;
	   if(cool)
	       elements.pb(x);
	   cool = true;
       }
       cout << "Case #"<<c+1<<": "<<elements<<endl;


   }

   return 0;
}



















