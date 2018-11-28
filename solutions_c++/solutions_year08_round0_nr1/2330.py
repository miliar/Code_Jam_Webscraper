/*
 * search.cpp
 *
 *  Created on: Jul 16, 2008
 *      Author: killaMetz
 */

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;

void getStrings(int num, ifstream &i, string arr[])
{
	string * temp;
	for(int j=0;j<num;j++)
	{
		temp = new string();
		getline(i,*temp);
		arr[j] = *temp;
	}
}

int findNextSwitch(string engine, string quer[], int start, int size)
{
	for(int i=start;i<size;i++)
	{
		if(engine.compare(quer[i])==0)
		{
			return i;
		}
	}
	return -1;//can finish out the queries
}
/*
int getSwitches(string eng[],int s1, string quer[], int s2,int goal)
{
	int lowest_total=0;//lowest total number of switches so far
	//go through the queries
	for(int j=0;j<s2;j++)
	{

	}
	if(lowest_total <= goal)
		return lowest_total;
	else
		return getSwitches(eng,s1,quer,s2,goal+1);
}*/
int getSwitches(string eng[],int s1, string quer[], int s2)
{
    int lowest_total = 0;//lowest total number of switches so far
	int highest_index = 0;//furthest we can get
	//go through the queries
	for (int j = 0; j < s2;) {
		for (int k = 0; k < s1; k++)//go through each engine
		{
			int nextSW = findNextSwitch(eng[k], quer, j, s2);
			if (nextSW < 0) {
				j = s2;
				highest_index = -1;
				break;
			} else {
				if (nextSW > highest_index) {
					highest_index = nextSW;
				}
			}
		}
		if (highest_index < 0) {
			break;
		} else//update the number of switches
		{
			j = highest_index;
			lowest_total++; //switch engines
		}
	}
	cout<<"lowest total: "<<lowest_total<<endl;
	return lowest_total;
                //else
                //            return getSwitches(eng,s1,quer,s2,goal+1);
}

void runtest(ifstream &i, ofstream &o)
{
	//get the number of lines below
	string lineNum;
	getline(i,lineNum);
	int numlines = atoi(lineNum.c_str());
	string engArr[numlines];
	getStrings(numlines,i,*&engArr);
	//get the number of queries
	string lineNum2;
	getline(i,lineNum2);
	int numqueries = atoi(lineNum2.c_str()) ;
	string qArr[numqueries];
	getStrings(numqueries,i,*&qArr);
	o<<getSwitches(engArr,numlines,qArr,numqueries)<<endl;

}

int main(int argc, char * argv[])
{
	//open the file
	string currline;
	ifstream infile;
	ofstream ofile;
	ofile.open("output.out",ios::out);
	infile.open(argv[1]);
	if(infile.is_open())
	{
		while(!infile.eof())
		{
			getline(infile,currline);
			//convert next line to a number
			int testCases = atoi(currline.c_str());
			for(int i=1;i<=testCases;i++)
			{
				ofile<<"Case #"<<i<<": ";
				runtest(infile,ofile);
			}
		}
	}

	//close the file
	infile.close();
	ofile.close();
}
