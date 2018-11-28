/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Sat 07 May 2011 07:54:45 PM CST

 @Created By: Zhai Yan

 @Purpose :
        template for gcj

*******************************************************************************/


#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>

using namespace std;

#define ROB_O_COLOR 0
#define ROB_B_COLOR 1

struct RobPos {
  int color;
  int pos;
};

template <class T>
static inline void check_min(T& dst, const T src) {
  if (dst > src) dst = src;
}

template <class T>
static inline void check_max(T& dst, const T src) {
  if (dst < src) dst = src;
}


static void solve(int t)
{
  vector<RobPos> pos_seq;
  int last_pos[2]  = {1, 1};
  int last_time[2] = {0, 0};
  int global_time  = 0;

  /*
   *  Get input sequence
   */
  int seq_count;
  scanf("%d", &seq_count);
  for (int i = 0; i < seq_count; i++) {
    char tmp_color[4];
    RobPos new_pos;
    scanf("%s%d", tmp_color, &new_pos.pos);
    if (strcmp(tmp_color, "B") == 0) {
      new_pos.color = ROB_B_COLOR;
    } else {
      new_pos.color = ROB_O_COLOR;
    }
 //   fprintf(stderr, "debug: color = %d, step = %d\n", new_pos.color, new_pos.pos);
    pos_seq.push_back(new_pos);
  }


  /*
   *  Simulate the sequence
   */

  for (vector<RobPos>::iterator it = pos_seq.begin(); it != pos_seq.end(); ++it) {
 //   fprintf(stderr, "debug: last btime = %d, last bpos = %d, last otime = %d, last opos = %d\n", last_time[1],
 //                                                                                         last_pos[1],
  //                                                                                        last_time[0],
  //                                                                                        last_pos[0]);
    int end_time = last_time[1 - it->color] + 1; /* one step slower than previous end */
    check_max(end_time, last_time[it->color] + abs(last_pos[it->color] - it->pos) + 1);
    global_time = end_time;
    last_time[it->color] = end_time;
    last_pos[it->color]  = it->pos;
  }
  printf("%d", global_time);
}


int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n", i + 1);
  }
  return 0;
}





