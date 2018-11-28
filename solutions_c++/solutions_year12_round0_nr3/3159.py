#include <fstream>
#include <iostream>
#include <conio.h>
#include <cmath>

using namespace std;

int digits (int d)	{
	int ans=0;
	while (d)	{
		d=d/10;
		ans++;
	}
	return ans;
}
int expo (int n)	{
	if (n==1) return 10;
	else return 10*expo(n-1);
}

//int q3()	{
int main()	{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("c-small.txt", ios::ate);
	int t=1, count;
	fin >> t;
	//cin >> t;
	for (count=1; count <= t; count++)	{
		int a, b, n, m, d, i, ans=0;
		
		fin >> a >> b;
		//cin >> a >> b;
		
		for (n=a; n<=b; n++)	{
			d= digits (n);
			//cout << d << " ";
			for (i=1; i<d;i++)	{
				m=(n/expo(i)+(n%expo(i))*expo(d-i));
				if (m>n && m<=b)	ans++;
			}
		}

		fout<<"Case #"<<count<<": "<<ans<<"\n";
		//cout<<"Case #"<<count<<": "<<ans<<"\n";
	}
	getch();
	return 0;
}