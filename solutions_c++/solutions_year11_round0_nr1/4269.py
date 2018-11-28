// Sunny Basi 
//
// you found your way here!
// i reccommend leaving before your brain melts from the horrible code that follows.
// i am rusty at coding. you have been warned.
//
#include <iostream>
#include <utility>
#include <list>
using namespace std;

int main(){
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++){
		list <pair<char,int> > move_list; // list of entire sequence
		list <int> o_list, b_list; // list of sequences for each bot
		int bIndex = 1; // current bot pos
		int oIndex = 1;
		int total = 0; // total moves
		int N; cin >> N;
		
		while (N--) { // input 
			char bot; cin >> bot;
			int button; cin >> button;
			if (bot == 'O') o_list.push_back(button);
			else {
				b_list.push_back(button);
			}
			move_list.push_back(make_pair(bot, button));
		}

		while(!move_list.empty()){
			pair <char,int> currMove;
			currMove = move_list.front();
			
			if ( currMove.first == 'O'){	// ORANGE MOVE
				if (currMove.second == oIndex){
					o_list.pop_front();
					move_list.pop_front();
				}
				else if (oIndex < currMove.second) oIndex++;
				else oIndex--;
			} else {
				if (!o_list.empty()){
					if (oIndex < o_list.front()) oIndex++;
					else if (oIndex > o_list.front()) oIndex--;
				}
			}
			if ( currMove.first == 'B'){   // BLUE MOVE
				if (currMove.second == bIndex){
					b_list.pop_front();
					move_list.pop_front();
				}
				else if (bIndex < currMove.second) bIndex++;
				else bIndex--;
			} else {
				if (!b_list.empty()){
					if (bIndex < b_list.front()) bIndex++;
					else if (bIndex > b_list.front()) bIndex--;
				}
			}
			total++;
		}
		cout << "Case #" << (1 + i) << ": " << total << endl;
	}

	return 0;
}
