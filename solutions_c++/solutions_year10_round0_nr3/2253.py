/*
 * ThemePark.cpp
 *
 *  Created on: May 8, 2010
 *      Author: wen
 */

#include <iostream>
#include <fstream>
//#include <queue>

using namespace std;

int main()
{
	ifstream input("D:\\eclipseWorkspace\\ThemePark\\C-small-attempt0.in");
	ofstream output("D:\\eclipseWorkspace\\ThemePark\\C-small-attempt0.out");

	int T;//No. of test cases

	input>>T;

	int R;//No. of times roller runs
	int k;//No. of people roller holds
	int N;//No. of groups


	for (int i=1;i<=T;i++)
	{
		int sum=0;//total money
		input>>R>>k>>N;
		//build the initial queue(array)
		int queue[N];
		for(int j=0;j<N;j++)
		{
			int g;
			input>>g;
			queue[j]=g;
		}
		int front;//current front	front%N
		int end=0;//current end  	end%N
		for (int l=0;l<R;l++)
		{
			front=end;
			int curSum=0;
			do
			{
				curSum=curSum+queue[end];
				end++;
				if(end>=N)
					end=end-N;
			} while((curSum+queue[end]<=k)&&(front!=end));
			sum=sum+curSum;
		}
		output<<"Case #"<<i<<": "<<sum<<endl;
	}

	input.close();
	output.close();

}
