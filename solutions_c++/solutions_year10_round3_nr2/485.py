#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	freopen("d:\\gj\\r1c\\A-large(2).in","r",stdin);
//	freopen("d:\\gj\\r1c\\a.txt","r",stdin);
	freopen("d:\\gj\\r1c\\ao.txt","w",stdout);
	int l,p,c,ans;
	double k;
	int rp,ri;
	cin>>rp;
	for (ri=1;ri<=rp;ri++)
	{
		ans=0;
		cin>>l>>p>>c;
		k=1.0*p/l;
		while (k-1e-8>c)
		{
			k=sqrt(k);
			ans++;
		}
		cout<<"Case #"<<ri<<": "<<ans<<endl;
	}
	return 0;
}

