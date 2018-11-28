#include <list>
#include <iostream>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	long long p, k, l,z, tests;
	ifstream in("C:\\large.in");
	if(!in)
	{
		cout << "Cannot open input file.\n";
		return 1;
	}
	char str[100000];
	in.getline(str,100000);
	istringstream iss(str, istringstream::in);
	iss >> tests;
	for (int w = 0; w< tests; w++)
	{
		in.getline(str,100000);
		istringstream iss2(str, istringstream::in);
		iss2 >> p;
		iss2 >> k;
		iss2 >> l;
		in.getline(str,100000);
		istringstream iss3(str, istringstream::in);
		list<long long> numList;
		list<long long>::reverse_iterator myIter;
		for (int i = 0; i<l ; i++)
		{
			iss3 >> z;
			numList.push_back(z);
		}
		numList.sort();
		long long sum = 0;
		myIter=numList.rbegin();
		long long counter = 0;
		long long c2 = 0;
		for (int m = 0; m<l; m++)
		{
			
			if(counter > p)
			{
				cout << "Impossible";
				break;
			}
			for (int j = 0; j<k; j++)
			{
				sum = (*myIter)*(m+1) +sum;
				myIter++;
				c2++;
				if (c2 >= l)
					break;
			}
			if(c2 >= l)
				break;
			counter ++;
		}
		cout << "Case #" << w+1 << ": " << sum << endl;
	}
	
	
}