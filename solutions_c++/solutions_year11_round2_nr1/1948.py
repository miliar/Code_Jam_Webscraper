// acm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

#ifdef Deg
#define in cin
#define out cout
#endif

vector<float> GetAnswer(vector<char> vec, int n)
{
	float* wp = new float[n];
	float* wp2 = new float[n];
	float* owp = new float[n];
	float* oowp = new float[n];

	//calc each wp
	for(int i=0; i < n; i++)
	{
		int nWin = 0;
		int nLose = 0;
		for(int j=0; j < n; j++)
		{
			if(vec[i*n+j] == '1')
			{
				nWin++;
			}
			else if(vec[i*n+j] == '0')
			{
				nLose++;
			}
		}
		wp[i] = ((float)nWin)/(nWin+nLose);
	}


	//calc owp
	for(int i=0; i < n; i++)
	{
		for(int k=0; k < n; k++)
		{
			int nWin = 0;
			int nLose = 0;
			for(int j=0; j < n; j++)
			{
				if(i!=j)
				{
					if(vec[k*n+j] == '1')
					{
						nWin++;
					}
					else if(vec[k*n+j] == '0')
					{
						nLose++;
					}
				}
			}
			wp2[k] = ((float)nWin)/(nWin+nLose);
		}


		int oppo=0;
		float total=0.0f;
		for(int j=0; j < n; j++)
		{
			if(vec[i*n+j] == '0' || vec[i*n+j] == '1')
			{
				oppo++;
				total += wp2[j];
			}
		}
		owp[i] = total / oppo;
	}

	//calc oowp
	for(int i=0; i < n; i++)
	{
		int oppo=0;
		float total=0.0f;
		for(int j=0; j < n; j++)
		{
			if(vec[i*n+j] == '0' || vec[i*n+j] == '1')
			{
				oppo++;
				total += owp[j];
			}
		}
		oowp[i] = total / oppo;
	}
	
	vector<float> ans;
	for(int i=0; i < n; i++)
	{
		ans.push_back(0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
	}

	delete [] wp;
	delete [] wp2;
	delete [] owp;
	delete [] oowp;
	return ans;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T=0;

	vector< vector<char> > q;

	ifstream in;
	in.open("A-large.in");

	ofstream out;
	out.open("out.out");

	in>>T;
	int* N = new int[T];
	for(int i=0; i < T; i++)
	{
		in>>N[i];
		vector<char> temp;
		for(int j=0; j < N[i]; j++)
		{
			for(int l=0; l < N[i]; l++)
			{
				char c;
				in>>c;
				temp.push_back(c);
			}
		}
		q.push_back(temp);
	}

	for(int i=0; i < T; i++)
	{
		out<<"Case #"<<i+1<<":"<<endl;
		
		vector<float> ans = GetAnswer(q[i],N[i]);
		for(int j=0; j < ans.size(); j++)
		{
			out.precision(8);
			out<<ans[j]<<endl;
		}
	}

	in.close();
	out.close();

	getchar();
	getchar();
	getchar();
	return 0;
}

