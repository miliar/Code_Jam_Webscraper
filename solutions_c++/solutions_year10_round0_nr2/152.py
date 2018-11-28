#include "bigint.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int main()
{
	int nr;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> nr;
	for(int cases=1;cases<=nr;cases++)
	{
		BigInt a;
		deque <BigInt> vec;
		int n;
		fin >> n;
		for(int i=0;i<n;i++)
		{
			fin >> a;
			vec.push_back(a);
		}
		sort(vec.begin(),vec.end());
		BigInt max=vec[vec.size()-1];
		for(int i=vec.size()-1;i>0;i--)
		{
			vec[i]=vec[i]-vec[i-1];
		}
		vec.pop_front();
		while (vec.size()>1)
		{
			while ((vec[0]!=vec[1])&&(vec[0]!=0)&&(vec[1]!=0))
			{
				if (vec[0]>vec[1])
					vec[0]%=vec[1];
				else
					vec[1]%=vec[0];
				/*cout << vec[0] << " " << vec[1] <<endl;
				system("pause");*/
			}
			if (vec[1]==0)
			{
				BigInt temp=vec[1];
				vec[1]=vec[0];
				vec[0]=temp;
			}
			vec.pop_front();
		}
		BigInt T=vec[0];
		BigInt kyt=max/T;
		if (T*kyt<max)
			kyt+=1;
		fout << "Case #" << cases <<": " << kyt*T-max <<endl;
	}
	return 0;
}