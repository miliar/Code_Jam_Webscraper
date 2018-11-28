#include <iostream>
using namespace std;
int main()
{
//	freopen("d:\\gj\\r1c\\A-small-attempt0.in","r",stdin);
	freopen("d:\\gj\\r1c\\a.txt","r",stdin);
	freopen("d:\\gj\\r1c\\co.txt","w",stdout);
	int a[2000],b[2000];
	int n,i,j;
	int ri,rp,ans=0;
	cin>>rp;
	for (ri=1;ri<=rp;ri++)
	{
		cin>>n;
		ans=0;
		for (i=0;i<n;i++)
			cin>>a[i]>>b[i];
		for (i=0;i<n;i++)
			for (j=i;j<n;j++)
			{
				if (a[i]<a[j] && b[i]>b[j] || a[i]>a[j] && b[i]<b[j]) ans++;
				//if () ans++;
			}
		cout<<"Case #"<<ri<<": "<<ans<<endl;
	}
	return 0;
}

