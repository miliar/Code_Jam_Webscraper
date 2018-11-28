#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;



class move {
	public:
		int col;
		int  step;
		
};

vector<move> queue;
int N,T;


int getBlue(int i) {


	for(int a = i; a < N; a++)
		if(queue[a].col == 1) return a;
		
	return -1;

}

int getOrange(int i) {

	for(int a = i; a < N; a++)
		if(queue[a].col == 0) return a;
		
	return -1;

}



int main() {
	


	
	
	cin >> T;
	
	for(int c = 1; c <= T; c++) {
	
	
		cin >> N;
	
		queue.clear();
		for(int i = 0 ; i < N; i++) {
		
			move a;
			int step;
			char col;
		
			cin >> col >> step;
		
			if((int)col == 79) a.col = 0;
			else					 a.col = 1;
		
			a.step = step;
		
		
			queue.push_back( a );
		}
	
		int pos[2] = {1,1}; // 0 = Orange, 1 = Blue
		int moves = 0;
		int id;
		int but;
		
		for(int i = 0 ; i < N; i+=but) {
			but = 0;
		
			if(queue[i].step == pos[queue[i].col]) {
				//cout <<  queue[i].col << " presses the button " << '\t'; 
				moves++;
				but = 1;
			} else {
		
				if(queue[i].step > pos[queue[i].col]) {
					//cout <<  queue[i].col << " moves from " << pos[queue[i].col] << 
					//" to " << pos[queue[i].col]+1 << '\t';
					moves++;
					pos[queue[i].col]++;
				} else {
					//cout <<  queue[i].col << " moves from " << pos[queue[i].col] << 
					//" to " << pos[queue[i].col]-1 << '\t';
					moves++;
					pos[queue[i].col]--;
				} 
			}
		
			if(queue[i].col == 0) {
				id = getBlue(i);
			} else {
				id = getOrange(i);
			}
		
			if(id > -1) {
				if(queue[id].step == pos[queue[id].col]) {
					//cout <<  queue[id].col << " wait " << endl; 
				
				} else {
		
					if(queue[id].step > pos[queue[id].col]) {
						//cout <<  queue[id].col << " moves from " << pos[queue[id].col] << 
						//" to " << pos[queue[id].col]+1 << endl;
				
						pos[queue[id].col]++;
					} else {
						//cout <<  queue[id].col << " moves from " << pos[queue[id].col] << 
						//" to " << pos[queue[id].col]-1 << endl;
				
						pos[queue[id].col]--;
					} 
				}
			} /*else {
				if(queue[id].col == 0)
					//cout << "0 does nothing " << endl;
				else
					//cout << "1 does nothing " << endl;
			}*/
		
		
		
	
		}
	
		cout << "Case #" << c << ": " << moves << endl;
	}

return 0;
}
