/*
 *  quick.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 07/02/15.
 *  Copyright 2007 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <cmath>
using namespace std;

#include <set>
#include <vector>
#include <map>
#include <algorithm>

#include <iterator>

int main()
{
	int T,N;
	
	cin>>T;
	
	for(int i=0; i<T; ++i)
	{
				
		cin>>N;
		
		int blue_pos = 1, orange_pos = 1;
		
		char temp;
		int new_pos;
		
		int blue_time = 0, orange_time = 0;
		
		int time_cost;
		
		for (int j=0; j<N; ++j) {
			
			cin>>temp>>new_pos;
			
			if(temp == 'O')
			{
				time_cost = 1 + abs(new_pos - orange_pos);
				
				/*
				if(blue_time <= orange_time)
					orange_time += time_cost;
				else
				{
					orange_time += (time_cost - (blue_time - orange_time));
					
					int minimum = blue_time + 1;
					
					if(orange_time < minimum) orange_time = minimum;
				}
				*/
				
				orange_time += time_cost;
				int minimum = blue_time + 1;
				if(orange_time < minimum) orange_time = minimum;
				
				orange_pos = new_pos;
			}
			else
			{
				time_cost = 1 + abs(new_pos - blue_pos);
				//blue_time += (time_cost - min(0, orange_time - blue_time));
				
				blue_time += time_cost;
				int minimum = orange_time + 1;
				if(blue_time < minimum) blue_time = minimum;
				
				blue_pos = new_pos;
			}
			
			//cout<<"O: "<<orange_time<<" B: "<<blue_time<<endl;
			
		}
		
		cout<<"Case #"<<i+1<<": "<<max(orange_time, blue_time)<<endl;
	}
	
	return 0;
}
