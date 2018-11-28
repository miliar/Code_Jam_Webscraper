#include <iostream>
#include <fstream>

using namespace std;

#define SIZE 100

struct OP
{
    char color;
    int location;
};

int abs(int a)
{
    return (a > 0)? a : -a;
}


int main()
{
  OP op[SIZE];
  ifstream fin("A-large.in");
  ofstream fout("out.txt");

  int count;

  fin >> count;


  for(int i = 0; i < count; i++)
  {
      int opCount;
      int time = 0;
      int current_locationO = 1, current_locationB = 1;
      int timeO = 0, timeB = 0;

      fin >> opCount;

      for(int j = 0; j < opCount; j++)
      {
          fin >> op[j].color >> op[j].location;
      }

      if(op[0].color == 'O')
      {
        time += (op[0].location - current_locationO) + 1;
        current_locationO = op[0].location;
        timeO = time;
      }
      else
      {
        time += (op[0].location - current_locationB) + 1;
        current_locationB = op[0].location;
        timeB = time;
      }
        //cout << time << " ";

      for(int j = 1; j < opCount; j++)
      {
          //cout << "deltaO: " << time - timeO << " deltaB: " << time - timeB << endl;
          if(op[j].color == 'O')
          {
              int delta = time - timeO;
              if(delta < abs(current_locationO - op[j].location))
              {
                  time += (abs(op[j].location - current_locationO) - delta) + 1;
              }
              else
                  time ++;
              timeO = time;
              current_locationO = op[j].location;
          }
          else
          {
              int delta = time - timeB;
              if(delta < abs(current_locationB - op[j].location))
              {
                  time += (abs(op[j].location - current_locationB) - delta) + 1;
              }
              else
                  time ++;
              timeB = time;
              current_locationB = op[j].location;
          }
      }

      fout << "Case #" << i+1 << ": " << time << endl;
  }

  return 0;
}
