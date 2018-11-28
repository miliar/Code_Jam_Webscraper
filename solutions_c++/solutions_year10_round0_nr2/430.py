
#include <iostream>
#include <cstdio>
using namespace std;

void swap(int &x, int &y)
{
	int tmp;
	tmp = x;
	x = y;
	y = tmp;
}

int gcd(int x,int y)
{
	if (x<y) swap(x,y);
	while (x!=y)
	{
		if (x%y == 0)
		{
			x = y;
		}
		else
		{
			x = x%y;
			swap(x,y);
		}
	}
	return x;
}

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int caseNum;
	int num[3];
	int ans;
	int n;
	int x;

	cin >> caseNum;

	for (int crtCase=1; crtCase<caseNum+1; crtCase++)
	{
		cin >> n;

		for (int i=0; i<n; i++)
		{
			cin >> num[i];
		}

		if (n == 3)
		{
			if (num[0]>num[1]) {swap(num[0],num[1]);}
			if (num[0]>num[2]) {swap(num[0],num[2]);}
			if (num[1]>num[2]) {swap(num[1],num[2]);}
		}
		else
		{
			if (num[0]>num[1]) {swap(num[0],num[1]);}
		}

		if (n == 2)
		{
			if (num[1] == num[0]) x = 1; else x = num[1] - num[0];
			ans = num[0] % x;
			if (ans!=0) ans = x-ans;
		}
		else
		{
			if (num[1] == num[0])
			{
				if (num[2] == num[1]) x = 1; else x = num[2] - num[1];
				ans = num[0] % x;
				if (ans!=0) ans = x-ans;
			}
			else
			{
				x = num[1] - num[0];
				if (num[2] != num[1]) x = gcd(x,(num[2]-num[1]));
				ans = num[0] % x;
				if (ans!=0) ans = x-ans;
			}
		}

		cout<<"Case #"<<crtCase<<": ";
		cout<<ans;
		cout<<endl;
	}
	return 0;
}
