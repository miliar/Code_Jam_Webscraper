#include <iostream>

using namespace std;

#define fi(n) for (int i=0;i<n;i++)
#define fj(n) for (int j=0;j<n;j++)
#define sz size()

int main()
{
	int cc;
	cin>>cc;
	for (int xx=0;xx<cc;xx++)
	{
		int k,mu=9999;
		cin>>k;
		int a[k];
		fi(k)a[i]=i;
		string s;cin>>s;
		do
		{
		//	fi(k)cout<<a[i]<<' ';
		//	cout<<endl;
			string dd="",ss=s;
			while(ss.sz)
			{
				
				fi(k)
				dd+=ss[a[i]];
				ss.erase(0,k);
				
			}
		//	cout<<dd<<endl;
			int uu=1;
			for (int i=1;i<dd.sz;i++)
			if (dd[i]!=dd[i-1])
				uu++;
		//	cout<<uu<<endl;
			mu=min(uu,mu);
		}
		while (next_permutation(a,a+k));
		cout<<"Case #"<<xx+1<<": "<<mu<<endl;
	}
	return 0;
}