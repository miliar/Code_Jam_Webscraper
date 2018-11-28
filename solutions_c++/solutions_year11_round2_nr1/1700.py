// RPI.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	int T,N;
	char games[101][101];
	double WP[101], OWP[101], OOWP[101];

	string temp;



	ifstream fin;
	fin.open("LRPI.in");

	ofstream fout;
	fout.open("RPI.txt");


	fin >> T;

	for(int k=0;k<T;k++)
	{
		fin >> N;

		

		for(int i=0;i<N;i++)
		{
			fin >> temp;
			for(int j=0;j<N;j++)
			{
				games[i][j]=temp.at(j);
				
				
			}
		}

		//WP
		for(int i=0;i<N;i++)
		{
			double num=0, wnum=0;
			for(int j=0;j<N;j++)
			{
				if(games[i][j]=='1')
				{
					num++;
					wnum++;
				}
				else if(games[i][j]=='0') num++;
			}
			WP[i]=wnum/num;
			
		}

		//OWP

		for(int i=0;i<N;i++)
		{
			double numOfOp=0; 
			double sumOfWP=0;
			for(int j=0;j<N;j++)
			{
				if((games[i][j]=='1')||(games[i][j]=='0'))
				{
					double num=0, wnum=0; 
					double WP=0;
					for(int l=0;l<N;l++)
					{
						if(i!=l)
						{
							if(games[j][l]=='1')
							{
								num++;
								wnum++;
							}
							else if(games[j][l]=='0') num++;
						}
					}
					
					WP=wnum/num;
					sumOfWP+=WP;
					numOfOp++;
				}
			}
			OWP[i]=sumOfWP/numOfOp;
			
		}

		//OOWP

		for(int i=0;i<N;i++)
		{
			double num=0;
			double sumOWP=0;
			
			for(int j=0;j<N;j++)
			{
				if((games[i][j]=='1')||(games[i][j]=='0'))
				{
					num++;
					sumOWP+=OWP[j];
				}
				
			}
			OOWP[i]=sumOWP/num;
			
		}

		//SCORE
		fout << "Case #"<<k+1<<":"<<endl;
		for(int i=0;i<N;i++)
		{
			fout << 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i] <<endl;
			//cout << WP[i]<<" "<<OWP[i]<<" "<< OOWP[i]<<endl;
		}


	}

	//cin >> N;

	fin.close();
	fout.close();
	return 0;
}

