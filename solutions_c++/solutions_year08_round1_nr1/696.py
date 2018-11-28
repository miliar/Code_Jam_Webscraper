#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
using namespace std;

void main()
{
	ifstream ip("A-small-attempt0.in");
	ofstream op("A-small-attempt0.out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return;
	}

	int N;
	ip>>N;

	for(int i=1;i<=N;++i)
	{
		int vals;
		ip>>vals;

		vector <int> num1,num2;

		for(int l =0;l<vals;++l)
		{
			int tmp;
			ip>>tmp;
			num1.push_back(tmp);
		}
		for(int j =0;j<vals;++j)
		{
			int tmp;
			ip>>tmp;
			num2.push_back(tmp);
		}
		sort(num1.begin(),num1.end());
		sort(num2.begin(),num2.end());
		long retval = 0;

		for(int k=0;k<vals;++k)
			retval += num1[k]*num2[num2.size()-k-1];
		op<<"Case #"<<i<<": "<<retval<<endl;
	}
	op.close();
}