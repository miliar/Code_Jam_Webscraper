#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>

#define MAX 1000000000000000000

using namespace std;


int main()
{
	unsigned long long ibuf,i=0,j=0,k=0,T=0,base,r,t;
	double dbuf=0;
	string sbuf="";
	stringstream ssbuf("");
	string symb;
	vector<unsigned int> num;
	
	cin >> T;
	
	for (i=0;i<T;i++)
	{
		symb.clear();
		num.clear();
		cin >> sbuf;
		for (j=0;j<sbuf.size();j++)
		{
			ibuf = symb.find(sbuf[j]);
			if (ibuf >= symb.size())
			{
				num.push_back(symb.size());
				symb += sbuf[j];
			}
		}
		if (symb.size()==1)
		{
			num.push_back(symb.size());
			symb+='_';
		}
		base = symb.size();
		
		sort(num.begin(),num.end());
		r = MAX;
		do
		{
			if (num[symb.find(sbuf[0])]==0)
				continue;
			t=0;
			for (j=0;j<sbuf.size();j++)
			{
				//std::cout << j << ":" << sbuf[sbuf.size()-j-1] << " " << symb.find(sbuf[sbuf.size()-j+1]) << " " << num[symb.find(sbuf[sbuf.size()-j+1])] << "\n";
				t += num[symb.find(sbuf[sbuf.size()-j-1])]*pow(base,j);
			}
				//std::cout << "\n";
			if (t < r)
				r= t;
		}
		while(next_permutation(num.begin(),num.end()));

		cout << "Case #" << i+1 << ": " << r << "\n";
	}
}

