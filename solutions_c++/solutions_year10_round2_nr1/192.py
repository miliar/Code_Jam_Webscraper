#include<iostream>
#include<map>
#include<vector>
#include<string>

using namespace std;



typedef map<string,int>msi;


vector<msi>st;


int main()
{
	int n,m;
	int t,cas;
	int i,j;
	int ans;

	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);

	cas=0;
	scanf("%d",&t);
	
	for (cas=1;cas<=t;cas++)
	{
		cin>>n>>m;
		ans=0;
		st.resize(1);
		st[0].clear();

		for (i=0;i<n;i++)
		{
			string path;
			cin>>path;
			vector<string> va;

			path+='/';
			int pre=1;
			for (j=1;j<path.size();j++)
				if (path[j]=='/')
				{
					va.push_back(path.substr(pre,j-pre));
					pre=j+1;
				}
			pre=0;
			for (j=0;j<va.size();j++)
			{
				if (st[pre].find(va[j])==st[pre].end())
				{
					msi tmp;
					st[pre][va[j]]=st.size();
					st.push_back(tmp);
				}
				pre=st[pre][va[j]];
			}		
		}

		for (i=0;i<m;i++)
		{
			string path;
			cin>>path;
			vector<string> va;

			path+='/';
			int pre=1;
			for (j=1;j<path.size();j++)
				if (path[j]=='/')
				{
					va.push_back(path.substr(pre,j-pre));
					pre=j+1;
				}
			pre=0;
			for (j=0;j<va.size();j++)
			{
				if (st[pre].find(va[j])==st[pre].end())
				{
					msi tmp;
					st[pre][va[j]]=st.size();
					st.push_back(tmp);
					ans++;
				}
				pre=st[pre][va[j]];
			}		
		}
		printf("Case #%d: %d\n",cas,ans);		
	}
	
	return 0;
}
