#include <iostream>
#include <stack>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int test_case = 1; test_case <= T; test_case++) {
    int H,W;
    cin >> H >> W;
    int map[H][W];
    char label[H][W];

    for (int i = 0; i < H; i++)
      for (int j = 0; j < W; j++) {
	cin >> map[i][j];
	label[i][j] = '0';
      }

    char label_c = 'a';
    cout << "Case #" << test_case << ":" << endl;
    for (int h = 0; h < H; h++)
      for (int w = 0; w < W; w++) {
	int cur_h = h, cur_w = w;
	stack<int> stack;
	while (true) {
	  if (label[cur_h][cur_w] != '0') { // A sink having been found before.
	    while(!stack.empty()) {
	      int cur_stack_w = stack.top();
	      stack.pop();
	      int cur_stack_h = stack.top();
	      stack.pop();
	      label[cur_stack_h][cur_stack_w] = label[cur_h][cur_w];
	    }
	    break;
	  }

	  int th = cur_h, tw = cur_w; // To see flow to which direction.
	  if (cur_h-1 >= 0 && map[cur_h-1][cur_w] < map[th][tw]) {
	    th = cur_h-1;
	    tw = cur_w;
	  }
	  if (cur_w-1 >= 0 && map[cur_h][cur_w-1] < map[th][tw]) {
	    th = cur_h;
	    tw = cur_w-1;
	  }
	  if (cur_w+1 < W && map[cur_h][cur_w+1] < map[th][tw]) {
	    th = cur_h;
	    tw = cur_w+1;
	  }
	  if (cur_h+1 < H && map[cur_h+1][cur_w] < map[th][tw]) {
	    th = cur_h+1;
	    tw = cur_w;
	  }

	  if (cur_h == th && cur_w == tw) { // A new sink.
	    label[cur_h][cur_w] = label_c;
	    while(!stack.empty()) {
	      cur_w = stack.top();
	      stack.pop();
	      cur_h = stack.top();
	      stack.pop();
	      label[cur_h][cur_w] = label_c;
	    }
	    label_c++;
	    break;
	  } else { // Go along the basin.
	    stack.push(cur_h);
	    stack.push(cur_w);
	    cur_h = th;
	    cur_w = tw;
	  }
	}
      }

    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++)
	cout << label[i][j] << " ";
      cout << endl;
    }


  }

}


