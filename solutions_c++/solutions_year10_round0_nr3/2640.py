#include <iostream>
#include <vector>

using namespace std;

int t,r,k,n;
vector<int> vec_g;

int slove(int r,int k,vector<int> vec_g)
{
	int i,j,cnt=0;
	int sum=0;
	while(r--)
	{
		cnt=0;
		for(i=0;i<vec_g.size();i++)
		{
			if((cnt+vec_g[i])<=k)
				cnt+=vec_g[i];
			else
				break;
		}
		j=0;
		while(j<i)
		{
			vec_g.push_back(vec_g[0]);
			vec_g.erase(vec_g.begin());
			j++;
		}
		sum+=cnt;
	}
	return sum;
}

int main()
{
#ifdef _DEBUG
   freopen("C-small-attempt4.in","r",stdin);
   freopen("C-small-attempt4.out","w",stdout);
#endif
	int i,data,j=1;
	cin>>t;
	while(t--)
	{
		cin>>r>>k>>n;
		for(i=0;i<n;i++)
		{
			cin>>data;
			vec_g.push_back(data);
		}
		cout<<"Case #"<<j<<": ";
		cout<<slove(r,k,vec_g)<<endl;
		vec_g.clear();
		j++;
	}
	return 0;
}