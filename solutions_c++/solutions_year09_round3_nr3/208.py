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
#include<cstring>
#include<locale>
#include<utility>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

vector<int> rel;
int memo[200][200];

int recur(int st,int en)
{
    if(en-st<=1) return 0;
    if(memo[st][en]!=-1) return memo[st][en];
    int best=(1<<30);
    for(int i=st+1;i<en;i++)
    {
	int curcost=rel[i]-rel[st]-1+rel[en]-1-rel[i];
	int tot=curcost+recur(st,i)+recur(i,en);
	best=min(best,tot);
    }
    return memo[st][en]=best;
}


int main()
{
    int t,cn=0;
    cin>>t;
    while(t--)
    {
	memset(memo,-1,sizeof memo);
	cn++;
	int p,q;	
	cin>>p>>q;
	rel.resize(q);	
	for(int i=0;i<q;i++) cin>>rel[i];
	rel.insert(rel.begin(),0);
	rel.push_back(p+1);

	cout<<"Case #"<<cn<<": "<<recur(0,sz(rel)-1)<<endl;

	
    }
}
