#include <iostream>
#include <queue>
#include <fstream>

using namespace std;


void emptyQueue(queue<int> &queue0)
{
  while(!queue0.empty())
    queue0.pop();
}

int main(int argc, char *argv[])
{
  queue<int> queue_in, queue_out;
  int test_case;
  int R, N;
  int car_size, car_board;
  int counter, temp, total, queue_size;
  int i;
  int total_cases;

  ifstream input("C-small-attempt1.in");
  ofstream output("output.txt");

  if ((!input) || (!output))
  {
    cerr << "error opening file(s)";
    exit(1);
  }

  test_case = R = N = counter = total = 0;
  car_size = car_board = 0;

  input >> total_cases;
  while(counter != total_cases)
  {
    input >> R >> car_size >> queue_size;
    for (i = 0; i < queue_size; i++)
    {
      input >> temp;
      queue_in.push(temp);
    }

    counter++;
    total = 0;
    for(i = 0; i < R; i++)
    {
      while((queue_in.front() + car_board <= car_size) && (!queue_in.empty()))
      {
        temp = queue_in.front();
        queue_in.pop();
        queue_out.push(temp);
        car_board += temp;
      }

      total += car_board;
      car_board = 0;

      while(!queue_out.empty())
      {
        queue_in.push(queue_out.front());
        queue_out.pop();
      }
    }
    emptyQueue(queue_in);
    emptyQueue(queue_out);

    output << "Case #" << counter << ": " << total << endl;

  }

  input.close();
  output.close();

  return 0;
}
