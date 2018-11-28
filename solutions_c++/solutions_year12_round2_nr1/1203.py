#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>

using namespace std;
int main()
{
	ifstream input("input_a.txt");
	FILE* f = fopen("output_a.txt", "w");
	int t;
	input >> t;
	for (int i = 0; i < t; ++i)
	{
		std::vector < double> results;
		if (i!=0)
			fprintf(f, "\n");
		int n;
		input >> n;
		vector< int > s;
		int sum = 0;
		for (int j = 0; j < n; ++j)
		{
			int tmp;
			input >> tmp;
			s.push_back(tmp);
			sum += tmp;
			//std::cout << tmp << "\n";
		}
		//std::cout << "sum=" << sum << "\n";
		fprintf(f, "Case #%d:", i+1);
		for (int j = 0; j < n; ++j)
		{
			double a = sum * n;
			
			double b = sum * 2 - s[j]*n;
			double res = b/a*100;
			//std::cout << a << " " << b << " " << res << std::endl;
			//fprintf(f, " %.6f", res);
			//if (res > -0.000001)
				results.push_back(res);
			//else
			//	results.push_back(0);
		}
		double ssum = 0;
		int k = 0;
		for (int j = 0; j < n; ++j)
			if (results[j] >= 0)
			{
				ssum += s[j];
				k++;
			}
		if (k == n)
		{
			for (int j = 0; j < n; ++j)
				fprintf(f, " %.6f", results[j]);
			continue;
		}
		for (int j = 0; j < n; ++j)
		{
			if (results[j] < 0)
			{
				double ff = 0;
				fprintf(f, " %.6f", ff);
				continue;
			}
			double a = sum * k;
			double b = sum + ssum - k*s[j];
			double res = b / a;
			if (res < 0)
				std::cout << "WARNING!!!!!!!!!!!!!!!!!" << std::endl;
			fprintf(f, " %.6f", res * 100);
		}
		
	}
	
	input.close();
	fclose(f);
	return 0;
}