#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
typedef istringstream iss; typedef ostringstream oss; typedef long long int lli;
const double TOLL=1e-9;
int memo[110][1010];
vector<string> server, query;
int findbest(int sat,int qat)
{
	if(qat==sz(query)) return 0;

	if(memo[sat][qat]!=-1) return memo[sat][qat];
	int rv=1000000000; memo[sat][qat]=rv;

	if(server[sat]!=query[qat]) rv=min(rv,findbest(sat,qat+1));
	for(int i=0;i<sz(server);i++) if(i!=sat) 
	{
		if(server[sat]!=query[qat]) rv=min(rv,findbest(i,qat+1)+1);
		rv=min(rv,findbest(i,qat)+1);
	
	}
	return memo[sat][qat]=rv;
}

int main()
{
	int n,s,q;
	cin>>n; string temp;

	for(int cas=1;cas<=n;cas++)
	{
		memset(memo,-1,sizeof memo);
		server.clear(); 
		cin>>s; cin.ignore();
		for(int i=0;i<s;i++)
		{
			getline(cin,temp);
			server.push_back(temp);
		}
		cin>>q; cin.ignore();
		query.clear();
		for(int i=0;i<q;i++)
		{
			getline(cin,temp);
			query.push_back(temp);
		}
		int rv=1000000000;
		for(int i=0;i<s;i++) rv=min(rv,findbest(i,0));
		cout<<"Case #"<<cas<<": "<<rv<<endl;
//		cout<<"DEBUG"<<endl;
//		for(int i=0;i<s;i++) cout<<server[i]<<' '; cout<<endl;
//		for(int i=0;i<q;i++) cout<<query[i]<<' '; cout<<endl;

	}

	return 0;
}
