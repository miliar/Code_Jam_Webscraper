#include <cstdio>
#include <cstdlib>

#define MAX_N 105
#define ORANGE true
#define BLUE false
#define ROBOT(r) ((r) == ORANGE ? orange : blue)
#define ABS(x) ((x) < 0 ? -(x) : (x))

bool sequenceRobots[MAX_N];
int sequenceButtons[MAX_N];

int main() {
   FILE* in = fopen("A-large.in","r");
   FILE* out = fopen("botout.txt","w");
   
   int t;
   fscanf(in, "%d", &t);
   
   for(int i = 0; i < t; i++) {      
      int n;
      fscanf(in, "%d", &n);
      
      int time = 0;
      int blue = 1, orange = 1;
      
      for(int j = 0; j < n; j++) {
         char r = 0;
         int b;
         
         while(r != 'O' && r != 'B') fscanf(in, "%c", &r);
         fscanf(in, "%d", &b);

         if(r == 'O') {
            sequenceRobots[j] = ORANGE;
         } else if(r == 'B') {
            sequenceRobots[j] = BLUE;
         }
         
         sequenceButtons[j] = b;
      }
      
      for(int j = 0; j < n; j++) {
         //printf("Sequence %d:\n", j);
         
         bool r = sequenceRobots[j];
         int b = sequenceButtons[j];

         int dist = ABS(ROBOT(r) - b) + 1; // +1 for button press
         int dir = b - ROBOT(r);
         
         //printf("blue is at %d, orange is at %d\n", blue, orange);
        // if(r == BLUE) printf("BLUE is going to move!\n");
         //else printf("ORANGE is going to move!\n");
         
         //printf("it has to take %d time to move to button %d\n", dist, b);
         
         int oppDist = 0;
         int oppDir = 0;
         // check for any opp. robot buttons left
         for(int k = j + 1; k < n; k++) {
            if(sequenceRobots[k] != r) {
               //printf("other robot can pre-move\n");
               
               // the other robot has to do something
               oppDist = ABS(ROBOT(!r) - sequenceButtons[k]); // can't press button yet
               if(oppDist > dist) {
                  oppDist = dist;
               }
               
               //printf("other robot can use %d time to move %d to button %d\n", dist, oppDist, sequenceButtons[k]);
               
               // direction to move
               oppDir = sequenceButtons[k] - ROBOT(!r);
               if(oppDir > 0 && oppDir > dist) oppDir = dist;
               else if(oppDir < 0 && oppDir < -dist) oppDir = -dist;
               break;
            }
         }
         
         // update positions
         ROBOT(r) += dir;
         ROBOT(!r) += oppDir;
         
         //printf("BLUE is now at %d, ORANGE is now at %d\n", blue, orange);
         
         time += dist;
         
         //printf("the time is %d\n", time);
      }
      
      fprintf(out, "Case #%d: %d\n", i + 1, time);
      //system("PAUSE");
      //         system("cls");
   }
   
   //system("PAUSE");
   
   fclose(in);
   fclose(out);
}
