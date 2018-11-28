#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)

#define ll long long
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
vector<pair<ll,ll> > vec;
int N;
double dista;
double f(double p, int index)
{
	double c1 = 0., c2 = 0.;
	double place = p;
	for(int i = index+1 ; i < N ; i ++ )
	{
		int k = vec[i].second;
		double p2 = vec[i].first;
		for( int j = 0 ; j < k ; j ++ )
		{
			c1 += fabs(place-p2);
			place += dista;
			c2 += fabs(place-p2);
		}	
	}
	for( int i = index ; i >= 0 ; i -- )
	{
		int k = vec[i].second;
		double p2 = vec[i].first;
		for( int j = 0 ; j < k ; j ++ )
		{
			c2 += fabs(place-p2);
			place -= dista;
			c1 += fabs(place-p2);
		}		
	}
	return min(c1, c2);	
}

bool ok(double len)
{
	vector<pair<double,double> > aux;
	int i,j ,k;
	for( i = 0 ; i < vec.size() ;i ++ )
	{
		for( j = 0 ; j < vec[i].second ; j ++ )
			aux.PB(MP(vec[i].first-len, vec[i].first+len));
	}
//	sort(aux.begin(), aux.end());
	double mini = -1e36;
	for( i = 0 ; i < aux.size() ; i ++ )
	{
		if( mini+dista > aux[i].second ) return false;
		mini = max(aux[i].first, mini + dista );
	}
	return true;
	
}




int main()
{
	int i,j ,k;
	int casos ; cin >> casos;
	for( int h = 0 ; h < casos ;h ++ )
	{
		ll C, D;
		cin >> C >> D;
		N = C;
		dista = D;
		vec.clear();
		for( i = 0 ; i < C ; i ++ )
		{
			ll a , b ; cin >> a >> b;
			vec.PB(MP(a,b));
		}
		double res = 1e36;
		double b = 0., e = 1e13;
		
		int pasos = 0;
		while( pasos < 100 && fabs(e-b) > 1e-11 )
		{
			pasos++;
			double med = (b+e)/2.;
			if( ok(med) ) e = med;
			else b = med;
		}
		res = b;
		
		/*
		for( i = 0 ; i + 1 < C ; i ++ )
		{
			// BS en el intervalo...
			double b = 0., e = vec[i+1].first-vec[i].first;
//			double bf = f(b+vec[i].first), ef = f(e+vec[i].first);
			int paso = 0;
			while( fabs(e-b) > 1e-9 && paso <= 100 )
			{
				paso ++;
				double med1 = (e-b) * (1./3.);
				double med2 = (e-b) * (2./3.);
				
				if( f(med1+vec[i].first,i) < f(med2+vec[i].first,i) )
				{
					e = med2;
				}else b = med1;
			}
			res = min(res, f(b+vec[i].first, i));
		}
*/
		cout << "Case #" << h+1 << ": " ;
		cout << setprecision(10) << (res+1e-12) << endl;
	}return 0;
}

