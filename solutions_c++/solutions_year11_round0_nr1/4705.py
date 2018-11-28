#include <iostream>

using namespace std;

typedef struct robot_action_t {
	string robot;
	int button;
	bool pushed;
	robot_action_t * previous;
} robot_action_t;

typedef struct {
	string name;
	robot_action_t current;

} robot_t;


robot_action_t * getNextActionPos(int nbOfAction, robot_action_t * rAction, string robotName) {
	int i;
	for (i = 0; i < nbOfAction; i++) {
		if(rAction[i].robot.compare(robotName) == 0 && rAction[i].pushed == false) {
			return &rAction[i];
		}
	}
	return NULL;
}

int main(int argc, const char *argv[])
{
	int T;
	cin >> T;
	//cout << T << endl;
	int N;
	string s;
	int nbO;
	int Opos;
	int nbB;
	int Bpos;

	int i, x;

	int time;
	robot_action_t rAction[100];
	robot_action_t * Oaction;
	robot_action_t * Baction;
	bool lockPushButton;

	for (i = 1; i <= T; i++) {
		cin >> N;
		//cout << N << endl;

		nbO = 0;
		nbB = 0;
		Opos = 1;
		Bpos = 1;

		for (x = 0; x < N; x++) {
			cin >> rAction[x].robot;
			cin >> rAction[x].button;
			rAction[x].pushed = false;
			if(x > 0) {
				rAction[x].previous = &rAction[x-1];
			} else {
				rAction[x].previous = NULL;
			}
		}
		for (x = 0; x < N; x++) {
			//cout << rAction[x].robot << " - " << rAction[x].button << endl;
		}
		x = 0;
		Oaction = getNextActionPos(N, rAction, "O");
		Baction = getNextActionPos(N, rAction, "B");

		for (time = 0; Oaction!= NULL || Baction != NULL; time++) {
			//cout << "time : " << time << endl;
			lockPushButton = false;
			if(Oaction != NULL) {
				//cout << "OOO" << endl;
				if(Opos == Oaction->button ) {
					if (!lockPushButton && (Oaction->previous == NULL || Oaction->previous->pushed == true)) {
						lockPushButton = true;
						Oaction->pushed = true;
						// get next Action...
						Oaction = getNextActionPos(N, rAction, "O");
					}
				} else if(Opos < Oaction->button){
					Opos++;
				} else {
					Opos--;
				}
			}
			if(Baction != NULL) {
				//cout << "BBB" << endl;
				if(Bpos == Baction->button ) {
					if (!lockPushButton && (Baction->previous == NULL || Baction->previous->pushed == true)) {
						lockPushButton = true;
						Baction->pushed = true;
						// get next Action...
						Baction = getNextActionPos(N, rAction, "B");
					}
				} else if(Bpos < Baction->button){
					Bpos++;
				} else {
					Bpos--;
				}
			}
			//cout << "Opos : " << Opos << " - Bpos : " << Bpos << endl;
		}

		cout << "Case #" << i << ": " << time << endl; 
	}

	return 0;
}
