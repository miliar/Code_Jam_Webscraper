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

#define fi(n,i)         for(int i=0;i<n;i++)
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

using namespace std;


struct robot
{
    int pos;
    int n;
    int seq[110];
    void clear()
    {
	pos = 0;
	n=0;
	memset(seq,-1,110);
    }
};

vector< pair<char,int> > sequence;
int main()
{
   ios_base::sync_with_stdio(0);
   freopen("2011/A.in","r",stdin);
   freopen("2011/A.out","w",stdout);
   int tc,button,n;
   char turn;

   cin>>tc;
   robot o,b;
   for(int c=1;c<=tc;c++)
   {
       sequence.clear();
       o.clear();
       b.clear();
       cin>>n;
       fi(n,i)
       {
	   cin>>turn;
	   cin>>button;
	   sequence.pb(mp(turn , button));
	   if(turn == 'O')
	       o.seq[o.n++]=button;
	   else
	       b.seq[b.n++]=button;
       }
       int time = 0;
//       fi(o.n,i)
//       	   cout << o.seq[i]<<" , ";
//       cout << endl;
//       fi(b.n,i)
//	   cout << b.seq[i]<<" , ";
//       cout << endl;
       o.n = 0;
       b.n = 0;
       o.pos =1;
       b.pos =1;
//       fi(sequence.size(),i)
//	   cout << sequence[i].fs<<" , "<<sequence[i].sc<< endl;
       bool opressed = false , bpressed =false;
       while(!sequence.empty())
       {
	   time++;
	   if(sequence.front().fs == 'O' && o.pos == sequence.front().sc )
	   {
	       sequence.erase(sequence.begin());
	       o.n++;
	       opressed = true;
	   }
	   else if(sequence.front().fs == 'B' && b.pos == sequence.front().sc )
	   {
	       sequence.erase(sequence.begin());
	       b.n++;
	       bpressed = true;
	   }
	   if(!opressed)
	   {
	       if(o.pos<o.seq[o.n])
		   o.pos++;
	       else if(o.pos>o.seq[o.n])
		   o.pos--;
	   }
	   if(!bpressed)
	   {
	       if(b.pos<b.seq[b.n])
		   b.pos++;
	       else if(b.pos>b.seq[b.n])
		   b.pos--;
	   }
//	   cout<<"o.pos: "<<o.pos<<endl;
//	   cout<<"b.pos: "<<b.pos<<endl;
	   bpressed = opressed = false;

       }
       cout << "Case #"<<c<<": "<<time<<endl;
   }


   return 0;
}



















