#include<vector>
#include<iostream>
#include<iomanip>
#include<set>
#include<string>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define f(i,n,m) for(int i=n;i<=(int)(m);i++)
#define rep(i, n) f(i,0,n-1)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
using namespace std;
int a[1111],b[1111];
int main()

{
		freopen("in.txt","r",stdin);
	
		freopen("out.txt","w",stdout);
	
	int t,n;
	cin>>t;
	f(ii,1,t)
	{
		cin>>n;
		rep(i,n)
			cin>>a[i]>>b[i];
		int cnt=0;	
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if(a[i]>a[j]&&	b[i]<b[j])
				cnt++;
				else if(a[i]<a[j]&&b[i]>b[j])
				cnt++;
			}
		}
		cout<<"Case #"<<ii<<": "<<cnt<<endl;
	}
//	system("pause");
	
	return 0;
}				
			
		
