// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <math.h>
#include   <iomanip>
using namespace std;

int T,A,B;
double arr[100000];
int getTryTime();
int getBackTime(int breakspaceCount);
int getRetryTime();
bool curChanceArr[100000];
void tentotwoArr(int value);
double getChance();

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,k,l;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>A>>B;
		for(j=0;j<A;j++)
		{
			cin>>arr[j];
		}
		double sum =0.0;
		double tv =0.0;
		double tr =0.0;
		double tb[100000];
		memset(tb,0.0,sizeof(double)*A);
	
		int count =(int) pow((double)2,(double)(A));
		for(j=0;j<count;j++)
		{
			memset(curChanceArr,0,sizeof(bool)*A);
			tentotwoArr(j);
			double chance = getChance();
			tv+=chance*getTryTime();
			tr+=chance*getRetryTime();
			for(k=1;k<=A;k++)
			{
				tb[k-1]+=chance*getBackTime(k);
			}

		}
		double min = tb[0];
		for(j=1;j<=A-1;j++)
		{
			if(min>tb[j])
				min=tb[j];

		}
		double ret=0.0;
		if(min>=tv&&tr>=tv)
			ret = tv;
		if(tv>=min&&tr>=min)
			ret = min;
		if(tv>=tr&&min>=tr)
			ret = tr;
		cout<<"Case #"<<i+1<<": ";
		cout <<setiosflags(ios::fixed); 
      cout <<setprecision(6)<<ret<<endl;
		//printf(".6lf\n",ret);
		
		//sum /= count;
	}

	return 0;
}

int getTryTime()
{
	int time = 0;
	//
	time = B-A+1;
	int i = 0;
	bool f=false;
	for(;i<A;i++)
	{
		if(curChanceArr[i])
		{
			f=true;
			break;
		}
	}
	if(f)//has error
	{
		time+=B+1;
	}
	return time;
}

int getRetryTime()
{
	int time = 1+B+1;//give up+try+enter
	return time;
}
int getBackTime(int breakspaceCount)
{
	int time = 2*breakspaceCount+B-A+1;
	int i = 0;
	bool f = false;
	for(;i<A-breakspaceCount;i++)
	{
		if(curChanceArr[i])
		{
			f=true;
			break;
		}
	}
	if(f)
	{
		time+=B+1;
	}
	return time;
}

void tentotwoArr(int value)
{
	int yu =0;
	int i;
	for(i=0;i<=A;i++)
	{
		if(value==0)
			return;
		yu = value%2;
		if(yu)
			curChanceArr[i]=true;
		else
			curChanceArr[i]=false;
		value /= 2;

	}
}

double getChance()
{
	double c = 1;
	int i;
	for(i=0;i<A;i++)
	{
		if(curChanceArr[i])
			c*=(1-arr[i]);
		else
			c*=arr[i];
	}
	return c;
}