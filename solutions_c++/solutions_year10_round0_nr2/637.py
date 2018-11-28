#include "iostream"
#include "fstream"
#include <time.h>
#include <math.h>
#include <stdio.h>
#include "LargeNumber.h"
using namespace std;

CLargeNumber process(vector<CLargeNumber> arr, int N);
const CLargeNumber zero = CLargeNumber(0);
const CLargeNumber one = CLargeNumber(1);
void main()
{
	ifstream fin;
	ofstream fout;
	int T;	//number of testcases
	vector<CLargeNumber> arr;
	int N;
	CLargeNumber result=0;
	string str;
	CLargeNumber numberI;

	fin.open("B-large.in", ios_base::in);
	fout.open("B-large.out", ios_base::out);

	fin>>T;
	getline(fin, str);
	for(int i=1; i<=T; i++)
	{				
		fin>>N;
		fout<<"Case #"<<i<<": ";		
		getline(fin, str);		

		size_t index=1;
		size_t oldIndex=1;				

		while(index != str.npos)
		{
			string subStr;
			if(index>1)
				oldIndex = index+1;

			index = str.find(" ", oldIndex);
			subStr = str.substr(oldIndex, index-oldIndex);			
			numberI= CLargeNumber(subStr);
			arr.push_back(numberI);
		}
		cout<<i<<"....."<<endl;
		result = process(arr, N);
		arr.clear();
		fout<<result.ToString();

		if(i<T)
			fout<<endl;
	}

	fin.close();
	fout.close();
}

CLargeNumber maxDivisor (CLargeNumber a,CLargeNumber b)
{
	CLargeNumber t = 0;

	while(b > zero)
	{
		t = a%b;
		a = b;
		b = t;
	}
	return a;
}

int sortArray(vector<CLargeNumber> &arr, int N)
{
	CLargeNumber pre = arr[N-1];
	for(int i=0; i<N-1; i++)
	{
		for(int j=i+1; j<N; j++)
		{
			if(arr[i]<arr[j])
			{
				CLargeNumber tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
	if(pre == arr[0])
		return 1;
	return 0;

}
CLargeNumber maxDivisorArray(vector<CLargeNumber> arr, int N)
{
	int i;
	CLargeNumber divisor = arr[0];
	for (i = 1; i < N; i ++)
		divisor = maxDivisor( divisor, arr[i]);
	return divisor;
} 
int checkExist(vector<CLargeNumber> arr, int N, CLargeNumber ele)
{
	for(int i=0; i<N; i++)
	{
		if(ele == arr[i])
			return 1;
	}
	return 0;
}

void diffArray(vector<CLargeNumber> arr, int N, vector<CLargeNumber> &diffArr)
{
	for(int i=1; i<N; i++)
		diffArr.push_back(arr[0]-arr[i]);	
}

CLargeNumber process(vector<CLargeNumber> arr, int N)
{		
	CLargeNumber result=0;
	int flag = sortArray(arr,N);


	if(N==2)
	{
		CLargeNumber h = arr[0]-arr[1];		
		if(arr[0]%h == zero)
			return zero;
		result = h-(arr[0]%h);
		if(checkExist(arr,N,result))
			return zero;
		return result;
	}
	else 
	{
		vector<CLargeNumber> diffArr;
		diffArray(arr, N, diffArr);

		CLargeNumber mxDivisor = maxDivisorArray(diffArr, diffArr.size());
		if(arr[0]%mxDivisor == zero)
			return zero;
		if(mxDivisor == one)
			return zero;
		result = mxDivisor - (arr[0] % mxDivisor);

		if(checkExist(arr,N,result)&&flag)
			return zero;
		return result;
	}
	return CLargeNumber(0);
}