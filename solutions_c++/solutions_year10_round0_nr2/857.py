// codejam3.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include<algorithm>
#include<fstream>
using namespace std;

int gcd(int a, int b)
{
    while(b != 0)
    {
        int r = b;
        b = a % b;
        a = r;
    }
    return a;
}
void swap(int &a, int &b)
{
	int temp = a;
	a = b;
	b = temp;
}
int _tmain(int argc, _TCHAR* argv[])
{
	int testcase;
	fstream f("c:\\output8.txt");
	cin>>testcase;
	for(int i=0; i<testcase; ++i)
	{
		int size;
		cin>>size;
		vector<long> input;
		long mize[2]={0, 0};
		for(int j=0;j<size; ++j)
		{
			long temp;
			cin>>temp;
			input.push_back(temp);
		}
		sort(input.begin(),input.end());
		for(int k=1; k < input.size(); ++k)
		{
			mize[k-1] = input[k] - input[k-1];
		}
		int thegcd=0;
		if(size == 3)
		{
			if(mize[0] < mize[1])
				swap(mize[0], mize[1]);
			thegcd = gcd(mize[0], mize[1]);
		}
		else
		{
			thegcd = mize[0];
		}
		int result = -input[0];
	//	result = result/thegcd*thegcd;
		while(result < 0)
		{
			result += thegcd;
		}
//		cout<<result<<endl;
		f<<"Case #"<<i+1<<": "<<result<<endl;		
	
	}
	return 0;
}

