#include<iostream>
#include<fstream>

using namespace std;

bool calcNoSurprise(int score, int total)
{
	int counter,nums[3];
	if(score==0)
		return true;
	int div=total/score;
	int remainder=total%score;

	nums[0]=nums[1]=nums[2]=0;
	if(div>=3)
		return true;
	else if(div<3)
	{
		for(counter=0;counter<div;counter++)
			nums[counter]=score;
		nums[counter]=remainder;

		while(nums[1]-nums[2]>1)
		{
			nums[1]--; nums[2]++;
		}
		while(nums[0]-nums[1]>1)
		{
			nums[0]--;nums[1]++;
		}
		while(nums[0]-nums[2]>1)
		{
			nums[0]--;nums[2]++;
		}
		if(nums[0]>=score || nums[1]>=score ||nums[2]>=score)
			return true;
		else
			return false;
	}
}

bool calcSurprise(int score, int total, const int &surprise)
{
	int counter,div=(total/score),remainder=(total%score),nums[3];
	nums[0]=nums[1]=nums[2]=0;
	if(surprise<=0)
		return false;

	for(counter=0;counter<div;counter++)
		nums[counter]=score;
	nums[counter]=remainder;

	while(nums[1]-nums[2]>1)
	{
		nums[1]--; nums[2]++;
	}
	while(nums[0]-nums[1]>2)
	{
		nums[0]--;nums[1]++;
	}
	while(nums[0]-nums[2]>2)
	{
		nums[0]--; nums[2]++;
	}

	if(nums[0]>=score || nums[1]>=score ||nums[2]>=score)
		return true;
	else
		return false;
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("output.txt");
	
	int cases,counter,nGooglers[100],surprise[100],score[100],totalPoints[100][100],correctFlag=0;

	in>>cases;
	for(counter=0;counter<cases;counter++)
	{
		in>>nGooglers[counter];
		in>>surprise[counter];
		in>>score[counter];
		for(int counter2=0;counter2<nGooglers[counter];counter2++)
			in>>totalPoints[counter][counter2];
	}

	//I read in everything! YAAY :D

	for(counter=0;counter<cases;counter++)
	{
		for(int counter2=0;counter2<nGooglers[counter];counter2++)
		{
			if(calcNoSurprise(score[counter],totalPoints[counter][counter2]))
				correctFlag++;
			else if(calcSurprise(score[counter],totalPoints[counter][counter2],surprise[counter]))
			{
				correctFlag++;
				surprise[counter]--;
			}
		}
		out<<"Case #"<<counter+1<<": "<<correctFlag<<endl;
		correctFlag=0;
	}

	return 0;
}