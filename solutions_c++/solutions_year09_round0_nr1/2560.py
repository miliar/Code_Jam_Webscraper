#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <numeric>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int j;
	int L,D,N;
	string str_D[5005];
	string str_L[18];
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("A-large.out");
	if(!input)
	{
		cout<<"input error"<<endl;
		return 0;
	}
	if(!output)
	{
		cout<<"output error"<<endl;
		return 0;
	}
	input>>L>>D>>N;
	int round=1;
	//vector<string> vec;
	for(int i=0;i<D;i++)
		input>>str_D[i];
	//for(int i=0;i<D;i++)
	//	cout<<str_D[i]<<endl;
	while(round<=N)
	{
		string str;
		input>>str;
		int min=0,max;
		for(int i=0;i<L;i++)
		{
			if(str[min]=='(')
			{
				min++;
				max=min;
				while(str[max]!=')')
					max++;
				max--;
				
				str_L[i]=str.substr(min,max-min+1);
				min=max+2;
			}
			else
			{
				max=min;
				
				str_L[i]=str.substr(min,max-min+1);
				min=max+1;
			}
			
			
		}
		long long res=0;
		for(int i=0;i<D;i++)
		{
			for(j=0;j<L;j++)
			{
				if(str_L[j].find(str_D[i][j],0) < str_L[j].size())
					continue;
				else
					break;
			}
			if(j==L)
				res++;			
		}
		output<<"Case #"<<round<<": "<<res<<endl;
		round++;
	}
	input.close();
	output.close();
	return 0;
}