// SaveUniverse.cpp : 定义控制台应用程序的入口点。
//
#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <hash_set>
#include <algorithm>
#include "BigInteger.h"
using namespace std;
using namespace stdext;
int getNum(ifstream& im)
{
	string strNum;
	if(!im.eof())
	{
		getline(im, strNum);
		return atoi(strNum.c_str());
	}
	else
		return 0;
}

BigInteger product(vector<int> x, vector<int> y)
{
	
	
	char * a = new char[1000];
	BigInteger result = 0;
	if(x.size()!=y.size())
	{
		cout<<"error! the dimension of x and y is different!"<<endl;
		return -10000;
	}
	int dim = x.size();
	for(int i = 0; i<dim; i++)
	{

		BigInteger temp = BigInteger(x[i])*BigInteger(y[dim-i-1]);
		result = result + temp;
	}
	delete a;
	return result;
}
int main(int argc, char* argv[])
{
	if(argc!=3)
	{
		printf("Please Input: [Input File Name] [Output File Name]\n");
		return 0;
	}
	int numCase = 0;

	ifstream im(argv[1]);
	ofstream om(argv[2]);

	numCase = getNum(im);
	int realNum = numCase;
	int numVecDim;
	vector<int> vecAlpha;//frequency
	
	while(numCase>0)
	{
		numCase--;
		int P;
		int K;
		int L;
		vecAlpha.clear();
	
		BigInteger result = 0;
		
		im>>P;
		im>>K;
		L = getNum(im);
		int tempL = L;
		int f;
		if(L>P*K)
		{
			om<<"Case #"<<realNum-numCase<<": "<<"Impossible"<<endl;
			continue;
		}
		while(tempL>1)
		{
			tempL--;
			im>>f;
			vecAlpha.push_back(f);
		}
		f = getNum(im);
		vecAlpha.push_back(f);
		sort(vecAlpha.begin(), vecAlpha.end());

		tempL = L;
		

		for(int i = 1; i<P+1; i++)
		{
			for(int j = 0; j<K; j++)
			{
				tempL--;
				if(tempL>=0)
				{
					result+=BigInteger(vecAlpha[tempL])*BigInteger(i);
				}

			}
		}
		
		

		om<<"Case #"<<realNum-numCase<<": "<<result<<endl;
	}
	return 0;
}

