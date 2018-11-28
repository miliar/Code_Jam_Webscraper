#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>

using namespace std;
int main()
{
	int T;
	map<char, char> other;
	other['O'] = 'B';
	other['B'] = 'O';

	cin >> T;
	for(int t=1; t<=T; t++){
		int res=0;
		int N;
		map<char, int> robot, moveTime;
		robot['O'] = 1;
		robot['B'] = 1;
		moveTime['O'] = 0;
		moveTime['B'] = 0;
		
		cin >> N;
		for(int n=0; n<N; n++){
			char color;
			int pos;
			cin >> color;
			cin >> pos;
			int time = abs(pos - robot[color]) - moveTime[color];
			if (time < 0)  time = 0;
			time++;
			robot[color] = pos;
			res += time;
			moveTime[color] = 0;
			moveTime[other[color]] += time;
		}
	
		cout << "Case #" << t << ": " << res << endl;
	}
	
	return 0;
}

