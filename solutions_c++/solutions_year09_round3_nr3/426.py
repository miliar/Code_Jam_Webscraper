#include <iostream>

using namespace std;

int main()
{
	int m;
	cin>>m;
	for (int q=1;q<=m;q++)
	{
		int a,b;
		cin>>a>>b;
		
		int c[10];
		for (int i=0;i<b;i++)
			cin>>c[i];
		
		cout<<"Case #"<<q<<": ";
		
		int p[111],gr=99999999;
		
		
		sort(c,c+b);
		do
		{
			//for (int i=0;i<b;i++)
				//cout<<c[i]<<' ';
			//cout<<endl;
			for (int i=0;i<=100;i++)
		p[i]=1;
		p[0]=0;
		p[a+1]=0;
			int r=0;
			for (int i=0;i<b;i++)
			{
				int u=c[i];
				p[u]=0;
				int t=u+1;
				while (p[t])
					r++,t++;
				t=u-1;
				while (p[t])
					r++,t--;
			}
			//cout<<r<<endl;
			gr=min(r,gr);
		}
		while (next_permutation(c,c+b));
		cout<<gr<<endl;
	}
	return 0;
}
