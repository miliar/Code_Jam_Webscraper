#include <vector>
#include <queue>
#include <iostream>

using namespace std;

struct Pair{
	char robot;
	int buttonPosition;
};

bool isSamePair(Pair p1, Pair p2){
	if((p1.buttonPosition == p2.buttonPosition) && (p1.robot == p2.robot)){
		return true;
	}
	return false;
}

struct State{
	Pair blue;
	Pair orange;
};

int status(int a, int b){ // 0 means a = b, 1 means bigger a > b, -1 means smaller a < b
	if(a == b){
		return 0;
	}
	if(a < b){
		return -1;
	}
	return 1;
}

int main(){
	int cases = 0;
	cin>>cases;
	for(int i = 0; i < cases; i++){
		int num = 0;
		cin>>num;
		queue<Pair> orange;
		queue<Pair> blue;
		queue<Pair> All;
		for(int j = 0; j < num; j++){
			char c = char('\0');
			int buttonPosition = 0;
			cin>>c>>buttonPosition;
			Pair p = {c, buttonPosition};
			c == 'B' ? blue.push(p) : orange.push(p); // if its blue then push it in blue otherwise orange
			All.push(p);
		}

		int currentBluePosition = 1, currentOrangePosition = 1, answer = 0;

		while(All.empty() == false){
			Pair orangeState = {'\0', -1};
			Pair blueState = {'\0', -1};
			if(orange.size() > 0)
				orangeState = orange.front();
			if(blue.size() > 0)
				blueState = blue.front();
			bool isQueuePopped = false;				

			// Dr. Orange

			int statusOfOrange = status(currentOrangePosition, orangeState.buttonPosition);				

			// case 1: current position is less than state position
			if(statusOfOrange == -1){					
				currentOrangePosition++;
			}
			// case 2: current position is more than state position
			if(statusOfOrange == 1){					
				currentOrangePosition--;
			}
			// case 3 : if they are the same then check if we should push the button or not?
			// we should push the button is the most recent element in the All queue is that one
			
			// I need to update this part of the code as well ............................................................................................
			// Add additonal error checking
			
			if(statusOfOrange == 0){
				// two choices : either you push the button or you stay there
				// you push is the most recent element in the queue is same as state
				bool areTheySame = false;
				if(All.size() > 0){
					areTheySame = isSamePair(All.front(), orangeState);
				}
				if(areTheySame == true){
					answer++;
					if(All.size() > 0)
						All.pop();
					if(orange.size())
						orange.pop();
					isQueuePopped = true;
				}				
			}

			// Dr. Blue

			int statusOfBlue = status(currentBluePosition, blueState.buttonPosition);

			// case 1: current position is less than state position
			if(statusOfBlue == -1){					
				currentBluePosition++;
			}
			// case 2: current position is more than state position
			if(statusOfBlue == 1){					
				currentBluePosition--;
			}
			// case 3 : if they are the same then check if we should push the button or not?
			// we should push the button is the most recent element in the All queue is that one
			if(statusOfBlue == 0){
				// two choices : either you push the button or you stay there
				// you push is the most recent element in the queue is same as state
				bool areTheySame = false;
				if(All.size() > 0){
					areTheySame = isSamePair(All.front(), blueState);
				}
				if(areTheySame == true && isQueuePopped == false){
					answer++;
					if(All.size() > 0)
						All.pop();
					if(blue.size() > 0)
						blue.pop();
					isQueuePopped = true;
				}				
			}

			if((statusOfBlue == 1 || statusOfBlue == -1 || statusOfOrange == 1 || statusOfOrange == -1) && isQueuePopped == false){
				answer++;
			}
		}
		cout<<"Case #"<<i + 1<<": "<<answer<<endl;
	}	
	return 0;
}
