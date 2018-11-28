// googlecj2012c.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin( "c:\\B-large.in" );
	ofstream fout( "c:\\output.txt" , ios_base::in || ios_base::trunc);
	string temp1, temp2;
	istringstream stream1;
	string temp;
	fin>>temp;
	int times=0;
	stream1.str(temp);
	stream1>>times;

	string stc;
	getline(fin, stc);
	stream1.clear();
	stream1.str(stc);
	int N=0;
	int S=0;
	int p=0;
	int ti[100]={0};
	int ns[303]={0};
	int result=0;
	/*while(!stream1.eof())
	{
		stream1>>ns[i++];
	}*/
	for(int n=0; n<times; ++n)
	{		
		getline(fin, stc);
		stream1.clear();
		stream1.str(stc);
		int i=0;
		stream1>>N;
		stream1>>S;
		stream1>>p;
		while(!stream1.eof())
		{
			stream1>>ti[i++];
		}
		for(i=0; i<N; i++)
		{
			if(ti[i]<p)
				continue;
			double check=(double)p-((double)(ti[i]-p)/2.0);
			if(check>1.0)
			{
				if(check<=2.0)
				{
					if(S)
					{
						--S;
						++result;
					}
				}
			}
			else
				++result;
		}
		if(n<times)
			fout<<"Case #"<<n+1<<": "<<result<<endl;

		memset(ti, 0, sizeof(int)*100);
		N=0;
		S=0;
		p=0;
		result=0;
	}
	system("pause");
	return 0;
}


