#include <algorithm>
//#include <iostream>
#include <vector>
//#include <string>
#include <fstream>
using namespace std;


int main()
{
	ifstream infile;
	infile.open("A-small-attempt0.in.txt");
	ofstream outfile;
	outfile.open("A-small-attempt0.out.txt");
	
	int T, n;
	vector<int> x;
	vector<int> y;

	infile>>T;
	int i, j, v, res;


	i = 0;
	while (i<T)
	{
		x.clear();
		y.clear();
		res = 0;

		infile>>n;
		//getline(infile, temp);
		for (j=0; j<n; j++)
		{
			infile>>v;
			x.push_back(v);
		}
		for (j=0; j<n; j++)
		{
			infile>>v;
			y.push_back(v);
		}

		sort(x.begin(), x.end());
		sort(y.begin(), y.end());

		for (j=0; j<n; j++)
		{
			res += x[j]*y[n-j-1];
		}
	
		outfile<<"Case #"<<i+1<<": "<<res<<endl;

		i++;
	}

	infile.close();
	outfile.close();

	return 0;
}

