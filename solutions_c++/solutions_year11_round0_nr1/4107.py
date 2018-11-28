/*******************************************************************************
   Charlie Andrews
   Google Codejam Qualification Round, Question 1
******************************************************************************/
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

struct Job {
   char robot;
   int button;
};

// Returns the index of the next job for the robot.
// Returns -1 if there are no remaining jobs
int getNextJob(vector<Job> jobs, int searchStart, char robot) {
   for(int i = searchStart; i < jobs.size(); ++i) {
      if(jobs[i].robot == robot)
         return i;
   }

   return -1;
}

// Moves the robot towards completing the current job, returning the
// robot's new position
int moveRobot(int currentPos, Job currentJob) {
   int desiredPos = currentJob.button;

   if(desiredPos < currentPos)
      return currentPos - 1;
   if(desiredPos > currentPos)
      return currentPos + 1;

   // The robot is at the current position
   return currentPos;
}

int solve(vector<Job> jobs) {
   // Indicates the current job that we're waiting on
   int currentOrangeJob = getNextJob(jobs, 0, 'O');
   int currentBlueJob = getNextJob(jobs, 0, 'B');

   int oPos = 1, bPos = 1;

   int time = 0;

   while(!(currentOrangeJob == -1 && currentBlueJob == -1)) {
      // Move both robots
      int beforeOrange = oPos, beforeBlue = bPos;

      if(oPos != -1)
         oPos = moveRobot(oPos, jobs[currentOrangeJob]);
      if(bPos != -1)
         bPos = moveRobot(bPos, jobs[currentBlueJob]);

      char laggingRobot;
      if(currentOrangeJob == -1)
         laggingRobot = 'B';
      else if(currentBlueJob == -1)
         laggingRobot = 'O';
      else
         laggingRobot = (currentOrangeJob < currentBlueJob) ? 'O' : 'B';

      // Press the button if necessary
      switch(laggingRobot) {
      case 'O':
         if(beforeOrange == oPos) {
            // Press the button, effectively moving onto the next job
            currentOrangeJob = getNextJob(jobs, currentOrangeJob + 1, 'O');
         }
         break;
      case 'B':
         if(beforeBlue == bPos) {
            // Press the button effectively moving onto the next job
            currentBlueJob = getNextJob(jobs, currentBlueJob + 1, 'B'); 
         }
         break;
      default:
         break;
      }
      ++time;
   }

   return time;
}

void PrintJobs(vector<Job> jobs) {
   for(int i = 0; i < jobs.size(); ++i) {
      cout << "Robot " << jobs[i].robot << " presses button " << jobs[i].button << endl;
   }
}

int main() {
   int caseCount;
   cin >> caseCount;
   cin.ignore();
   
   for(int i = 0; i < caseCount; ++i) {
      vector<Job> jobs;

      // Read in the test case
      int jobCount;
      cin >> jobCount;

      for(int j = 0; j < jobCount; ++j) {
         Job newJob;
         cin >> newJob.robot;
         cin >> newJob.button;
         jobs.push_back(newJob);
      }

      int timeToSolve = solve(jobs);

      cout << "Case #" << (i + 1) << ": " << timeToSolve << endl;
   }
}
   
