#include <cstdio>
#include <vector>
#include <map>

using namespace std;

const int kInf = 1 << 20;
const int DEBUG = 0;

int T, N;

int main() {
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    vector<pair<int, int> > blue_seq;
    vector<pair<int, int> > orange_seq;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
      char R;
      int P;
      scanf(" %c %d", &R, &P);
      if (R == 'B') {
	blue_seq.push_back(make_pair(P, i));
      } else {
	orange_seq.push_back(make_pair(P, i));
      }
    }
    blue_seq.push_back(make_pair(-1, kInf));
    orange_seq.push_back(make_pair(-1, kInf));

    if (DEBUG) {
      printf("Blue: ");
      for (int i = 0; i < blue_seq.size(); ++i) {
	printf("(%d, %d) ", blue_seq[i].first, blue_seq[i].second);
      }
      printf("\n");
      printf("Orange: ");
      for (int i = 0; i < orange_seq.size(); ++i) {
	printf("(%d, %d) ", orange_seq[i].first, orange_seq[i].second);
      }
      printf("\n");
    }

    int ans = 0;
    int blue_turn = 0, orange_turn = 0;
    int blue_pos = 1, orange_pos = 1;
    for (int turn = 0; turn < N; ++turn) {
      pair<int, int> blue_button = blue_seq[blue_turn];
      pair<int, int> orange_button = orange_seq[orange_turn];
      if (blue_button.second == turn) {
	int distance = abs(blue_button.first - blue_pos);
	int delta = orange_button.first - orange_pos;
	blue_pos = blue_button.first;
	if (abs(delta) < (distance)+1) {
	  orange_pos += delta;
	} else {
	  orange_pos += (delta>0?1:-1) * (distance+1);
	}
	ans += distance+1;
	++blue_turn;
      } else if (orange_button.second == turn) {
	int distance = abs(orange_button.first - orange_pos);
	int delta = blue_button.first - blue_pos;
	orange_pos = orange_button.first;
	if (abs(delta) < (distance)+1) {
	  blue_pos += delta;
	} else {
	  blue_pos += (delta>0?1:-1) * (distance+1);
	}
	ans += distance+1;
	++orange_turn;
      }
    }    
    printf("Case #%d: %d\n", t, ans);
  }
}
