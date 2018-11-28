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
#include <ctime>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define SQR(a) ((a)*(a))
typedef long long  ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<ll,ll> PII;
typedef pair<double,double> PDD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define EPS 1e-8
const ll INF=1LL<<55;
#define MOD 1000000007
#define SIZE 100010

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;cin>>t;FR(cas,t)
	{
		printf("Case #%d: ",cas+1);
		bool kill[30][30]={false};
		char a[30][30]={0};
		FR(i,30)FR(j,30)a[i][j]=-1;
		int n;
		string s;
		cin>>n;
		FR(i,n)
		{
			cin>>s;
			a[s[0]-'A'][s[1]-'A']=s[2]-'A';
			a[s[1]-'A'][s[0]-'A']=s[2]-'A';
		}
		cin>>n;
		FR(i,n)
		{
			cin>>s;
			kill[s[0]-'A'][s[1]-'A']=true;
			kill[s[1]-'A'][s[0]-'A']=true;
		}
		cin>>n>>s;
		string res;res.clear();
		FR(i,s.size())
		{
			char ch=s[i];
			if(!res.empty() && a[res[res.size()-1]-'A'][ch-'A']>-1)
			{
				res[res.size()-1]=a[res[res.size()-1]-'A'][ch-'A']+'A';
			}
			else
			{
				res.push_back(ch);
				FR(i,res.size()-1)
					if(kill[res[i]-'A'][ch-'A']) {res.clear();break;}
			}
		}
		cout<<"[";
		if(!res.empty())
		{
			cout<<res[0];
			FOR(i,1,res.size()) cout<<", "<<res[i];
		}
		cout<<"]"<<endl;
	}
}