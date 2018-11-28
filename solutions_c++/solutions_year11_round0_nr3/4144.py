#include <iostream>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <stdint.h>
#include <fstream>


using namespace std;


int64_t myadd(int64_t x, int64_t y)
{
	return x^y;
}

int64_t test(vector<int64_t>& vec)
{
	int64_t sum = 0;
	int64_t sum2 = 0;
	int64_t min = 1000000000;
	for(int64_t i = 0; i < vec.size(); i++)
	{
		sum = myadd(sum , vec[i]);
		sum2 += vec[i];
		if(vec[i] < min){
			min = vec[i];
		}
	}
	if(sum != 0){
		return -1;
	}
	return sum2 - min;
}

int main(int argc, char **argv)
{
	if(argc < 2){
		cout<<"error parameter"<<endl;
	}
	ifstream in(argv[1]);
	int64_t linenum = 0;
	in >> linenum;
	int index = 1;
	while(linenum -- > 0){
		int64_t num = 0;
		in >> num;
		vector<int64_t> vec;
		int64_t t;
		while(num -- > 0){
			in >> t;
			vec.push_back(t);		
		}
		int64_t max = test(vec);
		if(max > 0)
		{
			cout<<"Case #"<<(index++)<<": "<<max<<endl;
		}
		else
		{
			cout<<"Case #"<<(index++)<<": NO"<<endl;
		}
	}
	return 0;
}
