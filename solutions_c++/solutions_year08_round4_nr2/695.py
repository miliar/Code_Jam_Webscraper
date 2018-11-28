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

long long T;

cin>> T;


T++;

F(test,1,T)
{
	long long a,n,m;
	cin>>n>>m>>a;

	swap(n,m);

	if(n*m<a){cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl; continue;}

	long long x1,x2,x3,y1,y2,y3;

	x1=0;
		y1=0;
		x2=0;
		y3=0;
 int as;
 as=0;


F(i,1,n+1)
{
	if(i*m<a)continue;
	if(a%i!=0)continue;
	y2=i;
	x3=a/i;
	as=1;
	break;
}

if(as==1)
{cout<<"Case #"<<test<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl; continue;}
else
{
 F(i,1,n+1)
 {
	if(i*m<a)continue;
	y2=i;
    x3=a/i;
	int b;
	b=0;
	if(a%i!=0){x3++;
	b=i-(a%i);}

 F(j,1,m+1)
 {
	if(j*n<b)continue;
	if(b%j!=0)continue;
	x2=j;
	y3=b/j;
	break;
 }

   if((x3*y2-x2*y3)==a || (x3*y2-x2*y3)==-1)
   {
	as=1;
	break;
   }
 }
}
if(as==1)
	cout<<"Case #"<<test<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl;
else
cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
	
}


//cin>>T;

	return 0;
}