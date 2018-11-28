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
/*
 ifstream cin ("c:\A-small.in");
 ofstream cout ("c:\A-small.out");
*/
long long T;

cin>> T;


T++;
F(test,1,T)
{
	long long P,K,L;
	cin>>P>>K>>L;
 int an;
 an=0;

	vector<int> x(L, 0);
	vector<int> p_(P, 0); /// 0..K

	F(i,0,L)
	{
		cin>>x[i];
	}

	SB(x);



if(!(L>K*P))
{
		F(j,0,L)
		{
     	 F(i,1,P+1)
		 {
			 if(p_[i-1]<K) {p_[i-1]++; an+=i*x[j]; break;}
		 }
     

		}

	


	cout<<"Case #"<<test<<": "<<an<<endl;
} else cout<<"Case #"<<test<<": Impossible"<<endl;
	
}


cin>>T;

	return 0;
}