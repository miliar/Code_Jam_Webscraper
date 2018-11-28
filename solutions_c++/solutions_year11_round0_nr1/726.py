#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <set>
#include <limits>

#define abs(x) ((x) > 0 ? (x) : -(x))

using namespace std;

int main()
{

  int T;
  cin >> T;

  for (int i = 0; i < T; ++i) {

    int N;
    cin >> N;
    
    int total_time = 0;
    int current_bot_time = 0;
    char current_bot = 'O';
    int oposition = 1;
    int bposition = 1;

    for (int j = 0; j < N; ++j) {
      char bot;
      cin >> bot;
      
      int button;
      cin >> button;
      
      int pos = (bot == 'O') ? oposition : bposition;
      int walk_time = abs(pos - button);

      if (bot != current_bot) {
        walk_time = std::max(0, walk_time - current_bot_time);
        current_bot_time = 0;
      }

      int op_time = walk_time + 1;

      current_bot = bot;
      total_time += op_time;
      current_bot_time += op_time;
      if (bot == 'O') 
        oposition = button;
      else
        bposition = button;
    }
    
    cout << "Case #" << i+1 << ": " << total_time << endl;
  }
  
  return 0;
}
