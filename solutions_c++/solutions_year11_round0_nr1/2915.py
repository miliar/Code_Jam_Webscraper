#include <iostream>
#include <fstream>
using namespace std;

enum Robot {O, B};

struct Turn
{
  unsigned int button;
  Robot robot;
};

struct Game
{
  int currentOrangePosition;
  int currentBluePosition;

};

struct Task
{
  Turn* turns;
  int numOfTurns;
};

int makeStep(const int curActionNumber, Game* game, Turn* task, int len)
{
  int curActionNumberReturn = curActionNumber;
  Turn curTurn = task[curActionNumber];
  if(curTurn.robot == B && game->currentBluePosition == curTurn.button)
  {
    //blue have to press button
    //cout<<"Blue presses the button #" << game->currentBluePosition << std::endl;
    curActionNumberReturn = curActionNumber + 1;
  } else
  {
    //look for nearest Blue turn
    int i;
    for (i = curActionNumber; i < len; i++)
    {
      if (task[i].robot == B) break;
    }

    if (task[i].robot == B)
    {
      //found nearest blue turn
      if (task[i].button == game->currentBluePosition) 
      {
        //Stand still
        //cout<<"Blue stands still on "<<game->currentBluePosition<<endl;
      }else
      {
        if (task[i].button < game->currentBluePosition)
        {
          //move 1 step back
          game->currentBluePosition = game->currentBluePosition - 1;
          //cout<<"Blue moves back to "<<game->currentBluePosition<<endl;
        }else
        {
          //move 1 step fwd
          game->currentBluePosition = game->currentBluePosition + 1;
          //cout<<"Blue moves frwd to "<<game->currentBluePosition<<endl;
        }
      }
    }
  }

  if(curTurn.robot == O && game->currentOrangePosition == curTurn.button)
  {
    //orange have to press button
    //cout<<"Orange presses the button #" << game->currentOrangePosition << std::endl;
    curActionNumberReturn = curActionNumber + 1;
  } else
  {
    //look for nearest Orange turn
    int i;
    for (i = curActionNumber; i < len; i++)
    {
      if (task[i].robot == O) break;
    }

    if (task[i].robot == O)
    {
      //found nearest Orange turn
      if (task[i].button == game->currentOrangePosition) 
      {
        //Stand still
        //cout<<"Orange stands still on "<<game->currentOrangePosition<<endl;
      }else
      {
        if (task[i].button < game->currentOrangePosition)
        {
          //move 1 step back
          game->currentOrangePosition = game->currentOrangePosition - 1;
          //cout<<"Orange moves back to "<<game->currentOrangePosition<<endl;
        }else
        {
          //move 1 step fwd
          game->currentOrangePosition = game->currentOrangePosition + 1;
          //cout<<"Orange moves frwd to "<<game->currentOrangePosition<<endl;
        }
      }
    }
  }
  //if blue have to press button, move array pointer to next
  //if blue have to move - change current blue pos
  
  //if orange have to press button, move array pointer to next
  //if orange have to move - change current orange pos

  return curActionNumberReturn;
}

int solveTestcase(Turn* task, int len)
{
  Game* game = new Game; 
  game->currentBluePosition = 1;
  game->currentOrangePosition = 1;
  int curActionNumber = 0;
  int steps = 0;
  while(curActionNumber < len)
  {
    curActionNumber = makeStep(curActionNumber, game, task, len);
    steps++;
  }
  //cout<<"\nSteps performed: "<<steps<<endl;
  return steps;
}

int main ()
{
  //Turn* task = new Turn[100];
  //task[0].button = 2;
  //task[0].robot = O;
  //task[1].button = 1;
  //task[1].robot = B;
  //task[2].button = 2;
  //task[2].robot = B;
  //task[3].button = 4;
  //task[3].robot = O;
  //solveTestcase(task, 4);
  //
  /*Turn* task = new Turn[100];
  task[0].button = 5;
  task[0].robot = O;
  task[1].button = 8;
  task[1].robot = O;
  task[2].button = 100;
  task[2].robot = B;
  solveTestcase(task, 3);*/

  Task* allTasks;
  int numOfTasks;
  ifstream myfile ("input.txt");
  if (myfile.is_open())
  {
    myfile >> numOfTasks;
    //cout << "Num of tasks = "<<numOfTasks<<endl;
    
    allTasks = new Task[numOfTasks];
    for (int i =0; i<numOfTasks; i++)
    {
      int numOfTurns;
      myfile >> numOfTurns;
      //cout << "Num of turns = "<<numOfTurns<<endl;

      Turn* task = new Turn[numOfTurns];
      for (int j = 0; j < numOfTurns; j++)
      {
        char r;
        int butt;
        myfile >> r >> butt;
        //cout<<"j = "<<j<<" R = "<<r << " Button = "<<butt<<endl;

        task[j].button = butt;
        task[j].robot = (r=='O'?O:B);
      }

      allTasks[i].turns = task;
      allTasks[i].numOfTurns = numOfTurns;
    }

    myfile.close();
  }else cout << "Unable to open file"; 

  ofstream out;
  out.open ("output.txt");

  //cout << "Num of tasks = "<<numOfTasks<<endl;
  for (int i = 0; i<numOfTasks;i++)
  {
    //cout<<"Output task #"<<i<<endl;
    //for (int j = 0; j < allTasks[i].numOfTurns; j++) cout<<"  "<<j<<" : "<<(allTasks[i].turns[j].robot == O?'O':'B')<<" : "<<allTasks[i].turns[j].button<<endl;
    out<<"Case #"<<(i+1)<<": " << solveTestcase(allTasks[i].turns, allTasks[i].numOfTurns) << endl;
  }
  out.close();

  return 0;
}

