#include <iostream>
#include <fstream>
using namespace std;

int k;

int a[5010];


void advance(int& p, int cnt)
{
	while(cnt)
	{
		p = (p + 1)%k;
		if (a[p] == -1) cnt--;
	}
}

void gen()
{
	memset(a, -1, sizeof(a));
	int p = 0;
	for (int i = 0 ; i < k ; i++)
	{
		if (i) advance(p, i + 1);
		a[p] = i;
	}
}

int main()
{
	ifstream cin("small.in");
	ofstream cout("small.out");

	int z;
	cin>>z;
	for (int tc = 1 ; tc <= z ; tc++)
	{
		::cout<<tc<<'/'<<z<<endl;
		cout<<"Case #"<<tc<<": ";
		
		cin>>k;
		gen();

		int q;
		cin>>q;
		while(q--)
		{
			int x;
			cin>>x;
			cout<<a[x - 1]+1<<' ';
		}
		cout<<endl;
	}
}