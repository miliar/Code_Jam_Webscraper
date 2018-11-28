// googldcodejam20110507.cpp : 定義主控台應用程式的進入點。
//A Bot Trust 

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin( "j:\\A-large.in" );
	ofstream fout( "j:\\output" , ios_base::in || ios_base::trunc);
	string t;
	getline(fin, t);
	istringstream ss1(t,istringstream::in);
	int times=0;
	ss1>>times;
	for(int i=0; i<times; ++i)
	{
		string line;
		getline(fin,line);
		istringstream stream1(line,istringstream::in);
		int N=0;
		stream1>>N;
		string tag;
		int *tags=new int[N];
		vector<int> orangeButton;
		vector<int> blueButton;
		int orange=0;
		int blue=0;
		for(int j=0; j<N; ++j)
		{
			stream1>>tag;
			if(tag=="O")
			{
				tags[j]=0;
				stream1>>orange;
				orangeButton.push_back(orange);
			}
			else if(tag=="B")
			{
				tags[j]=1;
				stream1>>blue;
				blueButton.push_back(blue);
			}
		}
		int orangePos=1;
		int bluePos=1;

		int orangeNext=0;
		int blueNext=0;

		int current=0;

		int orangeIdx=0;
		int blueIdx=0;

		int time=0;
		while(current<N)
		{
			if(orangeIdx!=(int)orangeButton.size())
				orangeNext=orangeButton.at(orangeIdx);
			else
				orangeNext=0;

			if(blueIdx!=(int)blueButton.size())
				blueNext=blueButton.at(blueIdx);
			else
				blueNext=0;

			if(tags[current]==0)
			{
				if((orangeNext-orangePos)<0)
					--orangePos;//move
				else if((orangeNext-orangePos)>0)
					++orangePos;//move
				else
				{
					//press button
					++current;
					++orangeIdx;
				}
				
				if((blueNext-bluePos)<0)
					--bluePos;//move
				else if((blueNext-bluePos)>0)
					++bluePos;//move
				else
					;//stay
			}
			else if(tags[current]==1)
			{
				if((blueNext-bluePos)<0)
					--bluePos;//move
				else if((blueNext-bluePos)>0)
					++bluePos;//move
				else
				{
					//press button
					++current;
					++blueIdx;
				}

				if((orangeNext-orangePos)<0)
					--orangePos;//move
				else if((orangeNext-orangePos)>0)
					++orangePos;//move
				else
					;//stay
			}
			++time;			
		}
		fout<<"Case #"<<i+1<<": "<<time<<endl;
		orangeButton.clear();
		blueButton.clear();
	}
	fout.close();
	system("pause");
	return 0;
}