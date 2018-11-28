#include<iostream>
#include<fstream>
#include<vector>
#include<set>
#include<cmath>
using namespace std;
const int MAX_LENGTH = 20;
int T;
int lower;
int upper;
int getNum(int lower, int upper)
{
	int sum = 0;
	std::vector<int> lA;
	lA.clear();
	int templower;
	int tempco = lower;
	while(tempco > 0)
	{
		templower = tempco%10;
		lA.push_back(templower);
		tempco=tempco/10;
	}
	std::vector<int> tlA;
	for(int i = 0; i < tlA.size(); i++)
	{
		tlA[i] = lA[lA.size()-1-i];
	}

	std::vector<int> lB;
	lB.clear();
	int tempupper;
	tempco = upper;
	while(tempco > 0)
	{
		tempupper = tempco%10;
		lB.push_back(tempupper);
		tempco=tempco/10;
	}
	std::vector<int> tlB;
	for(int i = 0; i < tlB.size(); i++)
	{
		tlB[i] = lA[lB.size()-1-i];
	}

	for(int num = lower; num <= upper; num++)
	{
		std::set<int> mySet;
		mySet.clear();
		mySet.insert(num);
		for(int iter = 1; iter < lA.size(); iter++)
		{
			int temp = pow(10.0,iter);
			if(num%temp < temp/10)
				continue;
			int newnum = num/temp + (num%temp)*pow(10.0,(lA.size()-iter+0.00));
			if (newnum < num || newnum > upper)
				continue;
			mySet.insert(newnum);
		}
		sum = sum + mySet.size() - 1;
	}
	return sum;
}

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C.out");
	fin>>T;
	for(int i = 0; i < T; i++)
	{
		fin>>lower;
		fin>>upper;
		fout<<"Case #"<<i+1<<": ";
		fout<<getNum(lower,upper);
		fout<<"\n";
	}
	fin.close();
	fout.close();
}