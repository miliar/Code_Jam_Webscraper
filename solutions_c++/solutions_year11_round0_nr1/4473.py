
#include <cstdio>
#include <vector>
#include <iostream>

int main(int argc, const char *argv[])
{
    using namespace std;
    size_t T;
	//scanf("%d", &T);
	cin >> T; cin.get();
    for (size_t c = 1; c <= T; c++) {
       size_t buttons;
	   vector<size_t> blue, orange;
	   vector<char> turns;
	   //scanf("%d", &buttons);
	   cin >> buttons;
       for(size_t i = 0; i < buttons; i++) {
		  char robot;
		  size_t button;
          //scanf(" %c %d", &robot, &button);
		  cin >> robot >> button; cin.get();
	      turns.push_back(robot);
		  if (robot == 'B'){
			  blue.push_back(button);
		  }
		  else if (robot == 'O')
			  orange.push_back(button);
		  else
			  printf("unknown robot: %c", robot);
	   }
	   size_t orange_pos = 1, blue_pos = 1, turn_ndx = 0;
	   size_t orange_ndx = 0, blue_ndx = 0;
	   size_t seconds = 0;
	   while(turn_ndx < turns.size()) {
		   seconds++;
		   bool button_pressed = false;
          // both move towards next button 
		  if (orange_ndx < orange.size()) { 
		  if (orange_pos < orange[orange_ndx]) {
			  orange_pos++;
		  }
		  else if (orange_pos > orange[orange_ndx]) {
			  orange_pos--;
		  }
		  else {
			  if (turns[turn_ndx] == 'O') {
				  turn_ndx++;
				  orange_ndx++;
				  button_pressed = true;
			  }
		  }
		  }
		  if (blue_ndx < blue.size()) {
          if (blue_pos < blue[blue_ndx])
			  blue_pos++;
		  else if (blue_pos > blue[blue_ndx])
			  blue_pos--;
		  else {
             if (turns[turn_ndx] == 'B' && !button_pressed) {
				  turn_ndx++;
				  blue_ndx++;
			  }
		  }
		  }
	   }
	   //printf("Case #%u: %u\n",c,seconds);
	   cout << "Case #" << c << ": " << seconds << endl;
    }
	return 0;
}
