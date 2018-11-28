#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
using namespace std;

int d[20], n;

int main()
{
	ifstream cin("C-large.in");
	ofstream cout("a.out");
	//ifstream cin("a.txt");

	int tot, count = 1, sum, total;
	cin>>tot;
	while (tot--)
	{
		cin>>n;
		total = sum = 0;
		for (int i = 0; i < n; i++)
		{
			cin>>d[i];
			sum ^= d[i];
			total += d[i];
		}
		if (sum)cout<<"Case #"<<count++<<": NO"<<endl;
		else {
			sort(d, d + n);
			cout<<"Case #"<<count++<<": "<<total - d[0]<<endl;
		}
	}
	return 0;
}