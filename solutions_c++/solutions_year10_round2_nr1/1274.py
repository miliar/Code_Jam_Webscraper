#include "stdafx.h"
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string *de,*dc;

int calc(int n, int m)
{
	int count,lc,i,j,fl=0;
	count = 0;
	for(i=0;i<m;i++)
	{
		lc=0;
		string temp = dc[i];
		while(temp.size()!=0)
		{
			fl=0;
			for(j=0;j<n+i;j++)
			{
				string comp = de[j];
				int rt = comp.find(temp);
				int sz = temp.size();
				if(rt!=comp.npos && rt==0 && (comp.size()==temp.size() || comp[temp.size()]=='/'))
				{
					fl = 1;
					count+=lc;
					break;
				}
			}
			if(fl==1)
				break;
			int pos = temp.rfind('/');
			if(pos==temp.size())
				pos=0;
			temp = temp.substr(0,pos);
			lc++;
		}
		if(temp.size()==0)
			count+=lc;
		de[n+i] = dc[i];
	}
	return count;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T=0,N=0,K=0,i,j;
	string line;
	ifstream myfile ("example.txt");
	ofstream outfile("out.txt");
	if (myfile.is_open())
	{
		getline (myfile,line);
		T = atoi(line.c_str()); 
		for(i=0; i<T; i++)
		{
			getline (myfile,line);
			char *pch = (char *)line.c_str();
			N = atoi(strtok (pch," "));
			K = atoi(strtok (NULL," "));
			de = new string[N+K];
			dc = new string[K];

			for(j=0;j<N;j++)
				getline (myfile,de[j]);

			for(j=0;j<K;j++)
				getline (myfile,dc[j]);

			int ret = calc(N,K);
			outfile << "Case #" << i+1 << ": " << ret << endl;
		}
		myfile.close();
		outfile.close();
	}
	return 0;
}