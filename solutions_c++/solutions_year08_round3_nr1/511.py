// a_large.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define MAXN 1010

vector<__int64> vect[MAXN];
vector<__int64> vec;

// void show(vector<__int64> vec1)
// {
// 	vector<__int64>::iterator iter;
// 	for(iter = vec1.begin(); iter != vec1.end(); iter++)
// 		cout << *iter << " ";
// 	cout << endl;
// }


bool great(__int64 a,__int64 b)
{
	return a>b;
}

__int64 solve(__int64 p,__int64 k,__int64 l)
{
	sort(vec.begin(),vec.end());
	__int64 i;
	//	show(vec);
	
	while(!vec.empty())
	{
		for(i = 0; i < k; i++)
		{
			if(!vec.empty())
			{
				__int64 temp = vec.back();
				vec.pop_back();
				vect[i].push_back(temp);
			}
			else
				break;
			
		}
	}
	// 	for(i = 0; i < k; i++)
	// 		show(vect[i]);
	__int64 sum = 0;
	for(i = 0; i < k; i++)
	{
		__int64 j;
		for(j = 0; j < vect[i].size(); j++)
		{
			sum += vect[i][j] * (j+1);
		}
		
	}
	return sum;
	
}
int main(int argc, char* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	__int64 cases;
//	cin >> cases;
	scanf ("%I64d", &cases);
	__int64 i;
	for(i = 1; i <= cases; i++)
	{
		__int64 p,k,l,j,temp;
		scanf ("%I64d %I64d %I64d", &p,&k,&l);
//		cin >> p >> k >> l;
		vec.clear();
		
		__int64 ii;
		for(ii = 0; ii < MAXN; ii++)
		{
			vect[ii].clear();
		}
		for(j = 0; j < l; j ++)
		{
		//	cin >> temp;
			scanf ("%I64d", &temp);
			vec.push_back(temp);
		}
//		cout << "Case #" << i << ": " << solve(p,k,l) << endl;
		printf("Case #%I64d: %I64d\n",i,solve(p,k,l));
	}
	
	return 0;
}
