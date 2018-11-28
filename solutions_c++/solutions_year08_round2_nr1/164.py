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

struct ele
{
	int i, j;
	
	ele(int i_, int j_)
	:i(i_), j(j_)
	{}
	
	ele()
	:i(), j()
	{}
	
};

int main()
{
	int N_of_cases=0;
	cin >> N_of_cases;
	
	for(int LOOP=0; LOOP<N_of_cases; ++LOOP)
	{
		long long n, A, B, C, D, x, y, M;
		cin >> n >> A >> B >> C >> D >> x >> y >> M;
	
		vector<ele> con(n);

			con[0].i = x%3;
			con[0].j = y%3;
		
		//cout<<x<<' '<<y<<endl;
		
		for(int i=1; i<n; ++i)
		{
			x = (A*x + B) % M;
			y = (C*y + D) % M;
			
			con[i].i = x%3;
			con[i].j = y%3;
			
			
		//cout<<x<<' '<<y<<endl;
		
		}
		
		long long ans = 0;
		
		for(int i=0; i<n; ++i)
			for(int j=i+1; j<n; ++j)
				for(int k=j+1; k<n; ++k)
				{
			
					if(
					((con[i].i+con[j].i+con[k].i)%3 == 0)
					
					&& 
					
					((con[i].j+con[j].j+con[k].j)%3 == 0)
					
					)
						++ans;
				
				}
		
		cout<<"Case #"<<LOOP+1<<": "<<ans<<endl;	
	}
}

