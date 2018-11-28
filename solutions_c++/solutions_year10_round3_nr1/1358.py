#include<iostream>
#include<vector>

using namespace std;

int main()
{
	int i,j,ii,k,t,n,cnt;
	vector<int>a,b;
	cin>>t;
	for(ii=0;ii<t;ii++)
	{
		cnt=0;
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>k;
			a.push_back(k);
			cin>>k;
			b.push_back(k);
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[j]>a[i]&&b[i]>b[j])
					cnt++;
			}
		}
		//cout<<"Case #"<<ii+1<<": "<<cnt<<endl;
		cout<<"Case #"<<ii+1<<": "<<cnt<<endl;
		a.clear();
		b.clear();
	}
}
