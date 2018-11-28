#include <vector>
#include <iterator>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

typedef stringstream ss;

typedef string str;

typedef long double doub;

typedef vector< pair<int,int> > vpii;

typedef vector<int>::iterator vit;
typedef vector<int>::reverse_iterator vrit;

#define pb(what) push_back(what)
#define w(what) while(what)
#define re return
#define all(a) (a).begin(), (a).end()
#define F(i,b,a) for(int i=(int)b; i<(int)a; i++)
#define ln length()
#define s size()
#define SA(a) sort(a.begin(), a.end())// sort
#define SO(a,f,t) sort(a[f], a[t])// sort part
#define SB(a) sort(a.rbegin(), a.rend())// backsort
#define UN(a) unique(a.begin(), a.end())
#define mset(a,b) memset(a,b,sizeof(a))
#define sdel(v,n) v.erase(n,1)
#define soff(v,n) v.erase(n) // cut's off all the elements after n in STRING


int main()
{

 ifstream cin ("c:\A-small.in");
 ofstream cout ("c:\A-small.out");

int n;

cin>> n;




F(test,1,n+1)
{
int ansa=0, ansb=0, t, a, b, lefta=0, leftb=0;
cin>>t;

cin>>a>>b;

vector<pair<int,int> > ta(a),tb(b);
vi da(a, (0)),db(b, (0));
char ch;

string spam;

////////// READING TABLE

F(i,0,a)
{
 getline(cin, spam);

cin>>ch;
ta[i].first=60*10*(ch-'0');
cin>>ch;
ta[i].first+=60*(ch-'0');

cin>>ch;

cin>>ch;
ta[i].first+=10*(ch-'0');
cin>>ch;
ta[i].first+=(ch-'0');


//cin>>ch;


cin>>ch;
ta[i].second=60*10*(ch-'0');
cin>>ch;
ta[i].second+=60*(ch-'0');

cin>>ch;

cin>>ch;
ta[i].second+=10*(ch-'0');
cin>>ch;
ta[i].second+=(ch-'0');

ta[i].second+=t; ////
}


////


F(i,0,b)
{
 getline(cin, spam);

cin>>ch;
tb[i].first=60*10*(ch-'0');
cin>>ch;
tb[i].first+=60*(ch-'0');

cin>>ch;

cin>>ch;
tb[i].first+=10*(ch-'0');
cin>>ch;
tb[i].first+=(ch-'0');


//cin>>ch;


cin>>ch;
tb[i].second=60*10*(ch-'0');
cin>>ch;
tb[i].second+=60*(ch-'0');

cin>>ch;

cin>>ch;
tb[i].second+=10*(ch-'0');
cin>>ch;
tb[i].second+=(ch-'0');


tb[i].second+=t; ////
}

////////// TABLE READ SUCCESSFULLY
 
 F(i,0,a-1)
 F(j,i+1,a)
  if (ta[i].first>ta[j].first || (ta[i].first==ta[j].first && ta[i].second>ta[j].second))
      {swap(ta[i],ta[j]);}


 F(i,0,b-1)
 F(j,i+1,b)
  if (tb[i].first>tb[j].first || (tb[i].first==tb[j].first && tb[i].second>tb[j].second))
      {swap(tb[i],tb[j]);}


  lefta=a;
  leftb=b;

bool goa=false,gob=false, kan=false;
int tm=0;

while(lefta+leftb>0)
{
 if(lefta>0 && leftb>0)
 {
	 kan=false;
	F(scheda,0,a)
		if(kan){break;}else
   if(da[scheda]==0)
	 F(schedb,0,b)
	if(db[schedb]==0)
	{
		if( tb[schedb].second==ta[scheda].second ){goa=true; gob=true;}else
		if( tb[schedb].second<ta[scheda].second ){gob=true;}else
			 {goa=true;}
		kan=true;
		 break;
	}
 }	
 else
 {
	 ansa+=lefta;
     ansb+=leftb;
	 lefta=0;
	 leftb=0;
 }


 if(goa)
 {
	 ansa++;
	 tm=0;
	 kan=true;

   while(true)
   {
	kan=false;

	 F(scheda,0,a)
	if(da[scheda]==0 && tm<=ta[scheda].first)
	{lefta--; tm=ta[scheda].second; da[scheda]=1; kan=true; break;}

	if(!kan){break;}

    kan=false;

	 F(schedb,0,b)
	if(db[schedb]==0 && tm<=tb[schedb].first)
	{leftb--; tm=tb[schedb].second; db[schedb]=1; kan=true; break;}

	if(!kan){break;}
   }
  goa=false;
 }

  if(gob)
  {
	 ansb++;
	 tm=0;
	 kan=true;

   while(true)
   {
	kan=false;

	 F(schedb,0,b)
	if(db[schedb]==0 && tm<=tb[schedb].first)
	{leftb--; tm=tb[schedb].second; db[schedb]=1; kan=true; break;}

	if(!kan){break;}

    kan=false;

	 F(scheda,0,a)
	if(da[scheda]==0 && tm<=ta[scheda].first)
	{lefta--; tm=ta[scheda].second; da[scheda]=1; kan=true; break;}

	if(!kan){break;}
   }
  gob=false;
 }

}
    cout<<"Case #"<<test<<": "<< ansa<<" "<<ansb << endl;
}




	return 0;
}