#include<iostream>
#include<cstdio>
using namespace std;
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<map>
#include<vector>
#include<queue>
#define mymax(a,b) (a)>(b)?(a):(b)
#define mymin(a,b) (a)<(b)?(a):(b)
#define fi(i,a,b) for(i=a;i<=b;i++)
#define fir(i,a,b) for(i=a;i>=b;i--)
typedef long long int ll;

// function for priority queue
// arranges pairs in decreasing order of first element
class mycomparison
{ 
public:
  bool operator() (const pair<int, pair<int,int> >& lhs, const pair<int, pair<int,int> >& rhs) const
  {
    return (lhs.first>rhs.first);
  }
};


ll func(int n,int m,ll *nval,ll *ntype,ll *mval,ll *mtype,int i,int j)
{
	ll ans=0,tmp1,tmp2;
	
	if(i==n || j==m)
	return 0;
	
	if(ntype[i]==mtype[j])
	{
		if(nval[i]<mval[j])
		{
			ans += nval[i];
			mval[j] = mval[j] - nval[i];
			ans += func(n,m,nval,ntype,mval,mtype,i+1,j);
			mval[j] = mval[j] + nval[i];
		}
		else
		{
			ans += mval[j];
			nval[i] = nval[i] - mval[j];
			ans += func(n,m,nval,ntype,mval,mtype,i,j+1);
			nval[i] = nval[i] + mval[j];
		}
	}
	
	else
	{
			tmp1 = func(n,m,nval,ntype,mval,mtype,i+1,j);
			tmp2 = func(n,m,nval,ntype,mval,mtype,i,j+1);
			
			if(tmp1>tmp2)
			{
				ans = tmp1;
			}
			else
			{
				ans = tmp2;
			}
	}

	//cout<<i<<" "<<j<<" "<<ans<<'\n';
	return ans;
}



int main()
{
	int t,k,i,n,m;
	ll nval[101], mval[101], ntype[101], mtype[101];
	ll ans;
	cin>>t;
	
	for(k=1;k<=t;k++)
	{
		
		cin>>n>>m;
		
		fi(i,0,n-1)
		cin>>nval[i]>>ntype[i];
		
		fi(i,0,m-1)
		cin>>mval[i]>>mtype[i];
		
		
		ans = func(n,m,nval,ntype,mval,mtype,0,0);
		
		cout<<"Case #"<<k<<": "<<ans<<'\n';
	}
	
	return(0);
}

