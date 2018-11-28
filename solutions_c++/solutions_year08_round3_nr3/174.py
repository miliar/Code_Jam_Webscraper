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
	long long n,m,X,Y,Z;
	cin>>n>>m>>X>>Y>>Z;
 long long an;
 an=0;

	vector<long long> x(n, 0), y(n, 0);
	vector<long long> A(m, 0);

	F(i,0,m)
	{
		cin>>A[i];
	}


	F(i,0,n)
	{
     x[i]=A[i%m];
	 //cout<<x[i]<<"  ";
     A[i%m] = (X * A[i%m] + Y * (i + 1)) % Z;
	}

	long long o,o1;
	
	F(i,0,n)
	{o=1;
	 //o1=0;


	 F(j,0,i)
		 if(x[j]<x[i]){o+=y[j]%1000000007;}// o1+=y[j]/10000000;}

     y[i]=o%1000000007;
	}
	
an=0;
F(i,0,n){an+=y[i]%1000000007;}
an=an%1000000007;


	cout<<"Case #"<<test<<": "<<an<<endl;

	
}


cin>>T;

	return 0;
}