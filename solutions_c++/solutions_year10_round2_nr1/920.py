// round1B_1.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <set>
using namespace std;

set<string> records;

int main(int argc, char* argv[])
{
	int testcase;
	int n,m;
	scanf("%d",&testcase);
	for (int caseId =1 ; caseId <= testcase; caseId++)
	{
		printf("Case #%d:",caseId);
		//*****begin
		cin>>n>>m;
		int i,j;
		records.clear();
		records.insert("/");
		for (i=0; i < n;i++)
		{
			string t;
			cin>>t;
			records.insert(t);
		}

		set<string>::iterator iter;
		int result = 0;
		for (i =0;i<m;i++)
		{
			string t;
			cin>>t;
			int count = records.count(t);
			if (count == 0)
			{
				int last = t.length()-1;
				records.insert(t);
				result++;
				while(1)
				{
					int loc = t.find_last_of('/',last);
					loc = max(loc,1);
					//string temp(t.begin(), iter);
					string temp = t.substr(0,loc);
					int num = records.count(temp);
					if (num > 0 )
					{
						break;
					}
					else 
					{
						records.insert(temp);
						result++;
						t = temp;
					}
				}
				
			}
			
		}

		//****end
		printf(" %d\n", result );
		
	}
	return 0;
}

