#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

#define N 110
int p[N];
char ch[N];

int solve(int n)
{
	int d[N];
	d[0] = 0;
	d[1] = p[1];
	p[0] = 1;

	for (int i = 2; i <= n; i++)
	{
		if (ch[i] == ch[i - 1])
		{
			d[i] = d[i - 1] + abs(p[i] - p[i - 1]) + 1;
		}
		else 
		{
			int j = i - 1;
			for (; j >= 1; j--)
				if (ch[j] == ch[i])break;

			int time = abs(p[i] - p[j]);
			if (d[j] + time > d[i - 1])
				d[i] = d[j] + time + 1;
			else d[i] = d[i - 1] + 1;
		}
	}
	//for (int i = 0; i <= n; i++)
	//	cout<<d[i]<<" ";
	//cout<<endl;
	return d[n];
}
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("a.out");
	int tot, n, count = 1;

	cin>>tot;
	while(tot--)
	{
		cin>>n;
		//cout<<n<<endl;
		for (int i = 1; i <= n; i++)
		{
			cin>>ch[i]>>p[i];
			//cout<<ch[i]<<" "<<p[i]<<endl;
		}
		cout<<"Case #"<<count++<<": "<<solve(n)<<endl;
	}
	return 0;
}