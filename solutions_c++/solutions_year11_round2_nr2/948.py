
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

double func(int D, vector<int> P, vector<int> num)
{
    int sum;
	double m;
	int i, j, k;

	double max = 0.0; 

	int size = P.size();

	for(i = 1; i <= size; i++)
	{
		for(j = 0; j < size - i + 1; j++)
		{
			int sum = 0;
			for(k = j; k < j+i; k++ )
			{
				sum += (num[k]);

			}
			int range = P[j + i - 1] - P[j];

			double val = ((sum - 1.0) * D - range)/2.0;

			if(val > max)
				max = val;
		}
	}
	 

	return max; 
}
int main()
{
	ifstream in ("B-small-attempt0.in");
	ofstream out ("B-small-attempt0.out");

	string s; 
	
	int T;
	in >> T;
	int i, j; 
	getline(in, s); 
	for(i = 0; i < T; i++)
	{
		int C, D; 
		in >> C >> D;
		getline(in, s); 
		
		vector<int> P;
		vector<int> num; 
		int a, b;
		for(j = 0; j < C; j++)
		{
			in >> a >> b;
			P.push_back(a);
			num.push_back(b);
			getline (in, s); 
			 
		}
		out << "Case #" << i + 1 << ": ";
		out << func(D, P, num) << endl;

	}
	return 0; 
}

