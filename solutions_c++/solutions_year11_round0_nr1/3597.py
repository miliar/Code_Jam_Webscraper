#include <iostream>
#include <vector>
using namespace std;

typedef struct {
	int button_id;
	bool robot;
	// true for orange, false for blue
} PlayerAndButton;

void Q1Test() {
  int num_case;
  cin >> num_case;
  for (int c = 0; c < num_case; ++c) {
	  int step;
	  scanf("%d ", &step);
	  //cout << step << endl;
	  vector<PlayerAndButton> pb;
	  PlayerAndButton temp;
	  for (int s = 0; s < step; ++s) {
		 char r;
		  if (s == step - 1) {
			  scanf ("%c %d", &r, &temp.button_id);
		  } else {
              scanf("%c %d ", &r, &temp.button_id);
		  }
		  if (r == 'O') {
			  temp.robot = true;

		  } else {
			  temp.robot = false;
		  }
		  pb.push_back(temp);
		//cout << pb[s].robot << "\t";
		//cout << pb[s].button_id << endl;

	  }
      vector<int> next_step(step);
	  int current[2];
	  current[0] = -1;
	  current[1] = -1;

	  for (int s = step - 1; s >= 0; --s) {
		  bool player = pb[s].robot;

            next_step[s] = current[!player];
			current[player] = pb[s].button_id;
          
	  }

// 	  for (int s = 0; s < step; ++s) {
// 		  cout << pb[s].button_id << " ";
// 	  }
// 	  cout << endl;
// 	  for (int s = 0; s < step; ++s) {
// 		  cout << next_step[s] << " ";
// 	  }
// 	  cout << endl;
	  // end of input
      int location[2];
	  location[0] = 1;
	  location[1] = 1;
	  int total_time = 0;
	  for (int s = 0; s < step; ++s) {
		  bool player = pb[s].robot;
		  int step_time = abs(pb[s].button_id - location[player])+1;
		  total_time += step_time;
          location[player] = pb[s].button_id;

		  player = !player;
		  if (next_step[s] == -1) continue;
		  if (abs(location[player] - next_step[s]) > step_time) {
              if (location[player] > next_step[s]) location[player] -= step_time;
			  else location[player] += step_time;
		  } else {
              location[player] = next_step[s];
		  }

// 		  if (pb[s].robot == true) {
// 			  button_o.push_back(pb[s].button_id);
// 		  } else {
// 			  button_b.push_back(pb[s].button_id);
// 		  }
	  }
	  cout << "Case #" << c + 1 << ": " << total_time << endl;
  }
}

void main() {
Q1Test();
}