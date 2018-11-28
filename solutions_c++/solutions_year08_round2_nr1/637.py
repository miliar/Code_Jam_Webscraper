//#define SOLVE "A-small"
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include<set>
#define GI ({int t; scanf("%d",&t);t;})
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(it,v) FOR(it,(v).begin(), (v).end())
#define sz size()
#define pb push_back
#define cs c_str()
#define INF ((int)(1e8))
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

int main () {
	freopen ("A-small-attempt1.in", "r", stdin);
	//cout<<"1yes"<<endl;
	freopen ("Amit.out", "w", stdout);
	int N=0;
	cin>>N;
	for(int I=1;I<=N;++I)
	{
		//cout<<"2yes"<<endl;
        LL n=0,A=0,B=0,C=0,D=0,x0=0,y0=0,M=0;
		LL res=0;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		LL X=x0,Y=y0;
		vector <PII> VP;
		VP.pb(make_pair(X,Y));
		for(int i=1;i<n;++i)
		{
                X=(A*X+B)%M;
                Y=(C*Y+D)%M;
                VP.pb(make_pair(X,Y));
        }
        //cout<<"3yes"<<endl;sort(VP.begin(),VP.end());
        //for(int i=0;i<VP.size();++i)
        //cout<<VP[i].first<<" "<<VP[i].second<<endl;
        //cin>>M;
        set <vector<PII> > MA;
        for(int i=0;i<n-2;++i)
        for(int j=i+1;j<n-1;++j)
        for(int k=j+1;k<n;++k)
        {
           double x=(0.0+VP[i].first+VP[j].first+VP[k].first)/3;
           double y=(0.0+VP[i].second+VP[j].second+VP[k].second)/3;
           if(x==floor(x) && y==floor(y))
           {
               //cout<<VP[0].first<<" "<<VP[1].first<<" "<<VP[2].first<<" "<<VP[0].second<<" "<<VP[1].second<<" "<<VP[2].second<<" > "<<x<<" "<<y<<endl;
               vector< PII >v;
               v.pb(VP[i]);v.pb(VP[j]);v.pb(VP[k]);
               sort(v.begin(),v.end());
               MA.insert(v);
           }
           //cout<<"4yes"<<I<<endl;
           //for(int i=0;i<VP.size();++i)
        //cout<<VP[i].first<<" "<<VP[i].second<<endl;
        }
		//cout<<"5yes"<<endl;
        cout<<"Case #"<<I<<": "<<MA.size()<<endl;
	}
	return 0;
}
