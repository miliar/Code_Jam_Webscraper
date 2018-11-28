// googleCode.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<fstream>
#include<iostream>
using namespace std;

void Go(int caseNum,int times, int cap, int groups, int* head);
int _tmain(int argc, _TCHAR* argv[])
{
	fstream in("input.txt",ios_base::in);
	int num(0),capicity(0),times(0),groups(0);
	int size(0);
	int* head(NULL);
	int caseNum(1);
		
	in >> num;
	while(in >> times >> capicity >> groups)
	{
		head = new int[groups];
		for(int i = 0; i < groups; i++)
		{
			in >> size;
			head[i] = size;
		}
		Go(caseNum,times,capicity,groups,head);
		caseNum++;
		delete[]head;
	}
	return 0;
}

void Go(int caseNum,int times, int cap, int groups, int* head){
		int i = 0;
		int c(0);
		int dollar(0);
		while(times--){
			c = cap;
			int pre = i;
			while(c >= head[i]){
				c -= head[i];
			   dollar += head[i];
			   i++;
			   if(i == groups)
			       i = 0;
			   if(i == pre)
				   break;
			}
		}
		fstream out("out.txt",ios_base::app);
		out << "Case #" << caseNum <<": "<< dollar << '\n';
	}
