// acm2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

vector<int> Sean;
vector< vector<int> > Patrik;

void GetMFromN(vector<int> v, vector<int> res, unsigned int M)
{

	//if(M > v.size())
	//{
	//	return;
	//}
	//while(next_permutation(v.begin(),v.end()))
	//{
	//	
	//}

	if(M == res.size())
	{
		Patrik.push_back(res);
		//for(unsigned int i=0; i < res.size(); i++)
		//	cout<<res[i];
		//cout<<endl;
		return;
	}
	
	int nMax = 0;
	if(!res.empty())
		nMax = *max_element(res.begin(),res.end());
	for(vector<int>::iterator i=v.begin(); i != v.end(); i++)
	{
		if(*i>nMax)
		{
			vector<int> temp = v;
			res.push_back(*i);
			temp.erase(find(temp.begin(),temp.end(),*i));
			GetMFromN(temp,res,M);
			res.pop_back();
		}
	}
}

void GetSean(vector<int> v, int j)
{
	Sean.clear();
	vector<int> temp = Patrik[j];
	for(vector<int>::iterator i=v.begin(); i != v.end(); i++)
	{
		vector<int>::iterator ite;
		if((ite=find(temp.begin(),temp.end(),*i)) == temp.end())
		{
			Sean.push_back(*i);
		}
		else
		{
			temp.erase(ite);
		}
	}
}

bool NotCry(vector<int> patrik, vector<int> sean)
{
	if(sean.size()==0 || patrik.size() == 0)
		return false;

	int p=patrik[0];
	int s=sean[0];
	for(unsigned int i=1; i < patrik.size(); i++)
	{
		p = p^patrik[i];
	}
	for(unsigned int i=1; i < sean.size(); i++)
	{
		s = s^sean[i];
	}

	if(p==s)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int GetAnswer(vector<int> candy)
{
	int res = -1;

	for(unsigned int i=0; i < candy.size(); i++)
	{
		vector<int> res;
		Patrik.clear();
		GetMFromN(candy,res,i+1);
		for(unsigned int j=0; j < Patrik.size();j++)
		{
			GetSean(candy,j);
			if(NotCry(Patrik[j],Sean))
			{
				int temp=0;
				for(unsigned int i=0; i < Sean.size(); i++)
				{
					temp += Sean[i];
				}
				return temp;
			}
		}
	}

	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T=0;


	ifstream in;
	in.open("C-small-attempt.in");

	ofstream out;
	out.open("out.out");

	in>>T;
	int* N = new int[T];
	vector< vector<int> > candy;
	for(int i=0; i < T; i++)
	{
		in>>N[i];
		vector<int> vTemp;
		for(int j=0; j < N[i]; j++)
		{
			int temp=0;
			in>>temp;
			vTemp.push_back(temp);
		}
		sort(vTemp.begin(),vTemp.end());
		candy.push_back(vTemp);
		
	}


	for(int i=0; i < T; i++)
	{
		int res = GetAnswer(candy[i]);
		if(res == -1)
		{
			out<<"Case #"<<i+1<<": "<<"NO"<<endl;
		}
		else
		{
			out<<"Case #"<<i+1<<": "<<res<<endl;
		}
	}

	delete [] N;
	in.close();
	out.close();

	getchar();
	getchar();
	//getchar();
	return 0;
}