//Bismillahir Rahmanir Rahim

#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>

#define si  100000
#define pb push_back
#define popb pop_back
#define pf push_front
#define popf pop_front
#define mp make_pair
#define fo(i,n) for(int i=0;i<(n);i++)
#define sorta(a) sort(a.begin(),a.end())
#define sortab(a,n) sort(a,a+n)
#define sz size()
#define eps 0.000000000001
#define pi 2.0*acos(0.0)

using namespace std;

typedef long long ll;
typedef vector<int>VI;
typedef vector<string>VS;
typedef set<int>SI;
typedef pair<int,int>par;
typedef vector<par>VP;

bool eq(double a,double b)
{return !(fabs(a-b)>eps);}



int main()
{
	freopen("inputb.txt","rt",stdin);
	freopen("outputb.txt","wt",stdout);
	int t;
	cin>>t;
	for(int cs=0;cs<t;cs++)
	{
	    ll n,D,G;
	    cin>>n>>D>>G;
	    cout<<"Case #"<<cs+1<<": ";
	    if(G==100&&D!=100||G==0&&D!=0)
	    {
	        cout<<"Broken"<<endl;
	    }
	    else
	    {
	        int fl=0;
	        if(D!=0){
	        for(ll i=1;i<=min(n,100LL);i++)
	        {
	            ll k = i;
	            if((k*D)%100==0)fl=1;
	        }
	        }
	        if(fl||(D==0))
	        cout<<"Possible"<<endl;


	        else
	        cout<<"Broken"<<endl;
	    }
	}

	return 0;
}
