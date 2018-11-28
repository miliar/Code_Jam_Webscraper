#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <limits>
#include <iomanip>
using namespace std;

int main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("out.txt");
	
	int n;
	in>>n;
	int done = 0;
	int all = 0;
	vector<double>perc;
	vector<double>  allperc;
	double p = 0.0;
	int caseno = 1;
	while(n--)
	{
		in>>done>>all;
		int m = done;
		perc.clear();
		double sum = 1.0;
		while(m--)
		{
			in>>p;
			sum *= p;
			perc.push_back(p);
		}
		allperc.clear();
		allperc.push_back(sum);
		allperc.push_back(1 - perc[0]);
		double d = perc[0];
		for(size_t i=1;i< done;i++)
		{
			allperc.push_back((1 - perc[i])*d);
			d *= perc[i];
		}
		vector<vector<int> > vec;
		vector<int> temp;
		temp.push_back(all - done +1);
		for(int i=0;i< done;i++)
			temp.push_back(all*2 - done +2);
		vec.push_back(temp);
		temp.clear();
		for(int i = 1;i<= done;i++)
		{	temp.clear();
			temp.push_back(all-done+1+2*i);
			for(int j=0;j< done;j++)
			{
				if(i< done-j)
				{
					temp.push_back(i*2+all-done+1+all+1);
				}
				else
				{
					temp.push_back(i*2+all-done+1);
				}
			}
			vec.push_back(temp);
		}
		temp.clear();
		for(int i=0;i< done+1;i++)
			temp.push_back(all+2);
		vec.push_back(temp);
		//double sum = 0.0;
		sum = 1.0;
		double mini = numeric_limits<double>::max();
		for(size_t i = 0;i< vec.size();i++)
		{
			sum = 0.0;		
			for(size_t j=0;j< vec[i].size();j++)
			{
				sum += allperc[j] * vec[i][j];
			}
			if (sum < mini)
				mini = sum;
		}
		out<<"Case #"<<caseno<<": "<<fixed<<setprecision(6)<<mini<<endl;
		++caseno;
	}
	
	return 0;
}