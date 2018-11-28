#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	int t, n, s, p, *arr;
	fin.open("test.in",ios::in);
	fout.open("test.out",ios::out);

	fin>>t;
	for(int i=0;i<t;i++)
	{
		int sCnt = 0, nCnt = 0;
		fin>>n>>s>>p;
		arr = new int[n];
		for(int k=0;k<n;k++)
			fin>>arr[k];
		for(int k=0;k<n;k++)
		{
			if(arr[k] == 0 & p != 0)
				continue;
			int temp = (arr[k] - p)/2 ;
			if(temp < 0)
				continue;
			if(abs(temp-p) == 1 || temp >= p)
				nCnt++;
			else
			{
				temp = arr[k] - p;
				if(temp-(p-1) == (p-2) || temp/2 == p-2)
					sCnt++;
			}
		}
		int total = nCnt;
		if(sCnt >= s)
			total += s;
		else total += sCnt;

		fout<<"Case #"<<i+1<<": "<<total<<endl;
	}
	fout.close();

	return 0;
}