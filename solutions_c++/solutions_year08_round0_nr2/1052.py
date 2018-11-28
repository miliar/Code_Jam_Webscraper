// Train Timetable.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#include <math.h>

typedef struct
{
	int time;
	int a;
}MyPair;

void swapPair(MyPair& p1, MyPair& p2)
{
	int  temp = p1.time;
	p1.time = p2.time;
	p2.time = temp;
	temp = p1.a;
	p1.a = p2.a;
	p2.a = temp;
}

inline void removeSpace(ifstream& in)
{
	char temp[2];
	in.getline(temp, 2);
}



void  getHead(char* head, int index)
{
	size_t start = 0;

	char temp[10];
	_itoa_s(index, temp, 10);

	start = 6;
	head[start] = '\0';
	strcat(&(head[start]), temp);
	start += strlen(temp);
	strcat(&(head[start]), ": ");
}

void process(const string& time, int &start, int &end)
{
	int sum = 0;
	int index = 0;
	int temp = 0;
	for(int i = 0; i < 2; i++)
	{
		temp*= 10;
		temp += time.at(index++)-'0';
	}
	sum = 60* temp;
	index ++;
	temp = 0;
	for(int i = 0; i < 2; i++)
	{
		temp *= 10;
		temp += time.at(index++)-'0';
	}
	start = sum + temp;

	while(time.at(index) == ' ')
		index++;

	sum = 0;
	temp = 0;
	for(int i = 0; i < 2; i++)
	{
		temp*= 10;
		temp += time.at(index++)-'0';
	}
	sum = 60* temp;
	index ++;
	temp = 0;
	for(int i = 0; i < 2; i++)
	{
		temp *= 10;
		temp += time.at(index++)-'0';
	}
	end = sum + temp;
}


int pivot(int start, int end, vector<MyPair>& mypair)
{
	int i = start-1;
	int j = start;
	while(  j < end)
	{
		if(mypair[j].time < mypair[end].time || mypair[j].time == mypair[end].time && mypair[j].a % 2 == 0)
		{
			i++;
			swapPair(mypair[i],mypair[j]);
		}
		j++;
	}

	i++;
	swapPair(mypair[i], mypair[end]);
	return i;
}

void quickSort(int start, int end, vector<MyPair>& mypair)
{
	if( start < end)
	{
		int mid = pivot(start, end, mypair);
		quickSort(start, mid-1, mypair);
		quickSort(mid+1, end, mypair);
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	size_t N = 0;
	ifstream in("B-large.in");
	ofstream out("B-large.out");

	char out_head[100] = "Case #";
	char out_data[100];
	out_data[0] = '\0';
	in>>N;
	removeSpace(in);

	for (size_t  caseIndex = 0; caseIndex < N; caseIndex++)  //start the test
	{
		size_t aroudTime = 0;
		size_t NA, NB;
		in>>aroudTime;
		removeSpace(in);
		in>>NA;
		in>>NB;
		removeSpace(in);

		vector<MyPair> NAPair;
		for(size_t ii = 0; ii < NA; ii++)
		{
			string temp;
			getline(in, temp);
			MyPair aPair1;
			MyPair aPair2;
			process(temp, aPair1.time, aPair2.time);
			aPair1.a = 1;
			aPair2.a = 2;
			aPair2.time += aroudTime;
			NAPair.push_back(aPair1);
			NAPair.push_back(aPair2);
		}

		for(size_t ii = 0; ii < NB; ii++)
		{
			string temp;
			getline(in, temp);
			MyPair aPair1;
			MyPair aPair2;
			process(temp, aPair1.time, aPair2.time);
			aPair1.a = 3;
			aPair2.a = 4;
			aPair2.time += aroudTime;
			NAPair.push_back(aPair1);
			NAPair.push_back(aPair2);
		}


		// sort my pair
		quickSort(0,NAPair.size()-1, NAPair);

		int aStorage = 0, aHasToUse = 0, bStorage = 0, bHasToUse = 0;

		for(int i = 0, n = NAPair.size(); i < n; i++)
		{
			switch(NAPair[i].a)
			{
			case 1:
				{
					if(aStorage > 0)
						aStorage--;
					else
						aHasToUse ++;
					break;
				}
			case 2:
				{
					bStorage++;
					break;
				}
			case 3:
				{
					if(bStorage >0)
						bStorage--;
					else
						bHasToUse ++;
					break;
				}
			case 4:
				{
					aStorage++;
					break;
				}
				
			}
		}
		getHead(out_head, caseIndex+1);
		itoa(aHasToUse, out_data, 10);
		out.write(out_head, strlen(out_head));
		out.write(out_data, strlen(out_data));
		out.write(" ", 1);
		itoa(bHasToUse, out_data, 10);
		out.write(out_data, strlen(out_data));
		if(caseIndex != N-1)
			out.write("\n",1);

	}



	out.close();
	return 0;
}




