#include <string>
#include <fstream>
#include <iostream>
#include <map>
using namespace std;

map<char,int> digitalMap;
int temp[63];

int change(string &input)
{
	int k = 0;
	bool first = true;
	int biggest = 0;
	for( int i=0;i<input.length();i++ )
	{
		if(digitalMap.count(input[i]) <= 0)
		{
			if(i == 0)
				k = 1;
			else if( first&&k==2)
			{
				k = 0;
			}
			digitalMap.insert(make_pair(input[i],k));
			temp[i] = k;
			if(first&&k==0)
			{
				k = 1;
				first = false;
			}
			if(k > biggest)
				biggest = k;
			k++;
		}else
		{
			temp[i] = digitalMap[input[i]];
		}
	}
	return biggest+1;
}

long long baseToTen(const int input[],int &base,bool &ifOK,int length)
{
	int now = 0;
	long long res = 0;
	int k = 0;
	bool first = true;
	for( int i=0;i<length;i++ )
	{
		now = input[i];
		res = res*base + now;
	}
	return res;
}

long long check(string &input)
{
	long long res;
	int smallest = change(input);
	if(smallest < 2)
		smallest = 2;
	bool ifOK;
	for(int i = smallest;i<=36;i++)
	{
		ifOK = true;

		res = baseToTen(temp,i,ifOK,input.length());
		if(ifOK)
			return res;
	}
	return -1;
}

void main()
{
	ifstream inf("E:\\A-large.in");
	ofstream ouf("E:\\A-large.out");


	string input;
	if(inf)
	{
		getline(inf,input);
		int N = atoi(input.c_str());
		int i = 1;
		while(i <= N && getline(inf,input))
		{
			memset(temp,0,sizeof(temp));
			digitalMap.clear();
			ouf<<"Case #"<<i<<": "<<check(input)<<endl;
			//cout<<"Case #"<<i<<": "<<input<<" "<<check(input)<<endl;
			i ++;
		}
	}
}