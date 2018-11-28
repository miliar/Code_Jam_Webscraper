#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <deque>
#include <utility>

using namespace std;

int main() {
	int cases, buttons, movements;

	int orange,blue;
	
	pair<char,int> objective;
	char bot;
	int button;

	bool complete;
	
	cin >> cases;
	
	for(int i = 1; i <= cases; i ++) {
		deque<pair<char,int> > sequence;
		
		cin >> buttons;
		
		for(int k = 0; k < buttons; k++) {
			cin >> bot;
			cin >> button;
			sequence.push_back(make_pair(bot,button));
		}
		
		orange = blue = 1;
		movements = 0;
		
		while(sequence.size() != 0) {

			objective = sequence.front();
			sequence.pop_front();
			complete = false;

			while(complete == false) {
				
				if(objective.first == 'O') {
					if(objective.second > orange)
						orange++;
					else if(objective.second < orange)
						orange--;
					else
						complete = true;
						
					for(int m = 0; m < sequence.size(); m++)
						if(sequence[m].first == 'B') {
							if(sequence[m].second > blue)
								blue++;
							else if(sequence[m].second < blue)
								blue--;
							break;
						}
						

				}
				else  {
					if(objective.second > blue)
						blue++;
					else if(objective.second < blue)
						blue--;
					else					
						complete = true;
						
					for(int m = 0; m < sequence.size(); m++)
						if(sequence[m].first == 'O') {
							if(sequence[m].second > orange)
								orange++;
							else if(sequence[m].second < orange)
								orange--;
							break;
						}
				}				
				movements++;
			}
		}
		cout << "Case #" << i << ": " << movements << endl;
	}
	
	
	return 0;
}
