#include "StdAfx.h"
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string.h>
#include <math.h> 
#include <stdio.h> 
using namespace std;

int main() 
{

	fstream out;
	ofstream in;
	int n=0,T,temp,result;
	in.open("D:\\xx.out",ios::trunc); 
	out.open("D:\\xx.in",ios::in);
	int N[100],S[100],P[100],F[100][100],NN,SS,PP,i=0;
	out>>T;
	for(int i=0;i<T;i++)
	{
		out>>N[i]>>S[i]>>P[i];
		for (int j=0;j<N[i];j++)
		{
			out>>F[i][j];
		}
	}

	for(int i=0;i<T;i++)
	{
		//std::cout<<AA[i]<<"  "<<BB[i]<<endl;
		result=0;
		NN=N[i];
		PP=P[i];
		SS=S[i];
		for (int j=0;j<NN;j++)
		{
			for (int k=j+1;k<NN;k++)
			{
				if (F[i][j]>F[i][k])
				{
					temp=F[i][j];
					F[i][j]=F[i][k];
					F[i][k]=temp;
				}
			}
		}

		for (int j=0;j<NN;j++)
		{
			if (PP==0)
			{
				result=NN;
				break;
			}
			if(F[i][j]==0)
				continue;
			if (F[i][j]>=3*PP-4&&F[i][j]<3*PP-2)
			{
				if (0!=SS)
				{
					SS--;
					result++;
				}
			}
			else if (F[i][j]>=3*P[i]-2)
			{
				result++;
			}
		}

		//std::cout<<N[i]<<"  "<<S[i]<<"  "<<P[i]<<"  ";
		//for (int j=0;j<N[i];j++)
		//{
		//	std::cout<<F[i][j]<<"  ";
		//}
		//std::cout<<"    result is:"<<result;
		//std::cout<<endl;
		in<<"Case #"<<i+1<<": ";
		in<<result<<endl;

		//		std::cout<<result<<endl;
	}
	in.close();
	//else std::cout<<"0";
	std::cin>>T;
}