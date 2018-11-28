#include <iostream>
#include <queue>

using namespace std;

int main()
{
	queue< int > q;
	
	int num_case, num_ride, max_people, num_group;
	
	cin >> num_case;
	
	for ( int i = 1 ; i <= num_case ; i++ )
	{
		cin >> num_ride >> max_people >> num_group;
		
		int people[num_group];
		bool used[num_group];
		
		for ( int j = 0 ; j < num_group ; j++ )
		{
			cin >> people[j];
		}
		
		int curr_people, money = 0, idx = 0;
		while( num_ride-- )
		{
			curr_people = 0;
			memset( &used, false, num_group * sizeof(bool) );
			
			while( curr_people < max_people )
			{
				if ( curr_people + people[idx] > max_people || used[idx] )
					break;
						
				curr_people += people[idx];
				used[idx] = true;
				
				if ( idx == num_group - 1 )
					idx = 0;
				else
					idx++;	
			}
			
			money += curr_people;
		}
		
		cout << "Case #" << i << ": " << money << endl;
	}
}
