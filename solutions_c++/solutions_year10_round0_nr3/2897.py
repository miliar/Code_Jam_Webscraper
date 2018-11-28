#include "stdafx.h"
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin>>T;

	unsigned int R,K,N;
	vector<unsigned int> results;

	for(int i=0; i<T; i++)
	{
		cin>>R;
		cin>>K;
		cin>>N;

		unsigned int *queue = new unsigned int[N+1];
		unsigned int *head = queue;
		unsigned int sum =0;
		unsigned int turnC =0;

		for(int j=0; j<N; j++)
		{
			cin>>queue[j];
		}		
		queue[N] = 0;
		

		//R iter/day
		for(int j=0; j<R; j++)
		{
			turnC = 0;
			unsigned int *current = head;

			do
			{
				turnC += *head;
				head++;

				if(*head == 0)
					head = queue;

			}while(((turnC + *head) <= K) && (current != head));
			
			sum += turnC;
		}

		results.push_back(sum);

		delete[] queue;
	}

	for(int i=0; i<T; i++)
	{
		cout<<"Case #"<<i+1<<": "<<results[i]<<"\n";
	}

	return 0;
}

