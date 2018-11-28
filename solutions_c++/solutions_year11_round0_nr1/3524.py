#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <stdio.h>

int main(){

  int T;
  scanf("%d\n", &T);

  for(unsigned int c=1; c<=T; ++c){
 
    int N; 
    scanf("%d ", &N);

    unsigned int pos[2] = {1,1};
    unsigned int time[2] = {0,0};

    for(int i=0; i<N; ++i){

      char color; unsigned int button; 
      scanf("%c %d ", &color, &button);
      size_t index = color == 'B' ? 1 : 0;

      size_t dist = std::abs(((int)pos[index]) - ((int)button));
      time[index] = std::max(time[index ? 0 : 1] + 1, time[index] + dist + 1);
      pos[index] = button;

    }

    unsigned int answer = std::max(time[0], time[1]);
    std::cout << "Case #" << c << ": " << answer << "\n";

  }

}



