#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>

using namespace std;

int main()
{
	int t,i,e=0,c=0,r,k,n,x,ans=0,flag=0,j,m=0;
	vector<int> a,f;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.in");
	//ofstream fout("output.in");
	fin>>t;
	//cout<<t<<"\n";
	while(t--)
	{
		m++;
		ans=0;
		e=0;c=0;
		a.clear();
		f.clear();
		fin>>r>>k>>n;
		for(i=0;i<n;i++)
		{
			fin>>x;
			a.push_back(x);
		}
		i=0;
		while(e!=r)
		{
			e++;
			c=0;
			f.clear();
			flag=0;
			while(c<=k)
			{
				if(i>=a.size()) break;
				c+=a[i];
				if(c>k) break;
				else
				{
					f.push_back(a[i]);
					ans+=a[i];
					i++;
				}
			}
			for(j=0;j<f.size();j++)
				a.push_back(f[j]);
		}
		fout<<"Case #"<<m<<": "<<ans<<"\n";
	}
	return 0;
}
