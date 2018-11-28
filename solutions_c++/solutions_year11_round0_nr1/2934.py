#include <cstdio>
#include <cmath>
#include <cstring>
#define MAX 110
#define DEBUG 0

int distance(char *robot, char match, int index) {
  int max = strlen(robot);
  while (match != robot[index]) {
    index++;
    if (index == max) break;
  }
  return index;
}

int main () {
  int kases;
  scanf("%d", &kases);
  for (int i = 1; i <= kases; i++) {  
    char robot[MAX] = {};
    int positions[MAX] = {0};
    int N;
    scanf("%d", &N);
    getchar();
    for (int j = 0; j < N; j++) {
      scanf("%c", &robot[j]);
      scanf("%d", &positions[j]);
      getchar();
    }
    #if DEBUG
    for (int j = 0; j < N; j++) {
      printf("%c", robot[j]);
    }
    printf("Inputting done - %d\n", i);
    #endif
    // Inputting done
    char robot_in_action = '\0';
    char inactive_robot = '\0';
    int distance_next_position, next_index, local_time, distance_left = positions[0]-1;
    int total_time = 0;
    int inactive_robot_position = 1;
    for (int j = 0; j < N; j++) {
      robot_in_action = robot[j];
      inactive_robot = (robot_in_action == 'B') ? 'O' : 'B';
      #if DEBUG
        printf("active - %c, inactive - %c\n", robot_in_action, inactive_robot);
      #endif
      next_index = distance(robot, inactive_robot, j);
      inactive_robot_position = (j > 0) ? positions[j-1] : 1;
      if (next_index == N)
        distance_next_position = 0;
      else
        distance_next_position = (int)fabs(inactive_robot_position - positions[next_index]);
      local_time = distance_left+1; // for the current position
      while (j < next_index-1) {
        local_time += (int)fabs(positions[j] - positions[j+1])+1;
        #if DEBUG
          printf("l_t = %d, J = %d\n", local_time, j);
        #endif
        j++;
      } // for the next positions
      total_time += local_time;
      distance_left = (distance_next_position <= local_time) ? 0 : distance_next_position-local_time;
      #if DEBUG
        printf("dist_left = %d, time = %d, l_t = %d, next_index = %d, dist_nect = %d\n", 
         distance_left, total_time, local_time, next_index, distance_next_position);
      #endif
    }
    printf("Case #%d: %d\n", i, total_time);
  }
}
