#include <string>
#include <stack>
#include <iostream>
#include <fstream>

using namespace std;
class BigInt
{
public:
	string data;

	BigInt(string str):data(str){};
	BigInt():data("0"){};

	int len()
	{
		return data.length();
	}

	char at(int pos)
	{
		if(pos < 0 || pos >= data.length())
			return '0';

		return data[pos];
	}

	void set(int pos, char val)
	{
		if(pos < 0 || pos >= data.length())
			return;
		data[pos] = val;
	}

	void trim()
	{
		while(data[0] == '0' && data.length() > 1)
			data.erase(0, 1);
	}
};

int comp(BigInt x, BigInt y)
{
	if(x.len() > y.len())
		return 1;
	else if(x.len() < y.len())
		return -1;

	return x.data.compare(y.data);
}

BigInt sub(BigInt& x, BigInt& y)
{
	bool bow = false;
	stack<char> resStack;
	int lenX = x.len();
	int lenY = y.len();
	char curXValue, curYValue;

	for(int i=0; i<x.len(); i++)
	{
		curXValue = x.at(lenX-1-i);
		curYValue = y.at(lenY-1-i);

		if(bow)
		{
			if(curXValue == 0){
				bow = true;
				curXValue = 9;
			}
			else
			{
				curXValue --;
				bow = false;
			}
		}

		if(curXValue < curYValue)
		{
			bow = true;
			curXValue += 10;
		}

		x.set(lenX-1-i, curXValue - curYValue + '0');
	}

	x.trim();

	return x;
}


BigInt mod(BigInt& x, BigInt& y)
{
	if(comp(x, y) <0)
		return x;

	BigInt tmp("");
	for(int i=0; i<x.len(); i++)
	{
		tmp.data.push_back(x.data[i]);
		tmp.trim();
		while(comp(tmp, y) >= 0)
		{
			sub(tmp, y);
		}
	}
	return tmp;
}

void Qsort(BigInt* dataArr, int start, int end)
{
	if(start >= end)
		return;

	BigInt radix = dataArr[start];
	int s= start;
	int e= end;
	
	while(s < e)
	{
		while(s < e && comp(dataArr[e], radix) >= 0)
			e--;
		dataArr[s] = dataArr[e];

		while(s<e && comp(dataArr[s], radix) <= 0)
			s++;
		dataArr[e] = dataArr[s];
	}
	dataArr[s] = radix;
	Qsort(dataArr, start, s-1);
	Qsort(dataArr, s+1, end);
}

BigInt gcd(BigInt& x, BigInt& y)
{
	BigInt zero;
	if(comp(y, zero) == 0)
		return x;

	BigInt res = mod(x, y);
	return gcd(y, res);
}

BigInt gcd(BigInt* dataArr, int start, int end)
{
	if(start == end)
		return dataArr[start];
	int mid = (start + end)/2;

	BigInt left = gcd(dataArr, start, mid);
	BigInt right = gcd(dataArr, mid+1, end);

	if(comp(left, right) < 0)
		return gcd(right, left);
	else
		return gcd(left, right);
}

void main(int argc, char* argv[])
{
	if(argc != 3)
	{
		cout<<"usage error"<<endl;
		exit(0);
	}
	std::ifstream caseReader(argv[1]);
	std::ofstream resWriter(argv[2]);

	int nLine;
	caseReader>>nLine;

	int nNum;
	string data;
	for(int i=0; i<nLine; i++)
	{
		caseReader>>nNum;
		BigInt* dataArr = new BigInt[nNum];
		for(int j=0; j<nNum; j++)
		{
			caseReader>>data;
			dataArr[j] = BigInt(data);
		}
		Qsort(dataArr, 0, nNum-1);

		for(int j=nNum-1; j>0; j--)
			sub(dataArr[j], dataArr[j-1]);

		BigInt curGcd = gcd(dataArr, 1, nNum-1);

		BigInt curMod = mod(dataArr[0], curGcd);
		BigInt zero;
		if(comp(curMod, zero) == 0)
			resWriter<<"Case #"<<i+1<<": 0"<<endl;
		else
		{
			BigInt res = sub(curGcd, curMod);
			resWriter<<"Case #"<<i+1<<": "<<res.data<<endl;
		}

		delete [] dataArr;
	}
	caseReader.close();
	resWriter.close();
}