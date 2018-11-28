#include <iostream>
#include <fstream>

using namespace std;

long long T,N,Pd,Pg;

long long gcd(long long a,long long b)
{
	long long t;
	while (b!=0)
	{
		t=b;
		b=a%b;
		a=t;
	}
	return a;
}

bool solve()
{
	int a,b,D,G;
	a=gcd(100,Pd);
	b=gcd(100,Pg);
	/*if (!a&&!b)
		return true;
	if (!a&&b)
		return true;
	if (a&&!b)
		return false;*/
	a=Pd*100/a;
	b=Pg*100/b;
	//cout << a << " " << b << endl;
	if (!Pd&&Pg==100)
		return false;
	if (!Pd&&!Pg)
		return true;
	if (!Pd&&Pg)
		return true;
	if (Pd&&!Pg)
		return false;
	if (Pg==100&&Pd!=100)
		return false;
	D=a/Pd;
	G=b/Pg;
	//cout << D << " " << G << endl;
	//cout << a/100 << " " << b/100 << endl;
	if (D>N)
		return false;
	return true;
}

int main()
{
	int i;
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin >> T;
	//cout << gcd(100,0);
	for (i=0;i<T;i++)
	{
		cin >> N >> Pd >> Pg;
		cout << "Case #" << i+1 << ": ";
		//cout << N << " " << Pd << " " << Pg << endl;
		if (solve())
			cout << "Possible" << endl;
		else
			cout << "Broken" << endl;/**/
	}
	return 0;
}