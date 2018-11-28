#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef long long LINT;

void main()
{
	int t;
	cin>>t;
	for(int ii=0; ii<t; ii++)
	{
		int d[10000]={0,};
		int l[10000]={0,};
		int mm[10000]={0,};

		int n;
		cin>>n;
		for(int i=1; i<=n; i++)
			cin>>d[i]>>l[i];
		
		int dd;
		cin>>dd;

		d[0]=0;
		mm[0]=d[1];

		bool yes=false;
		for(int i=0; i<=n; i++)
		{
			for(int j=i+1; j<=n; j++)
			{
				if(d[i]+mm[i]>=d[j])
					mm[j]=max(mm[j],min(l[j],d[j]-d[i]));
				else
					break;
			}
			if(d[i]+mm[i]>=dd)
			{
				yes=true;
				break;
			}
		}
		
		cout<<"Case #"<<ii+1<<": "<<(yes ? "YES" : "NO")<<endl;
	}
}