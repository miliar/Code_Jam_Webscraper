#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int p[1010];

int getp(int x)
{
	if (p[x] == x) return x;
	return p[x] = getp(p[x]);
}

bool prime[1010];

bool isprime(int x)
{
	if (x <= 1) return false;
	if (x == 2) return true;
	for (int i = 2 ; i * i <= x ; i++) 
		if (x % i == 0) return false;

	return true;
}

bool ok(int x, int y, int pr)
{
	int p = pr;
	while(p <= x && p <= y)
	{
		if (prime[p] && x % p == 0 && y % p == 0) return true; 
		p++;
	}

	return false;
}

int main()
{
	// ifstream cin("a.txt");
	ifstream cin("small.in");
	ofstream cout("small.out");

	int z;
	for (int i = 1 ; i < 1010 ; i++) prime[i] = isprime(i);
	cin>>z;
	for (int tc = 1 ; tc <= z ; tc++)
	{
		::cout<<tc<<'/'<<z<<endl;
		int a, b, pr;
		cin>>a>>b>>pr;

		for (int i = a ; i <= b ; i++) p[i] = i;

		for (int i = a ; i <= b ; i++)
			for (int j = i + 1 ; j <= b ; j++)
				if (ok(i, j, pr)) p[getp(i)] = getp(j);

		set <int> s;
		for (int i = a ; i <= b ; i++)
			s.insert(getp(i));

		cout<<"Case #"<<tc<<": "<<s.size()<<endl;

	}
}