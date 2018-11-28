#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;

int t;
int n;



ofstream out("out.txt");

int d[10000];


int main()
{
	cin >> t;
	int count = 1;
	while(--t >= 0)
	{
		cin >> n;
		int temp = 0;
		for(int i = 0;i < n;i ++)
		{
			cin >> d[i];
			temp ^= d[i];
		}
		if(temp != 0)
		{
			out <<"Case #" << count ++ << ": " <<  "NO" << endl;
			continue;
		}
		sort(d, d + n);
		temp = 0;
		for(int i = 1;i < n;i ++)
			temp += d[i];	

		
		out <<"Case #" << count ++ << ": " <<  temp << endl;
	}



	return 0;
}