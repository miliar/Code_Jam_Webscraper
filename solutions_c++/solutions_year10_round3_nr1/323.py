#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void iter(int ind)
{
   	int n;
	cin >> n;

	vector<int> a,b;

	for(int i=0; i<n; ++i)
	{
		int temp,temp2;
		cin >> temp >> temp2;
		a.push_back(temp);
		b.push_back(temp2);		
	}

	int cnt=0;
	for(int i=0; i<n; ++i)
	{
		for(int j=0; j<n; ++j)
		{
			if ((a[i]>a[j] && b[i]<b[j]) || (a[i]<a[j] && b[i]>b[j]))
				cnt++;
		}
	}

	cout << "Case #" << ind << ": " << cnt/2 << endl;	
}

int main()
{
	int t;
	cin >> t;

	for(int i=0; i<t; ++i)
		iter(i+1);

	return 0;
}
