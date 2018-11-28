#include<iostream>
#include<algorithm>
using namespace std;
int tt, ii;
int mabs(int a)
{
	if (a<0)
		a*=-1;
	return a;
}
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d\n", &tt);
	int n, i, j, sm = 0, p1, p2, p, t, b;
	bool fl, fl1;
	char c;
	for(ii = 1; ii<=tt; ii++)
	{
		cin>>n;
		sm = 0; 
		p1 = p2 = 1;
		p = 0;
		t = 0;
		cin>>c>>p;
		fl = (c == 'O');
		i = 1;
		while(i<=n)
		{
			fl1 = (c == 'O');
			if(fl == fl1)
			{
				if(c=='O')
				{
					t +=  mabs(p2 - p)+1;
					p2 = p;
				}
				else
				{
					t +=  mabs(p1 - p)+1;
					p1 = p;
				}
			}
			else
			{
				sm += t;
				if(c=='O')
				{
					b =  mabs(p2 - p);
					p2 = p;
				}
				else
				{
					b =  mabs(p1 - p);
					p1 = p;
				}
				if(t>=b)
					t = 1;
				else
					t = b - t + 1; 
			}
			fl = fl1;
			if(i<n) cin>>c>>p;
			i++;
		}
		sm += t;
		printf("Case #%d: %d\n", ii, sm);
	}
	return 0;
}