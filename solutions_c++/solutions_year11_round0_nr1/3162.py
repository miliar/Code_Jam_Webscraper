#include <iostream>

using namespace std;

#define DEBUG 0

#define MAX_N 100

int n;

int button[MAX_N];
char color[MAX_N];

int pos_blue, pos_orange;
int idx_blue, idx_orange;
int push_wait_blue, push_wait_orange;
int nb_blue, nb_orange;

int t;

static inline void read_input()
{
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> color[i];
    cin >> button[i];
  }
#if DEBUG == 1
  cout << "n = " << n << endl;
  for (int i = 0; i < n; ++i) {
    cout << "button[" << i << "]=" << button[i] << endl;
    cout << "color[" << i << "]=" << color[i] << endl;
  }
#endif
}

static inline void reset()
{
  read_input();
  pos_blue = pos_orange = 1;
  push_wait_blue = push_wait_orange = 0;
  idx_blue = idx_orange = -1;
  nb_blue = nb_orange = 0;
}

static inline int get_next_button(char col, int& idx, int& waits)
{
  waits = 0;
  for (++idx; idx < n; ++idx) {
    if (color[idx] == col)
      return button[idx];
    ++waits;
  }
  return 0;
}

static inline void wait(char col)
{
#if DEBUG == 1
  cout << "Wait " << col << endl;
#endif
}

static inline void move(char col, int target, int& pos)
{
  target > pos ? ++pos : --pos;
#if DEBUG == 1
  cout << "Move " << col << " " << pos << endl;
#endif
}

static inline void push(char col, int but)
{
#if DEBUG == 1
  cout << "Push " << col << " " << but << endl;
#endif
}

static inline int step() 
{
  bool pushed = false;
#if DEBUG == 1
  cout << "idx_blue = " << idx_blue << " idx_orange = " << idx_orange << endl;
#endif
  if (!nb_blue)
    nb_blue = get_next_button('B', idx_blue, push_wait_blue);
  if (!nb_orange)
    nb_orange = get_next_button('O', idx_orange, push_wait_orange);
  if (!nb_blue && !nb_orange)
    return 0;
  if (nb_blue) {
    if (nb_blue != pos_blue) {
      move('B', nb_blue, pos_blue);
    } else if (push_wait_blue) {
      wait('B');
    } else {
      push('B', nb_blue);
      nb_blue = 0;
      --push_wait_orange;
      pushed = true;
    }
  }

  if (nb_orange) {
    if (nb_orange != pos_orange) {
      move('O', nb_orange, pos_orange);
    } else if (push_wait_orange || pushed) {
      wait('O');
    } else {
      push('O', nb_orange);
      nb_orange = 0;
      --push_wait_blue;
    }
  }
  return 1;
}

int main()
{
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int time = 0;
    reset();
    while (step()) {
#if DEBUG == 1
      cout << "Time: " << time << endl;
#endif
      ++time;
    }
    cout << "Case #" << i + 1 << ": " << time << endl;
  }
  return 0;
}
