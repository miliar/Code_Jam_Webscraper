// ga.cpp : Defines the entry point for the console application.
//

#include <fstream>
using namespace std;
int t;
int n[10000];
int k[10000];
int l[10000];

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin >> t;
	for (int i=0;i<t;i++)
	{
		cin >> n[i] >> k[i];
	}
	for (int i=0;i<t;i++)
	{
		l[i]=1;
		for (int j=1;j<=n[i];j++) l[i]=l[i]*2;
		if (k[i]%l[i]==(l[i]-1)%l[i])
		{
			cout << "Case" << " #";
			cout << i+1;
			cout << ": ON";
			cout << "\n";
		}
		else 
		{
			cout << "Case" << " #";
			cout << i+1;
			cout << ": " << "OFF";
			cout << "\n";
		}
	}
	return 0;
}

