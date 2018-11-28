#include <iostream>
#include <cstdio>
#include <cassert>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

typedef unsigned int u32;

u32 normalSum(const vector<u32> &data)
{
	u32 sum = 0;
	for(int i = 0 ; i < data.size() ; i++)
	{
		sum += data[i];
	}
	return sum;
}

u32 carryLostSum(const vector<u32> &data)
{
	u32 sum = 0;
	for(int i = 0 ; i < data.size() ; i++)
	{
		sum ^= data[i];
	}
	return sum;
}

int getUsedBit(u32 value)
{
	int bit = 0;
	while(value > 0)
	{
		value /= 2;
		bit++;
	}
	return bit;
}

//bit개의 비트로 만들수 있는 최대숫자. 이것보다는 반대쪽합이 작아야한다
int calcMaxSum(int bit)
{
	return (int)powf(2, bit)-1;
}

int doLogic(const vector<u32> &data)
{	
	int maxSum = calcMaxSum(getUsedBit(data.back()));
	//split는 집합에 넣을것을 bit연산으로 계산하기위해서 쓰는거
	u32 split = powf(2, data.size())-1-1;
	while(split >= 1)
	{
		vector<u32> seanData;
		vector<u32> patrickData;
		for(int i = 0 ; i < data.size() ; i++)
		{
			u32 mask = 1 << i;
			if((split & mask) == mask)
			{
				seanData.push_back(data[i]);
			}
			else
			{
				patrickData.push_back(data[i]);
			}
		}
		if(seanData.size() == 0 || patrickData.size() == 0)
			continue;

		u32 seanSum = carryLostSum(seanData);
		u32 patrickSum = carryLostSum(patrickData);
		if(seanSum == patrickSum)
		{
			return normalSum(seanData);
		}

		/*
		for(int i = 0 ; i < seanData.size() ; i++)
			cout << seanData[i] << " ";
		cout << endl;
		*/
		split--;
	}
	return -1;
}

int main()
{
	/*
	
	data.push_back(3);
	data.push_back(5);
	data.push_back(6);
	*/
	/*
	vector<u32> data;
	data.push_back(1);
	data.push_back(2);
	data.push_back(3);
	data.push_back(4);
	data.push_back(5);
	*/
	/*
	u32 d[] = {
		177780, 803487, 693880, 613352, 470589, 830393, 450854, 907063, 297669,
		809137, 407731, 97069, 367485, 721087, 819398
	};
	vector<u32> data(d, d+sizeof(d)/sizeof(d[0]));
	*/
	/*
	sort(data.begin(), data.end());
	int s = doLogic(data);
	cout << s;
	getchar();
	*/
	
	
	int numTest;
	cin >> numTest;
	for(int i = 0 ; i < numTest ; i++)
	{
		int inputNum;
		cin >> inputNum;
		vector<u32> data;
		for(int j = 0 ; j < inputNum ; j++)
		{
			int num;
			cin >> num;
			data.push_back(num);
		}
		sort(data.begin(), data.end());

		int s = doLogic(data);
		if(s > 0)
			printf("Case #%d: %d\n", i+1, s);
		else
			printf("Case #%d: NO\n", i+1);
	}
	
	return 0;
}