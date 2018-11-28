#include <iostream>
using namespace std;

int T;
int N;

struct robot_state{
  int position;
  int time;
};

const int MAX_ROBOTS = 2;
robot_state robots[MAX_ROBOTS];

int read_type(){
  char c;
  cin >> c;
  switch (toupper(c)){
    case 'O': return 0;
    case 'B': return 1;
  }
  cerr<< "error at read_type()" << endl;
  return -1;
}

void clean(){
  for(int i=0; i<MAX_ROBOTS; ++i){
    robots[i].position=1;
    robots[i].time=0;
  }
}

int main(){
  cin >> T;
  for(int Case=1; Case <= T; ++Case){
    clean();
    int current_time = 0;
    cin >> N;
    while(N--){
      robot_state & robot = robots[read_type()];
      int position;
      cin >> position;

      robot.time += abs(robot.position - position);
      robot.position = position;
      current_time = max(current_time, robot.time) +1;
      robot.time = current_time;
    }
    cout << "Case #" << Case <<": " << current_time << endl;
  }
  return 0;
}