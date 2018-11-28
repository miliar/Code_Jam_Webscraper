#include <bitset>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	ifstream in(argv[1]);
	int t, n, k;
	in>>t;

	int c = 0;
	// write to file
	ofstream o("a.out");
	while(t--)
	{
		in>>n>>k;
		unsigned long  y = 0;
		for(int i=1; i<=k; i++)
		{
			bitset<64> b(y);
			if(!b.test(n-1))
			{
				b.set(n-1);
			}
			else
			{
				for(int j=n-1; j>=0; --j)
				{
					if (b.test(j))
						b.reset(j);
					else
					{
						b.set(j);
						break;
					}
				}
			}
			y = b.to_ulong();
		}
	
		string s = "ON";
		bitset<64> x(y);
		for(int i=n-1; i>=0; --i)
		{
			if (!x.test(i))
			{
				s = "OFF";
				break;
			}
		}		
		o<<"Case #"<<++c<<": " << s <<endl;
	}
}
