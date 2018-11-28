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

int N;

cin>> N;





F(test,1,N+1)
{
	long long n,A,B,C,D,x0,y0,M;

	cin>>n>>A>>B>>C>>D>>x0>>y0>>M;

	vector<long long> x(n),y(n);

	int X,Y, ans;
	ans=0;
	X=x0; Y=y0;

	F(i,1,n)
	{
	 X=((long long)((long long)A*(long long)X+(long long)B))%M;
	 x[i]=X;
	}
F(i,1,n)
{
	 Y=((long long)((long long)C*(long long)Y+(long long)D))%M;
	 y[i]=Y;
}

	x[0]=x0;y[0]=y0;


	F(k,0,n-2)
	F(j,k+1,n-1)
	F(i,j+1,n)
	if(((x[i]+x[j]+x[k])%3==0)&&((y[i]+y[j]+y[k])%3==0)) ans++;
	 
/*
	F(i,0,n)
	{
		cout<<x[i]<<" "<<y[i]<<endl;
	}
cout<<endl<<endl;*/
	cout<<"Case #"<<test<<": "<<ans<<endl;

	
}


	return 0;
}