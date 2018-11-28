#include <vector>
#include <list>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

string getline(){
	string tmp;
	getline(cin, tmp);
	return tmp;
}

class robot_data {
	public:
	
	int last_button;
	int extra_time;
	
	robot_data(){
		last_button = 1;
		extra_time = 0;
	}
};

void solveCase(){
	stringstream line(getline());
	int N;
	line >> N;
	
	int seconds=0;
	
	map<string, robot_data> robot;
	robot["O"]; robot["B"];
	
	string name;
	int button, new_time;
	
	for(int n=0; n<N; n++){
		line >> name >> button;
		new_time = abs( robot[name].last_button - button )
		           - robot[name].extra_time
		           + 1;
		new_time = max( new_time, 1 );
		
		robot["O"].extra_time += new_time;
		robot["B"].extra_time += new_time;
		robot[name].extra_time = 0;
		robot[name].last_button = button;
		
		seconds += new_time;
	}
	
	cout << seconds << endl;
}

int main(int argc, char *argv[]){
	stringstream line(getline());
	unsigned int T;
	
	line >> T;
	
	for(unsigned int t=1; t<=T; t++){
		cout << "Case #" << t << ": ";
		solveCase();
	}
	
	return 0;
}

