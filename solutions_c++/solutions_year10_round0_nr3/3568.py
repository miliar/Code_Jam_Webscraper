// test.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <list>
#include <queue>
#include <deque>
#include <fstream>


using namespace std; 

int main(int argc, _TCHAR* argv[])
{
	short T; 
	cin>>T;
	long y;

	for(int __i = 0; __i<T;__i++)
	{
		////////////////////////////////////////////////////////////
	
		// 
		// INPUT 
		// 
		long R, k, N; 
		queue<long> q;
		queue<long> cq; 

		cin >> R; 
		cin >> k; 
		cin >> N; 
		long t; 
		for(int _i=0; _i<N; _i++) 
		{
			cin >> t; 
			q.push(t);
		}


		// 
		// PROCESS 
		// 

		long rev = 0L; 
	
		long current_run = 0L; 

		while (current_run<R) 
		{ 
			int temp_rev = 0L; 
			while(1) 
			{
				if(q.empty())
					break; 

				if(temp_rev >= k)
					break; 

				long c = q.front(); 
				if( (c+temp_rev) > k ) 
					break;

				temp_rev += c;
				cq.push(c);
				q.pop();
			}

			rev += temp_rev; 

			long nnn = cq.size();
			for(int _i=0; _i<nnn; _i++) 
			{
				long temp = cq.front(); 
				q.push(temp); 
				cq.pop();
			}

			current_run++;
		} 

		cout << "Case #"<<__i+1<<": " << rev <<endl;

		////////////////////////////////////////////////////////////
	}

	return 0;
}


