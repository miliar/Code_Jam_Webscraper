#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int t;
int n;

int d[2][2];
int a[2][2];

ofstream out("out.txt");


int main()
{
	cin >> t;
	int count = 1;
	while(--t >= 0)
	{
		//string prefix = "Case #" +  + ":";  
		cin >> n;
		d[0][0] = 1;
		d[0][1] = 1;
		a[0][0] = 0;
		a[0][1] = 0;
		for(int i = 0;i < n;i ++)
		{
			char tag;
			int num;
			cin >> tag >> num;
			if(tag == 'O')
			{
				int temp = d[0][0];
				d[0][0] = num;
				a[0][0] = max(a[0][0] + abs(num - temp) + 1,a[0][1] + 1);
			}
			else
			{
				int temp = d[0][1];
				d[0][1] = num;
				a[0][1] = max(a[0][1] + abs(num - temp) + 1,a[0][0] + 1);
			}

		}
		int ret = max(a[0][0],a[0][1]);
		out <<"Case #" << count ++ << ": " <<  ret << endl;
	}



	return 0;
}