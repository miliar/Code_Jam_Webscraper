#include <iostream>
#include <list>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

typedef unsigned long long int bigint;

int main (int argc, char * const argv[]) {
	
	// READ IN INPUT
	int cases;	
	cin >> cases;
	
	bigint R, k;
	int N;

	for (int c=1; c<=cases; c++)
	{
		
		//STORE ALL QUEUE SEQUENCES TO LOOK FOR RECURRING CYCLE
		//PAIR QUEUE WITH NUMBER BOARDED TO SAVE CALCS/FOR CONVENIENCE
		vector<pair<list<bigint>, bigint> > cycle;
		
		//euros made
		bigint e = 0;
		
		// CASE INFO
		cin >> R >> k >> N;
		
		// READ IN QUEUE
		list<bigint> queue;
		list<bigint> roller;
		bigint t;
		for (int i=0; i<N; i++)
		{
			cin >> t;
			queue.push_back(t);
		}
		//cout << "DB: poeple in queue: " << queue.size() << endl;
		
		// OPEN THE ROLLERCOASTER
		for (bigint i=0; i<R; i++)
		{
			// check if this queue has been seen
			bool match = false;
			int start, finish;
			for (int j=0; j<cycle.size();j++)
			{
				//pair<list<bigint>, bigint> tpair = cycle[j];
				//list<bigint> tlist = tpair.first;
				if (cycle[j].first == queue)
				{
					start = j;
					finish = i;
					match = true;
					//cout << "queue seen! R:" << i << " = " << j << endl;
					break;
				}
			}
			
			if (match)
			{
				int period = finish - start;
				int left = (R-i);
				// add all people to board for remaining runs
				
				for (int j=0; j<left; j++)						
					e += cycle[start + j%period].second;
				
				// break case;
				break;
			}
			
			// else do it the long way
			
			list<bigint> record_queue = queue;			
			list<bigint>::iterator it;
			
			bigint on = 0;
			bigint boarding=0;

			boarding = queue.front();
			
			// while there is still space and people queing
			while( (boarding+on) <= k && queue.size()>0)
			{
				on += boarding;
				e += boarding;
				//cout << "p" << endl;
				queue.pop_front();

				roller.push_back(boarding);
				
				if (queue.size()>0)
					boarding = queue.front();	
			}
			//SAVE QUEUE AND NUMBER BOARDED
			//e += on;
			pair<list<bigint>, bigint> QBpair;
			QBpair.first = record_queue;
			QBpair.second = on;
			cycle.push_back(QBpair);
			//cout << "adding: " << on << endl;
			//cout << "e: " << e << endl;	
			//cout << "go!" << endl;			
			// ROLLER PEOPLE JOIN BACK OF QUEUE
			
			it = queue.end();
			queue.splice(it, roller);
		}
		
		cout << "Case #" << c << ": " << e << endl;
		
	}

    return 0;
}
