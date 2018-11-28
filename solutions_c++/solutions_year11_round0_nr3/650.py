#include<iostream>

using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		int n;
		cin>>n;
		int x = 0, s = 0,m = 1000001;
		for(int i=0;i<n;i++)
		{
			int t;
			cin>>t;
			x^=t;
			m=min(m,t);
			s+=t;
		}
		if(x) puts("NO");
		else printf("%d\n",s-m);
		
	}
	return 0;
}
