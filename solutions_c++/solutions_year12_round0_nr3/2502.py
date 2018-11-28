// esta3anna 3al sha2a belAllah ..
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
#define rep(i,n,m) for( int i = (int) n ; i < (int) m ; ++i )
#define	rrep(i,n,m) for( int i = (int) n ; i >= (int) m ; --i )
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define pb(x) push_back(x)
#define mp make_pair
#define mems(arr,v) memset(arr,v,sizeof arr)
#define setb(x,bit) (x|(1<<bit))
#define resetb(x,bit) (x&(~(1<<bit)))
#define is0(x,bit)((x&(1<<bit))==0)
#define is1(x,bit)((x&(1<<bit))!=0)
#define INT_MAX  2000000000
#define INT_MIN -2000000000
#define debug(x) cout << #x << " : " << x << endl
typedef unsigned long long ll;
typedef long double ld;
#define Read() freopen("input.txt","r",stdin)
#define Write() freopen("output.txt","w",stdout)
int A,B;
int Ok(int n)
{
	stringstream ss;
	ss << n;
	int nDigits = ss.str().size();
	int koko = n,Counter = 0;
	do
	{
		if (koko > n && koko >= A && koko <= B)
			Counter ++;
		koko = ((koko%10)*powl(10,nDigits-1))+(koko/10);
	}while (koko != n);
	return Counter;
}
int main ()
{
	Read();
	Write();
	int cases,Counter;
	cin >> cases;
	rep(C,1,cases+1)
	{
		Counter = 0;
		cin >> A >> B;
		rep(n,A,B+1)
				Counter += Ok(n);
		cout << "Case #" << C << ": " << Counter << endl ;
	}
}