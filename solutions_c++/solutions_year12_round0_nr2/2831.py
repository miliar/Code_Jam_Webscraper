#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>

using namespace std;

int main(){	
	
	int T;
	cin >> T;
	
	for (int o = 1; o <= T; o++)
	{
		int N,S,P;
		cin >> N >> S >> P;
		
		int count = 0;
		
		for (int i = 0; i < N; i++)
		{
			int total;
			cin >> total;
			
			int maxInNon;
			int maxInSur;
			
			if( total == 0 )
			{
				maxInNon = maxInSur = 0;
			}
			else if( total%3 == 0 )
			{
				maxInNon = total/3;
				maxInSur = ( total/3 + 1 <= 10 ) ? total/3 + 1 : total/3;
			}
			else if( total%3 == 1 )
			{
				maxInNon = total/3 + 1;
				maxInSur = total/3 + 1;
			}
			else if( total%3 == 2 )
			{
				maxInNon = total/3 + 1;
				maxInSur = ( total/3 + 2 <= 10 ) ? total/3 + 2 : total/3 + 1;
			}
			
			if( maxInNon >= P )
				count++;
			else if( maxInSur >= P && S > 0 )
			{
				count++;
				S--;
			}
		}
		
		cout << "Case #" << o << ": " << count << endl;
	}
	
	return 0;
}

