#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int opos, bpos;
int steps, steps_arc;
char last_act;

void init(){
	opos = 1;
	bpos = 1;
	steps = 0;
	steps_arc = 0;
	last_act = '0';
};

int getStepCount(int oldpos, int pos){
	return (abs(pos-oldpos)+1); // 1 нажать
}

void iter(char color, int pos){
	int StepCount = 0;
	if (last_act == '0') last_act = color;
	if (color == 'B') {
		StepCount = getStepCount(bpos,pos);
		bpos = pos;
	};
	if (color == 'O') {
		StepCount = getStepCount(opos,pos);
		opos = pos;
		//cout << "opos" << StepCount;;
	};
	
	if (last_act == color)  
		steps_arc += StepCount; // колво времени на задание
		else {
			last_act = color;
			StepCount -= steps_arc;
			if (StepCount < 1) StepCount = 1;
			steps_arc = StepCount;
		}
	steps += StepCount;
}



int main (int argc, char * const argv[]) {
    // insert code here...
	int t,n,k = 0;
	k = 1;
    cin >> t;
	while (t--) { // общее количество
		cin >> n; // кол-во в серии
		init();
		char color;
		int pos;
		cout << "Case #" << k++ << ": ";
		while (n--) {
			cin.get();
			color = cin.get();
			cin.get();
			cin >> pos;
			iter(color,pos);
		}
		cout << steps;
		cout << endl;
	}
    return 0;
}
