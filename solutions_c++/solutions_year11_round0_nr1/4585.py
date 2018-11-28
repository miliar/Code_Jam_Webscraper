#include <stdio.h>
#include <stdlib.h>
#include <vector>

int
getint()
{
    int i;
    if (scanf("%d", &i) != 1) {
        fprintf(stderr, "Could not read integer value\n");
        exit(1);
    }
    return i;
}

int
getchar() {
  char c;
    if (scanf(" %c", &c) != 1) {
        fprintf(stderr, "Could not read char value\n");
        exit(1);
    }
    return c;
}


struct Robot {
  int current_position;
  int current_time;
  const char *name;
  
  Robot(const char *n) : current_position(1), current_time(0), name(n) {}
  
  void moveto(int pos) {
    int dist = abs(current_position-pos);
    current_time += dist;
    current_position = pos;
    
    //printf("%s move to %d time=%d\n", name, pos, current_time);
  }
  
  void wait_for(int time) {
    if (current_time < time) {
      //printf("%s wait for %d time=%d\n", name, time-current_time, current_time);
      
      current_time = time;
      
    }
    
    
  }
  
  void press() {
    current_time++;
    //printf("%s press\n", name);
  }
};



int
main()
{
  int T = getint();
 
  for (int testcase = 0; testcase < T; testcase++) {
    int N = getint();
    
    int orange_pos = 1;
    int blue_pos = 1;
    
    Robot orange("orange"), blue("blue");
    
    int time = 0;
    for (int i = 0; i < N; i++) {
      char color = getchar();
      int position = getint();
      Robot& robot = color == 'O' ? orange : blue;
      
      
      robot.moveto(position);
      robot.wait_for(time);
      robot.press();
      
      time = robot.current_time;
    }
    
    printf("Case #%d: %d\n", testcase+1, time);
  }
  
}