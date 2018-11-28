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

int product(vector<int> x, vector<int> y)
{
	int result = 0;
	if(x.size()!=y.size())
	{
		cout<<"error! the dimension of x and y is different!"<<endl;
		return -10000;
	}
	int dim = x.size();
	for(int i = 0; i<dim; i++)
	{
		result+=x[i]*y[dim-i-1];
	}
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
	vector<int> x;
	vector<int> y;
	while(numCase>0)
	{
		numCase--;
		int inX;
		int inY;
		x.clear();
		y.clear();
		int result = 0;
		numVecDim =getNum(im);
		int tempVecDim = numVecDim;
		while(tempVecDim>1)
		{
			tempVecDim--;
			im>>inX;
			x.push_back(inX);
		}
		inX = getNum(im);
		x.push_back(inX);

		tempVecDim = numVecDim;
		while(tempVecDim>1)
		{
			tempVecDim--;
			im>>inY;
			y.push_back(inY);
		}
		inY = getNum(im);
		y.push_back(inY);
		sort(x.begin(), x.end());
		sort(y.begin(), y.end());
		result = product(x,y);

		om<<"Case #"<<realNum-numCase<<": "<<result<<endl;
	}
	return 0;
}

