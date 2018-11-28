#include <stdio.h>
#include <math.h>

void solveBotTrust(int testCaseNumber)
{
   int numberOfButtons = 0;
   scanf("%d", &numberOfButtons);

   int robotOPosition = 1, robotBPosition = 1;
   int noOfSeconds = 0, robotOSpareSeconds = 0, robotBSpareSeconds = 0;

   for(int i = 0; i < numberOfButtons; i++)
   {
      char robot;
      scanf(" %c", &robot);
      int buttonNo;
      scanf(" %d", &buttonNo);

      if(robot == 'O')
      {
         if(buttonNo != robotOPosition)
         {
            int delta = abs(buttonNo - robotOPosition);
            if(delta > robotOSpareSeconds)
            {
               delta -= robotOSpareSeconds;
            }
            else
            {
               delta = 0;
            }
            robotBSpareSeconds += delta;
            noOfSeconds += delta;
            robotOPosition = buttonNo;
         }
         robotOSpareSeconds = 0;
         robotBSpareSeconds++;
         noOfSeconds++;
      }
      else if(robot == 'B')
      {
         if(buttonNo != robotBPosition)
         {
            int delta = abs(buttonNo - robotBPosition);
            if(delta > robotBSpareSeconds)
            {
               delta -= robotBSpareSeconds;
            }
            else
            {
               delta = 0;
            }
            robotOSpareSeconds += delta;
            noOfSeconds += delta;
            robotBPosition = buttonNo;
         }
         robotBSpareSeconds = 0;
         robotOSpareSeconds++;
         noOfSeconds++;
      }
   }

   printf("Case #%d: %d\n", testCaseNumber + 1, noOfSeconds);
}

int main(int argc, char** argv)
{
   int noOfTestCases = 0;
   scanf("%d", &noOfTestCases);
   for(int i = 0; i < noOfTestCases; i++)
   {
      solveBotTrust(i);
   }
   return 0;
}