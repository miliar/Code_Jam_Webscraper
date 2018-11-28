#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;
double solve(int a, int b, vector<double> &p);
int main()
{
	std::ifstream f("A-small-attempt2.in");
	std::ofstream o("result1-1.txt");

	int size;
	f >> size;
	
	for(int i = 0; i < size; i++)
	{
		int a, b;
		
		f >> a >> b;
		vector<double >p(a);
		for(int j = 0; j < a; j++)		
			f >> p[j];
		
		double result = solve(a,b,p);
	



		std::cout << "Case #" << i+1 << ": " << result << std::endl;
		o << fixed;
		o << setprecision (6) << "Case #" << i+1 << ": " << result << std::endl;
	}
	return 0;
}

double solve(int a,int b, vector<double> &p)
{
	vector<double> result;
	vector<double> p2;
	double ori = 1.0;
	for(int i = 0; i < (int)p.size(); i++)
		ori *= p[i];
	p2.push_back(ori);
	for(int i = (int)p.size()-1; i >= 0; i--)
	{
		ori /= p[i];
		p2.push_back(ori * (1 - p[i]));		
	}
	double keep = .0;
	vector<double> back(a);
	for(int i = 0; i < (int)p2.size(); i++)
	{
		//keep
		if( i != 0)
			keep += p2[i] * (b + 1 + (b - a) + 1);
		else
			keep += p2[i] * ( (b-a) +1 );
	}
	result.push_back(keep);
	for(int j = 1; j < a+1; j++)	
	{
		//backspace
		double tt =.0;
		for(int i = 0; i < (int)p2.size(); i++)
		{
			int t = (j*2 + b - a + 1);
			if(j < i)
				t += b+1;
			tt += p2[i] * t;
		}
		result.push_back(tt);
	}
	//enter
	double enter = .0;
	for(int i = 0; i < (int)p2.size(); i++)
	{
		enter += p2[i] * (b+2);	
	}
	result.push_back(enter);

	sort(result.begin(),result.end());
	return result[0];
}