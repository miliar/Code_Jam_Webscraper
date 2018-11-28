
#include <cstdio>
#include <cstring>
#include <assert.h>
#include <stdint.h>
#include <map>
#include <vector>
#include <list>

using namespace std;

char inFileName[64], outFileName[64];
FILE *ifile, *ofile;

class Robot
{
 public:
  void config(char botName);
  void addTask(char botName, int switchNum);
  bool run();
  void eventComplete();
  void clear();

 private:
  char name;
  int seq[101];
  int curPos;
  int nextPos;
  int seqIdx;
  int seqSize;

  int getNextPos();
  bool move();
  bool pushSwitch();
};

Robot B, O;

void Robot::config(char botName)
{
  name = botName;
}

void Robot::addTask(char botName, int switchNum)
{
  seq[seqSize++] = (botName == name) ? switchNum : 0;
}

int Robot::getNextPos()
{
  int i = seqIdx;
  while (0 == seq[i] and i < seqSize) ++i;
  return seq[i];
}

bool Robot::move()
{
  if (nextPos > curPos) {
    curPos++;
  } else if (nextPos < curPos) {
    curPos--;
  } else {
    return true;
  }
  return false;
}

bool Robot::pushSwitch()
{
  if (seq[seqIdx] != 0) {
    eventComplete();
    return true;
  }
  return false;
}

bool Robot::run()
{
  if (not nextPos) nextPos = getNextPos();
  if (move()) {
    return pushSwitch();
  }
  return false;
}

void Robot::eventComplete()
{
  seqIdx++;
  nextPos = getNextPos();
}

void Robot::clear()
{
  name = '\0';
  curPos = 1;
  nextPos = seqIdx = seqSize = 0;
}

int seqSize;

void parse_test_case()
{
  B.clear();
  O.clear();
  B.config('B');
  O.config('O');

  char robotName;
  int switchNum;
  fscanf(ifile, "%d", &seqSize);
  for (int i = 0; i < seqSize; ++i) {
    fscanf(ifile, " %c %d", &robotName, &switchNum);
    B.addTask(robotName, switchNum);
    O.addTask(robotName, switchNum);
  }
  fscanf(ifile, "\n");
}

int exec_tt()
{
  int steps = 0;
  int numCmplts = 0;
  while (numCmplts < seqSize) {
    bool bc = false, oc = false;
    bc = B.run();
    oc = O.run();
    if (bc) {
      O.eventComplete();
      numCmplts++;
    }
    if (oc) {
      B.eventComplete();
      numCmplts++;
    }
    steps++;
  }
  return steps;
}

int main(int argc, char *argv[])
{
  int T;
  printf("Enter the input file: ");
  scanf("%s", inFileName);
  sprintf(outFileName, "%s.out", inFileName);
  sprintf(&inFileName[strlen(inFileName)], ".in");
  printf("Input File: %s\n", inFileName);
  printf("Output File: %s\n", outFileName);
  ifile = fopen(inFileName, "r");
  ofile = fopen(outFileName, "w");
  fscanf(ifile, "%d", &T);

  for (int i = 1; i <= T; ++i) {
    parse_test_case();
    fprintf(ofile, "Case #%d: %d\n", i, exec_tt());
  }
  fflush(ofile);
  fclose(ifile);
  fclose(ofile);
  return 0;
}

