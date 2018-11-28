#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int,int> pii;
typedef long long ll;

#define I ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a ; i <= b ; i++)
#define REV(i,a,b) for(int i = a ; i >= b ; i--)
#define REP(i,n) for(int i = 0 ; i < n ; i++)

#define INF 1000000000

int cas;

string s1 = "Possible";
string s2 = "Broken";

ll gcd( ll a , ll b )
{
	if( a < b ) swap(a,b);
	if( !b ) return a;
	return gcd(b , a % b);
}

void solve()
{

	ll N , PD , PG;
	cin>>N>>PD>>PG;
	
	ll num = 100 / gcd(PD,100);
	if( num > N )
	{
		cout<<"Case #"<<cas<<": "<<s2<< endl;
		return ;
	}
	
	if(PG == 100 || PG == 0)
	{
		if(PD == PG)
			cout<<"Case #"<<cas<<": "<<s1<< endl;
		else
			cout<<"Case #"<<cas<<": "<<s2<< endl;
	}
	else
		cout<<"Case #"<<cas<<": "<<s1<< endl;

}

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		cas++;
		solve();
	}


	return 0;
}
