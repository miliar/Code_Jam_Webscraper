#include <iostream>
#include <queue>

using namespace std;

const unsigned int ORANGE = 0;
const unsigned int BLUE = 1;

int main() {
  unsigned int T;

  //read in the number of test cases
  cin >> T;
  for (unsigned int i = 0; i < T; ++i) {
    queue< pair< unsigned int, unsigned int > > seq[2];  //btn, order
    unsigned int pos[2] = {1,1};

    //read in the number of buttons
    unsigned int N;
    cin >> N;

    //read in the sequence of buttons for each robot
    for (unsigned int j = 0; j < N; ++j) {
      char bot;
      unsigned int btn;

      cin >> bot >> btn;
      if (bot == 'O')
	seq[ORANGE].push(make_pair(btn, j));
      else
	seq[BLUE].push(make_pair(btn, j));
    }

    unsigned int t = 0;
    while (!seq[ORANGE].empty() || !seq[BLUE].empty()) {
      pair < unsigned int, unsigned int > bot1, bot2;    //color, btn

      //determine which robot to go into position next
      if (seq[ORANGE].empty()) {
	bot1 = make_pair(BLUE, seq[BLUE].front().first);
	bot2 = make_pair(0, 0);
      }
      else if (seq[BLUE].empty()) {
	bot1 = make_pair(ORANGE, seq[ORANGE].front().first);
	bot2 = make_pair(0, 0);
      }
      else if (seq[ORANGE].front().second < seq[BLUE].front().second) {
	bot1 = make_pair(ORANGE, seq[ORANGE].front().first);
	bot2 = make_pair(BLUE, seq[BLUE].front().first);
      }
      else {
        bot1 = make_pair(BLUE, seq[BLUE].front().first);
        bot2 = make_pair(ORANGE, seq[ORANGE].front().first);
      }

      if (bot1.second == pos[bot1.first])
	seq[bot1.first].pop();
      else { //determine next move for bot1
	if (bot1.second > pos[bot1.first])
	  ++pos[bot1.first];
	else if (bot1.second < pos[bot1.first])
	  --pos[bot1.first];
      }


      //always plan next move for bot2
      if (bot2.second != 0) {
	if (bot2.second > pos[bot2.first])
          ++pos[bot2.first];
        else if (bot2.second < pos[bot2.first])
          --pos[bot2.first];
      }

      ++t;
    }

    cout <<"Case #"<<i+1<<": "<<t<<"\n";
  }

  return 0;
}
