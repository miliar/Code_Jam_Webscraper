#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
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
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

vector<int> B,E,W;

int X,S,R,T,N;

int main()
{
    int TEST; cin>>TEST; int cn=0;
    while(TEST--)
    {
        ++cn;

	cin>>X>>S>>R>>T>>N;
	B.clear(); E.clear(); W.clear();
	int TEMP=0;
	for(int i=0;i<N;i++)
	{
	    int b,e,w; cin>>b>>e>>w;
	    B.push_back(b); E.push_back(e); W.push_back(w);
	    TEMP+=e-b;
	}
	
	B.push_back(0); E.push_back(X-TEMP); W.push_back(0);
	N++;

	for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(W[j]<W[i])
	{
	    swap(B[i],B[j]); swap(E[i],E[j]); swap(W[i],W[j]);
	}
	double timeRem=T, ans=0;
	double dist=0;


	for(int i=0;i<N;i++)
	{
	    double step=E[i]-B[i];
	    double timeReq=1.0*step/(W[i]+R);
//	    cerr<<"KKK "<<step<<' '<<timeReq<<' '<<timeRem<<endl;
	    if(timeReq<timeRem+TOLL)
	    {
		ans+=timeReq; timeRem-=timeReq;
	    }
	    else
	    {
		ans+=timeRem;
		step-=(W[i]+R)*timeRem;
		ans+=step/(W[i]+S);
		timeRem=0;

	    }
	    dist+=(E[i]-B[i]);
	}
    	
	printf("Case #%d: %.12lf\n",cn,ans);
	
	

	
	
	


    }
}
