#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;

bool is_ok(vector<vector<bool> > & v)
{

}
int main()
{

	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		cin>>n;
		vector<vector<int > > v(n,vector<int>(n,0));
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n;k++)
			{
				char c;
				cin>>c;
				v[j][k]=c-'0';
			}
		}
		int cur=0;
		int  ans=0;
			while(cur < n)
			{
		/*		for(int j=0;j<n;j++)
				{
					for(int k=0;k<n;k++)
					{
						cout<<v[j][k]<<" ";
					}
					cout<<endl;
				}*/
				//cout<<cur<<endl;
				bool rowok=true;
				for(int j=cur+1;j<n;j++)
				{
					if(v[cur][j])
					{
						rowok=false;
						break;
					}
				}
				if (rowok)
				{
					cur++;
					continue;
				}
				else 
				{
					for(int j=cur+1;j<n;j++)
					{
						bool ok=true;
						for(int k=cur+1;k<n;k++)
						{	
							if(v[j][k])
							{
								ok=false;
								break;
							}
						}
						if(ok)
						{
							vector<int> temp=v[j];
							v.erase(v.begin()+j);
							v.insert(v.begin()+cur,temp);
							ans+=(j-cur);
							break;
						}		
					}
		//			cout<<ans<<endl;
					cur++;
				}
			}
			//cout<<ans<<endl;
			printf("Case #%d: %d\n",i,ans);


	}
	return 0;
}
