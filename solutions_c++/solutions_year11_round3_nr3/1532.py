#include <iostream>
#include <algorithm>
using namespace std;

#include <fstream>
using std::ifstream;
using std::ofstream;


int main()
{
	ifstream indata;
	ofstream outdata;
	int t;
	indata.open("C-small-attempt0.in");
	outdata.open("C.txt");
	indata>>t;
	for(int i = 1; i <= t; i++)
	{
		
		int n,l,h;
		indata>>n>>l>>h;
		int a[n], k;
		indata>>a[0];
		int flag = 0;
	//	int lcm = a[0];
		for(int j = 1; j < n; j++)
		{
			indata>>a[j];
		}
		std::sort(a, a + n);

		for(int j = l; j <= h; j++)
		{
			for(k = 0; k < n; k++)
			{
				if((a[k] % j != 0) && (j % a[k] != 0))
					break;
			}

			if(k == n)
			{
				outdata<<"Case #"<<i<<": "<<j<<"\n";
				flag = 1;
				break;
			}
		}

		if(flag == 0)
			outdata<<"Case #"<<i<<": NO\n";
	}
	indata.close();
	outdata.close(); 
}
