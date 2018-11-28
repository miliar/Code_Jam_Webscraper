#include<iostream>
#include<string>
#include<vector>
#include<set>
using namespace std;


int main()
{

	freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\gcj\\B-small-attempt0.in","r",stdin);
	freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\gcj\\B-small-attempt0.out","w",stdout);

	int cas;
	cin>>cas;
	for(int cs=1;cs<=cas;cs++)
	{
		int n,k,b,t;
		cin>>n>>k>>b>>t;
		vector<int> x(n),v(n);
		vector<bool> r(n,false); 
		for(int i=0;i<n;i++)
			cin>>x[i];
		for(int i=0;i<n;i++)
			cin>>v[i];
		int res=0;
		int cnt=0;
		for(int i=n-1;i>=0&&k;i--)
		{
			if(t*v[i]>=b-x[i])
			{
				r[i]=true;
				k--;
				res+=cnt;
			}
			else
			{
				cnt++;
			}
		}
		if(k)
			cout<<"Case #"<<cs<<": "<<"IMPOSSIBLE"<<"\n";
		else
			cout<<"Case #"<<cs<<": "<<res<<"\n";
	}
}