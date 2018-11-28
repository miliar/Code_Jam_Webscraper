
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int main()
{
	ifstream in("C-large.in");
	ofstream out("C-large.out");
	int T;

	in >> T;
	
	int i, j;
	string s;

	getline(in, s);

	for(i = 0; i < T; i++)
	{
		int N;
		in >> N;
		getline(in, s);
		
		int sum = 0;
		int min = -1; 
		int xorSum = 0;
		
		int cur;
		for(j = 0; j < N; j++)
		{
			
			in >> cur;
			if(cur < min)
				min = cur;
			else if(min < 0)
				min = cur; 
			
			sum += cur;
			xorSum = (xorSum ^ cur);
		}

		if(xorSum == 0)
		{
			out << "Case #" << i+1 << ": " <<  sum - min << endl; 
		}
		else out << "Case #" << i+1 << ": " <<  "NO" << endl; 
		
		getline(in, s);



	}
	return 0; 
}