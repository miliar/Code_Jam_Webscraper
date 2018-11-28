// qualification_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int sub_min(int &a,int &b)
{
	int c=a-b;
	if(c<0) c=-c;
	if(c>a) c=a;;
	if(c>b) c=b;
	return c;
	
}
int gcd(int a, int b)
{
    int r;
    while(b)
    {
        r = a%b;
        a = b;
        b = r;
    }
    return a;
}

int main(int argc, char* argv[])
{
	int c;
	int n;
	vector<int> ti_vec,ti_sub_vec;
	int ti;
	int min_ti;
	int t,y;
	fstream fr("B-small.in",ios::in);
	fr>>c;
	fstream fw;
	fw.open("output.txt",ios::out);

	for(int i=0;i<c;i++)
	{
		ti_sub_vec.clear();
		ti_vec.clear();
		fr>>n;
			for(int j=0;j<n;j++)
			{
				fr>>ti;
				ti_vec.push_back(ti);
			}
			sort(ti_vec.begin(),ti_vec.end());
			for(int m=1;m<ti_vec.size();m++)
		   {
			   int temp=ti_vec[m]-ti_vec[m-1];
				if(temp!=0) ti_sub_vec.push_back(temp);
		   }
			
		while(ti_sub_vec.size()>2)
		{
		   for(int k=1;k<ti_sub_vec.size();k++)
		   {
		
		      	ti_sub_vec[k-1]=sub_min(ti_sub_vec[k-1],ti_sub_vec[k]);
		    	
		   }
		   ti_sub_vec.pop_back();

		}
		if(ti_sub_vec.size()==1)
			t=ti_sub_vec[0];
		else if(ti_sub_vec.size()==2)
		{
			t=gcd(ti_sub_vec[0],ti_sub_vec[1]);
		}
		else 
		{
			 y=0;
			 fw<<"Case #"<<i+1<<": "<<y<<endl;
			 continue;
		}
        min_ti=ti_vec[0];
		min_ti%=t;
		if(min_ti==0) y=0;
		else y=t-min_ti;
		fw<<"Case #"<<i+1<<": "<<y<<endl;


	}
	fr.close();
    fw.close();

	return 0;
}
