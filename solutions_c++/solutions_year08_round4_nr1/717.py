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
#define CLR(a,x) memset((a),(x),sizeof((a)))

typedef istringstream iss; typedef ostringstream oss; typedef long long int lli;
const double TOLL=1e-9;
struct node
{
	bool val, gate, ca, leaf;
	node(bool v, bool g, bool cc, bool l)
	{
		val=v; gate=g; ca=cc; leaf=l;
	}
	node(){}
};

node arr[500100];

int dp[2][500100];
int m, v;
const lli inf=100000000;
lli recur(int value,int kunta)
{
//	cout<<value<<' '<<kunta<<endl;
	if(arr[kunta].leaf)
	{
		if(arr[kunta].val==value) return 0;
		return inf;
	}
	if(dp[value][kunta]!=-1) return dp[value][kunta];
	dp[value][kunta]=inf;
	lli rv=inf;
	lli leftz=recur(0,2*kunta);
	lli rightz=recur(0,2*kunta+1);
	lli lefto=recur(1,2*kunta);
	lli righto=recur(1,2*kunta+1);

	if(value==0)
	{
		if(arr[kunta].gate)
		{
			rv=min(leftz+rightz,rv);
			rv=min(leftz+righto,rv);
			rv=min(lefto+rightz,rv);
		}
		else
		{
			rv=min(leftz+rightz,rv);
		}

		if(arr[kunta].ca)
		{
			if(arr[kunta].gate)
			{
				rv=min((leftz+rightz)+1,rv);
			}
			else
			{
				rv=min(leftz+rightz+1,rv);
				rv=min(leftz+righto+1,rv);
				rv=min(lefto+rightz+1,rv);

			}
		}
	}
	else if(value==1)
	{
		if(arr[kunta].gate)
		{
			rv=min(rv,righto+lefto);
		}
		else
		{
			rv=min(rv,righto+lefto);
			rv=min(rv,righto+leftz);
			rv=min(rv,rightz+lefto);
		}

		if(arr[kunta].ca)
		{
			if(arr[kunta].gate)
			{	
				rv=min(rv,righto+lefto+1);
				rv=min(rv,righto+leftz+1);
				rv=min(rv,rightz+lefto+1);
			}
			else
			{
				rv=min(rv,righto+lefto+1);
			}
		}
	}
	return dp[value][kunta]=rv;
}

int main()
{
	int cn=0, t;
	cin>>t;
	while(t--)
	{
		cin>>m>>v; int g,c; int nnum=0;
		for(int i=0;i<(m-1)/2;i++)
		{
			cin>>g>>c;
			nnum++;
			arr[nnum]=node(0,g,c,0);
		}
		for(int i=0;i<(m+1)/2;i++)
		{
			cin>>g;
			nnum++;
			arr[nnum]=node(g,0,0,1);
		}
		CLR(dp,-1);
		lli rv=recur(v,1);
		cn++; 
		cout<<"Case #"<<cn<<": ";
		if(rv!=inf) cout<<rv<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
//		cout<<nnum<<' '<<m<<endl;
	}

	return 0;
}
