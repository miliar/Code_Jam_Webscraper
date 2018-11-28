//#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <string.h>
#include <algorithm>
#include <stack>
#include <map>
#include <list>
#include <cmath>
#include <math.h>
#include <stdlib.h>
#include <vector>
using namespace std;

ifstream cin("E:\\Heyi\\pd\\GoogleJam\\Qualification2010.5.7\\Qualification\\A-large.in");
ofstream cout("E:\\Heyi\\pd\\GoogleJam\\Qualification2010.5.7\\Qualification\\A-large.out");
#define POUT(n,v){cout<<"Case #"<<(n+1)<<": "<<v<<endl;} 

#define  MAX_LEN 200

int main()
{
	
	int status[MAX_LEN];
	list<int> o;
	list<int> b;
	int T;
	cin>>T;
	for (int i=0;i<T;i++)
	{
		int N;
		cin>>N;
		o.clear();
		b.clear();
		
		memset(status,0,MAX_LEN);
		int index=0;
		for (int j=0;j<N;j++)
		{
			int v;
			char ch;
			cin>>ch>>v;
			switch (ch)
			{
			case 'B':
				b.push_back(v);
				status[index++]=1;
				break;
			case 'O':
				o.push_back(v);
				status[index++]=0;
				break;
			}
		}
		o.push_back(0);
		b.push_back(0);
		int step_o=o.front()-1,step_b=b.front()-1;
		int total=0;
		for(int k=0;k<N;k++)
		{
			switch (status[k])
			{
			case 0:
				{	
					step_b-=(step_o+1);
					
					if (step_b<0)
					{
						step_b=0;//WAIT
					}
					total+=step_o;
					step_o=o.front();
					o.pop_front();
					
					step_o=(o.front()-step_o)>0?(o.front()-step_o):-(o.front()-step_o);
				
					
					total++;//press
					break;
				}
			case 1:
				{
					step_o-=(step_b+1);
					
					if (step_o<0)
					{
						step_o=0;//WAIT
					}
					total=total+step_b;
					step_b=b.front();
					b.pop_front();
					
					step_b=(b.front()-step_b)>0?(b.front()-step_b):-(b.front()-step_b);
					
					
					total++;//press	
					break;
				}
			}		
		}
	
		POUT(i,total);
	}
	return 0;
}