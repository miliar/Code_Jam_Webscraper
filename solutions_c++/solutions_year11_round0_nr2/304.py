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

vector<pair<char,int> > v;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;cin>>t;FR(cas,t)
	{
		printf("Case #%d: ",cas+1);
		int a[30][30]={0};
		bool kill[30][30]={false};
		int n;cin>>n;
		string s;
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
		vector<char> v;v.clear();
		FR(i,n)
		{
			int ch=s[i]-'A';
			if(!v.empty() && a[v.back()-'A'][ch]>0) 
			{
				v[v.size()-1]=a[v.back()-'A'][ch]+'A';
				continue;
			}
			v.push_back(s[i]);
			FR(i,v.size()-1)
				if(kill[v[i]-'A'][ch]) {v.clear();break;}
		}
		cout<<"[";
		if(!v.empty()) cout<<v[0];
		FOR(i,1,v.size()) cout<<", "<<v[i];
		cout<<"]"<<endl;
	}
}