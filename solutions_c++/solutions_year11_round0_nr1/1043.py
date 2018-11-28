#include <iostream>
using std::cin;
using std::cout;

inline int max(int x,int y)
{
	return (x>y)?x:y;
}

int main()
{
	int t,T;
	
	cin >> T;
	
	for ( t = 0; t < T; t++ )
	{
		int n,N;
		int time1 = 0, time2 = 0;
		int pos1 = 1, pos2 = 1;
		char bot_name;
		int pos_to_reach;

		cin >> N;
		
		for ( n = 0; n < N; n++ )
		{
			cin >> bot_name;
			cin >> pos_to_reach;

			if ( bot_name == 'B' )
			{
				time1 = max(time1 + abs(pos1 - pos_to_reach), time2) + 1;
				pos1 = pos_to_reach;
			}
			else
			{
				time2 = max(time2 + abs(pos2 - pos_to_reach), time1) + 1;
				pos2 = pos_to_reach;
			}
		}
		
		cout << "Case #" << t + 1 << ": " << max(time1,time2) << "\n";
	}
	
	return 0;
}
