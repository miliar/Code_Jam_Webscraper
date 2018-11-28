// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

vector<int> v1,v2;

bool great(int t1,int t2)
{
	return t1 > t2;
}

void show(vector<int> &t)
{
	vector<int>::iterator iter;
	for(iter = t.begin(); iter != t.end(); iter++)
	{
		cout << *iter << " ";
	}
	cout << endl;
	
}

int solve(vector<int> &v1,vector<int> &v2)
{
	int sum = 0;
	int i = 0;
	int size = v1.size();
	for(i = 0; i < size; i++)
	{
		sum += v1[i] * v2[i];
	}
	return sum;
}

int main(int argc, char* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	int i;
	for(i = 1; i <= T; i++)
	{
		int n,temp,j;
		cin >> n;
		v1.clear();
		for(j = 0; j < n; j++)
		{
			cin >> temp;
			v1.push_back(temp);
		}
		v2.clear();
		for(j = 0; j < n; j++)
		{
			cin >> temp;
			v2.push_back(temp);
		}
		sort(v1.begin(),v1.end());
		
//		show(v1);
		sort(v2.begin(),v2.end(),great);
		cout << "Case #" << i << ": " << solve(v1,v2) << endl;
//		show(v2);
	}
	return 0;
}
