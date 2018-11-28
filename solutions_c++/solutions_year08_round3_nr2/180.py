// CodeJam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
#include <math.h>
using namespace std;

int count = 0;
void GetValue(int num[], int elem_num, long long result)
{
	int bit_num=1;

	if(elem_num == 0)
	{
		if (result%2 == 0 || result%3 == 0 || result%5 == 0 || result%7 == 0 )
		count++;
		return;
	}

	while(bit_num <= elem_num)
	{
		long long temp=0;
		for (int i=elem_num-bit_num; i<elem_num; i++)
		{
			temp += num[i]*pow(10.0, elem_num-i-1);
		}
		if(bit_num!=elem_num)
		{
			GetValue(num, elem_num-bit_num, result+temp);
			GetValue(num, elem_num-bit_num, result-temp);
		}
		else
			GetValue(num, elem_num-bit_num, result+temp);
		bit_num++;
	}
}

int ints[40];
int Evaluate(string input)
{
	int len = input.length();
	for (int i=0; i<len; i++)
	{
		ints[i] = input[i]-'0';
	}
	GetValue(ints, len, 0);
	int temp = count;
	count = 0;
	return temp;
}
int main(int argc, char* argv[])
{
	ifstream in("input.in");
	ofstream out("output.out");
	int CaseNum;
	string line;
	int i=0;
	
	getline(in, line);
	CaseNum = atoi(line.c_str());
	while (getline(in, line))
	{
		i++;
		int num = Evaluate(line);
		out<<"Case #"<<i<<": "<<num<<endl;
	}
	in.close();
	out.close();
	return 0;
}

