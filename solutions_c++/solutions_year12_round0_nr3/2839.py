#include<iostream>
#include<cstdio>
#include<vector>
#include<sstream>
#include<set>

#define REP(i,n) for(int i=0;i<n;++i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define PRINT(n) {REP(i,n.size()) cout<<n[i]<<" ";cout<<endl;}
#define PB(n) push_back(n)

using namespace std;

string toString(int a)
{
	ostringstream oss;
	oss<<a;
	return oss.str();
}


void solve(int testNumber)
{
    int N,S,p; cin>>N>>S>>p;
    vector<int> g(N,0);
    REP(i,N) cin>>g[i];
//	PRINT(g);
	int ret = 0;
	vector<vector<int> > base;
	REP(uu,N)
	{
		int u = g[uu] / 3 ;
		int ub = g[uu]%3;
		vector<int> br(2,u);
		
		

		if(ub==0 && u>0) br[1]++;
		else if(ub==1&& u>0) br[0]++,br[1]++;
		else if(ub==2) br[0]++,br[1]+=2;
		
		base.PB(br);

	}
	
	REP(i,N)
	{
		if(base[i][0]>=p) ++ret;
		else if(base[i][1]>=p && S>0) ++ret,--S;
	} 
	
	cout<<"Case #"<<testNumber<<": "<<ret<<endl;

	
}

int main()
{
	int t;
	cin>>t;
	REP(i,t) solve(i+1);
}

 
