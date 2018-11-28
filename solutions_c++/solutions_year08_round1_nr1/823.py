/*
 *  1.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 08/07/25.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>


using namespace std;

int main()
{
	int N=0;
	cin >> N;
	
	for(int i=0; i<N; ++i)
	{
		int len=0;
		cin >> len;
		
		vector<int> A;
		vector<int> B;
		
		for(int j=0; j<len; ++j)
		{
			int temp;
			cin >> temp;
			
			A.push_back(temp);
		}
		
		for(int j=0; j<len; ++j)
		{
			int temp;
			cin >> temp;
			
			B.push_back(temp);
		}
		
		sort(A.begin(), A.end());
		sort(B.rbegin(), B.rend());
		
		int p = inner_product(A.begin(), A.end(), B.begin(), 0);
		
		cout<<"Case #"<<i+1<<": "<<p<<endl;
	
	}
}

