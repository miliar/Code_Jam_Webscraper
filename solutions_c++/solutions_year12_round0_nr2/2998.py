#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
	int t,s,p,n,i,j,a[102],jum,jml=0;
	vector<int> v[102];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n>>s>>p;
		jml=0;
		for(j=0;j<n;j++)
		{
			cin>>a[j];
		}
		stable_sort(a,a+n);
		for(j=0;j<n;j++)
		{
			jum=a[j]/3;
			v[j].push_back(jum);
			if(a[j]%3==0)
			{
				v[j].push_back(jum);
				v[j].push_back(jum);
			}
			else if(a[j]%3==1)
			{
				v[j].push_back(jum);
				v[j].push_back(jum+1);
			}
			else
			{
				v[j].push_back(jum+1);
				v[j].push_back(jum+1);
			}
			//cout<<jum<<endl;
			//stable_sort(v[j].begin(),v[j].end());
		}
		//stable_sort(v,v+3);
		for(j=n-1;j>=0;j--)
		{
			if(s==0)
				break;
			if(a[j]%3!=1&&a[j]!=0&&v[j][2]<p)
			{
			   v[j][2]++;
			   v[j][1]--;
				s--;
			}
			
			
		}
		for(j=0;j<n;j++)
		{
			//cout<<v[j][2]<<endl;
			if(v[j][2]>=p)
				jml++;
			v[j].clear();
			
		}
		cout<<"Case #"<<i+1<<": "<<jml<<endl;
	}
	return 0;
}