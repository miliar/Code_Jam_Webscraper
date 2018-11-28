#include <iostream>

using namespace std;

int main()
{
	int l,d,n;
	cin>>l>>d>>n;
	string a[d],b;
	for (int i=0;i<d;i++)
		cin>>a[i];
	for (int i=1;i<=n;i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>b;
		int u=0;
		for (int j=0;j<d;j++)
		{
			int y=0,xd=1;
			for (int k=0;k<l;k++)
			{
				if (b[y]==a[j][k])
				{
					y++;
					continue;
				}
				if (b[y]!='(')
				{
					xd=0;
					break;
				}
				bool xdd=1;
				while (b[y]!=')')
				{
					if (b[y]==a[j][k])
						xdd=0;
					y++;
				}
				y++;
				if (xdd)
				{
					xd=0;
					break;
				}
			}
			if (xd)
				u++;
		}
		cout<<u<<endl;
	}
	return 0;
}