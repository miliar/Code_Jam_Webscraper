// codeJam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int testcase;
	cin>>testcase;
	fstream f("c:\\output.txt");


	for(int i=0; i<testcase; ++i)
	{
		int r,k,n,sum=0, count=0, index=0;
		cin>>r>>k>>n;
		vector <int> input;
		vector <int> isOn;
		for(int j=0; j<n; ++j)
		{
			int temp;
			cin>>temp;
			input.push_back(temp);
			isOn.push_back(0);
		}
		for(int t=0; t<r; ++t)
		{
			count = 0 ;
			while(count<k)
			{
				if(isOn[index] == 0)
				{
					count += input[index];
					isOn[index] = 1;
					index++;		
				}
				if (count>k)
				{
					index -- ;
					count -= input[index];
					
					break;
				}	
				if(index == n)
					index = 0;
				
				bool flag= false;
				for(int y=0; y<n; y++)
				{
					if(isOn[y]==0)
					{	
						flag=true;
						break;
					}

				}
				if(!flag)
					break;


			}
		//	cout<<index<<ends<<count<<endl;
			sum+=count;
			count = 0;
			for (int k=0; k<n; ++k)
				isOn[k] = 0;
		}
		input.clear();
		isOn.clear();
		f<<"Case #"<<i+1<<": "<<sum<<endl;
		//cout<<"the sum is"<<sum<<endl;
	}
	return 0;
}

