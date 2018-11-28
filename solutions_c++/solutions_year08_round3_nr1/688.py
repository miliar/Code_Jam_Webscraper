#include "iostream"
#include "fstream"
#include "vector"
#include "algorithm"
#include "math.h"
using namespace std;

int greater(int a, int b)
{
	return a>b;
}
int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("Input.txt");
	outfile.open("Output.txt");
	int n;
	infile>>n;
	for(int i=0; i<n; i++)
	{
		int p, k, l;
		int res=0;
		vector <int> v;
		v.clear();
		infile>>p>>k>>l;
		for(int j=0; j<l; j++)
		{
			int tmp;
			infile>>tmp;
			v.push_back(tmp);
		}
		sort(v.begin(), v.end(), greater);
		int mul=1;
		for(int j=0; j<l; j++)
		{
			if(j>0 && j%k==0)
				mul++;
			res+=mul*v[j];
		}
	//	cout<<"Case #"<<i+1<<": "<<res<<endl;
		outfile<<"Case #"<<i+1<<": "<<res<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}