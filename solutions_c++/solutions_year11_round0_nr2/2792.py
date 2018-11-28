#include <iostream>
#include <fstream>
using namespace std;


struct Combination
{
  char first; 
  char second;
  char third;
};

struct Combinations
{
  Combination* combosArray;
  int combosLen;
};

struct Opposite
{
  char first; 
  char second;
};

struct Opposites
{
  Opposite* opposArray;
  int oppositeLen;
};

struct Task
{
  Opposites oppos;
  Combinations combos;
  char* input;
  int inputLength;
};

char getCombo(char first, char second, Combinations combos)
{
  for (int i = 0; i < combos.combosLen; i++)
  {
    if ((combos.combosArray[i].first == first && combos.combosArray[i].second == second)||(combos.combosArray[i].second == first && combos.combosArray[i].first == second))
      return combos.combosArray[i].third;
  }

  return ' ';
}

bool destroyOpposites(char* str, int len, Opposites oppos)
{
  for (int i = 0; i < len; i++)
  {
    for (int j = 0; j < len; j++)
    {
      if (j==i) continue;
      for (int k = 0; k < oppos.oppositeLen; k++)
      {
        if ((oppos.opposArray[k].first == str[i] && oppos.opposArray[k].second == str[j])||(oppos.opposArray[k].second == str[i] && oppos.opposArray[k].first == str[j])) return true;
      }
    }
  }
  return false;
}

void solveCase(Task task,  ofstream& out)
{
  char* outStr = new char[task.inputLength];
  int outLength = 0;

  for (int i = 0; i < task.inputLength; ++i)
  {
    char newSymbol = task.input[i];
    outStr[outLength] = newSymbol;
    outLength++;
    //find combs in the end
    if (outLength >= 2)
    {
      char comb='1';
      while (comb != ' ')
      {
        comb = getCombo(outStr[outLength-1], outStr[outLength-2], task.combos);
        if (comb!=' ')
        {
          outStr[outLength-2] = comb;
          outLength--;
        }
        if(destroyOpposites(outStr, outLength, task.oppos))
        {
          outLength = 0;
          break;
        }
      }
    }
    if(destroyOpposites(outStr, outLength, task.oppos))
    {
      outLength = 0;
    }
  }

  for (int i = 0; i < outLength; i++)
  {
    out << outStr[i];
    if (outLength - i > 1) out<<", ";
  }


}


int main ()
{
  Task* allTasks;
  int numOfTasks;
  ifstream inp ("input.txt");
  if (inp.is_open())
  {
    inp >> numOfTasks;
    //cout<<"num of cases is "<<numOfTasks<<endl;
    allTasks = new Task[numOfTasks];
    for (int i = 0; i < numOfTasks; ++i)
    {
      Task* task = new Task;
      //cout<<"Case #"<<i<<endl;
      int numOfCombinations;
      inp>>numOfCombinations;
      //cout<<"num of combinations is "<<numOfCombinations<<endl;
      task->combos.combosArray = new Combination[numOfCombinations];
      task->combos.combosLen = numOfCombinations;
      for (int j = 0; j < numOfCombinations; ++j)
      {
        char first, second, third;
        inp >> first >> second>>third;
        //cout<<"  +:"<< first <<" + "<<second<<" = "<<third<<endl;
        task->combos.combosArray[j].first = first;
        task->combos.combosArray[j].second = second;
        task->combos.combosArray[j].third = third;
      }
      int numOfOpposites;
      inp>>numOfOpposites;
      //cout<<"num of opposites is "<<numOfOpposites<<endl;
      task->oppos.opposArray = new Opposite[numOfOpposites];
      task->oppos.oppositeLen = numOfOpposites;
      for (int j = 0; j < numOfOpposites; ++j)
      {
        char first, second;
        inp >> first >> second;
        //cout<<"  -:"<< first <<" <-> "<<second<<endl;
        task->oppos.opposArray[j].first = first;
        task->oppos.opposArray[j].second = second;
      }
      int lengthOfInput;
      inp>>lengthOfInput;
      //cout<<"length of input is "<<lengthOfInput<<endl;
      task->input = new char[lengthOfInput];
      task->inputLength = lengthOfInput;
      for (int j = 0; j<lengthOfInput;j++)
      {
        char inputChar;
        inp>>inputChar;
        //cout<<inputChar;
        task->input[j] = inputChar;
      }
      allTasks[i] = *task;
      //cout<<endl<<endl;
    }

    inp.close();
  }else cout << "Unable to open file"; 

  for (int i = 0; i < numOfTasks; ++i)
  {
    cout<<"Case #"<<i<<endl;
    cout<<" num of combinations is "<<allTasks[i].combos.combosLen<<endl;
    for (int j = 0; j < allTasks[i].combos.combosLen; ++j)
      cout<<"  +:"<< allTasks[i].combos.combosArray[j].first <<" + "<<allTasks[i].combos.combosArray[j].second <<" = "<<allTasks[i].combos.combosArray[j].third <<endl;
    cout<<" num of opposites is "<<allTasks[i].oppos.oppositeLen<<endl;
    for (int j = 0; j < allTasks[i].oppos.oppositeLen; ++j)
      cout<<"  -:"<< allTasks[i].oppos.opposArray[j].first <<" <-> "<<allTasks[i].oppos.opposArray[j].second<<endl;
    cout<<"length of input is "<<allTasks[i].inputLength<<endl;
    for (int j = 0; j<allTasks[i].inputLength;j++)
      cout<<allTasks[i].input[j];
    cout<<endl<<endl;
  }

  ofstream out;
  out.open ("output.txt");
  for (int i = 0; i< numOfTasks; ++i)
  {
    cout<<"Case #"<<(i+1)<<endl;
    out<<"Case #"<<(i+1)<<": [";
    solveCase(allTasks[i], out);
    out<<"]"<<endl;
    cout<<endl;
  }
  out.close();

  return 0;
}
