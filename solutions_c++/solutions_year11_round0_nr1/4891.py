#include <iostream>
#include <queue>
#include <utility>
#include <map>
#include <cstdlib>

using namespace std;

class Robot
{
private:
   int currPos;
   queue<pair<int, int> > buttons;
   queue<int> pendingDone;
public:
   Robot() :
      currPos(1), buttons()
   {
   }
   bool done() const
   {
      return (buttons.size() == 0);
   }
   void processDone(map<int,bool>& steps)
   {
      //Probably only going to run once so this while basicall acts as an if(!empty)
      while (!pendingDone.empty())
      {
         steps[pendingDone.front()] = true;
         pendingDone.pop();
      }
   }
   void addButton(int location, int step)
   {
      buttons.push(pair<int, int> (location, step));
   }
   void go(map<int,bool>& steps)
   {
      if (buttons.empty()) return;
      int nextButton = buttons.front().first;
      int nextStep = buttons.front().second;

      if (currPos == nextButton && steps[nextStep-1])
      {
         buttons.pop();
         pendingDone.push(nextStep);
      }
      else if (currPos < nextButton)
      {
         currPos++;
      }
      else if (currPos > nextButton)
      {
         currPos--;
      }
   }
};

int main(int argc, char* argv[])
{
   //Set up the standard Code Jam, case #, loop setup
   int numCases;
   cin >> numCases;

   for (int x = 1; x <= numCases; x++)
   {
      //Get number of buttons
      int numButtons;
      cin >> numButtons;

      //Create our robots
      Robot orange;
      Robot blue;

      //Map to coordinate if steps are done;
      map<int, bool> steps;
      //Step '0' is always 'done'
      steps[0]=true;

      //Add instructions
      for (int y = 1; y <= numButtons; y++)
      {
         //Get the color and the button number
         char color;
         cin >> color;
         int loc;
         cin >> loc;

         //Mark the current step and uncompleted
         steps[y] = false;

         //Add the button the appropriate robot
         if (color == 'B')
         {
            blue.addButton(loc, y);
         }
         else if (color == 'O')
         {
            orange.addButton(loc, y);
         }
         else
         {
            cerr << "BUG, BAD INPUT, OR SOMETHING!\n";
            exit(1);
         }
      }

      //Solve and time
      int time = 0;
      while (!(orange.done() && blue.done()))
      {
         time++;
         orange.go(steps);
         blue.go(steps);
         orange.processDone(steps);
         blue.processDone(steps);
      }

      //Output results
      cout << "Case #" << x << ": " << time << endl;
   }
   return 0;
}
