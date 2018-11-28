// newtest.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <list>
#include <queue>
#include <deque>
#include <fstream>
#include <math.h>

using namespace std; 

#define TOGGLE_YTH_BIT(x,y)	\
					(x=x^(0x1<<(y-1))); 


int main(int argc, char* argv[])
{
	short T; 
	cin>>T;

	int l = 0x00002;

	//cout << l; 
	//TOGGLE_YTH_BIT(l,2);
	//cout << l; 

	for(int __i = 0; __i<T;__i++)
	{
		////////////////////////////////////////////////////////////

		// 
		// INPUT 
		// 
		long N, K; 
		cin >> N; 
		cin >> K; 

		long v = 0L;
		long state = 0;
	
		long last = pow(2.0,N)-1;

		long current_run = 0L; 
		while(current_run<K)
		{
			long bit = (v & (1 << N-1)); 
			TOGGLE_YTH_BIT(v,N);	// MSB always gets toggled 
			
			int p = 2;
			if(bit)
			{
				while (bit && (p<=N))
				{
					// keep getting set bits and toggle them until you stop getting
					bit = (v & (1 << N-p)); 
					if(bit)
					{
						TOGGLE_YTH_BIT(v,N-p+1);	
						++p;
					}
				} 
				if(p<=N)
					TOGGLE_YTH_BIT(v,N-p+1); // one 
			}
			++current_run;
		}

		if(last == v)
			state = 1; 
		else
			state = 0;

		cout << "Case #"<<__i+1<<": " << (!state?"OFF":"ON") <<endl;

		////////////////////////////////////////////////////////////
	}

	return 0; 
}

