#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef unsigned int uint;
#define L 19

int main()
{
	const char *K = "welcome to code jam";
	
	string l;
	getline(cin, l);
	uint C=1;
	while (getline(cin,l))
	{
		vector<uint> t(L);
		for (uint i=0; i<l.length(); ++i)
		{
			for (uint j=0; j<L; ++j)
			{
				if (l[i] == K[j])
				{
					if (j==0) t[0]++; else 
						t[j] += t[j-1];
				} 
				t[j] %= 10000;
			}
		}
		
		cout << "Case #" << (C++) << ": ";
		cout.width(4);
		cout.fill('0');
		cout << t[L-1];
		cout << endl;
	}
	
	return 0;
}
