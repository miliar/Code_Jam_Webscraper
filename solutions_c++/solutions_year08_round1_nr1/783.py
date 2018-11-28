// Round1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
// Train Timetable.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#include <math.h>


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

int pivot(int start, int end, vector<int>& mypair)
{
	int i = start-1;
	int j = start;
	while(  j < end)
	{
		if(mypair[j] < mypair[end])
		{
			i++;
			int temp = mypair[i];
			mypair[i] = mypair[j];
			mypair[j] = temp;
 			
		}
		j++;
	}

	i++;

	int temp = mypair[i];
	mypair[i] = mypair[end];
	mypair[end] = temp;
	return i;
}

void quickSort(int start, int end, vector<int>& mypair)
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
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");

	char out_head[100] = "Case #";
	char out_data[100];
	out_data[0] = '\0';
	in>>N;
	removeSpace(in);

	for (size_t  caseIndex = 0; caseIndex < N; caseIndex++)  //start the test
	{
		size_t sizeOfVector = 0;
		in>>sizeOfVector;
		removeSpace(in);
		vector<int> vectorA;
		vector<int> vectorB;
		for(size_t j = 0; j < sizeOfVector; j++)
		{
			int temp;
			in>>temp;
			vectorA.push_back(temp);
		}
		for(size_t j = 0; j < sizeOfVector; j++)
		{
			int temp;
			in>>temp;
			vectorB.push_back(temp);
		}

		quickSort( 0, sizeOfVector -1, vectorA);
		quickSort( 0,sizeOfVector -1, vectorB);

		int smallest = 0;
		for(int i =0; i < vectorA.size(); i++)
		{
			smallest += vectorA.at(i) * vectorB.at(sizeOfVector - i -1);
		}
		// now we have get all the numbers

	
		getHead(out_head, caseIndex+1);
		 
		itoa(smallest, out_data, 10);
		out.write(out_head, strlen(out_head));
		out.write(out_data, strlen(out_data));
		if(caseIndex != N-1)
			out.write("\n",1);
	}





	out.close();
	return 0;
}






