#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
struct Task
{
  vector<int> input;
};

int solveCase(Task task, ofstream& out)
{
  int toReturn = -1;
  vector<int> v = task.input;
  for (int i = 1; i < (1 << v.size()); ++i) {
    vector<int> left, right;
    for (int j = 0; j < v.size(); ++j) {
      if ((i >> j) & 1)
        left.push_back(v[j]);
      else
        right.push_back(v[j]);
    }

    if (left.size() == 0 || right.size() == 0) continue;

    int xorOfLeft = 0;
    for (int k = 0; k < left.size(); k++) xorOfLeft ^= left[k];
    
    int xorOfRight = 0;
    for (int k = 0; k < right.size(); k++) xorOfRight ^= right[k];

    //cout<<"Left: ";
    //for (int k = 0; k < left.size(); k++) cout << left[k] <<" ";
    //cout<<endl<<"Right: ";
    //for (int k = 0; k < right.size(); k++) cout << right[k] <<" ";
    //cout<<endl;
    //cout<<"Sum of Left = " << xorOfLeft << " right = " << xorOfRight << endl;
    if (xorOfLeft == xorOfRight)
    {
      int sumOfLeft = 0;
      for (int k = 0; k < left.size(); k++) sumOfLeft += left[k];

      int sumOfRight = 0;
      for (int k = 0; k < right.size(); k++) sumOfRight += right[k];

      int maxOfLeftAndRight = max(sumOfRight, sumOfLeft);
      if (maxOfLeftAndRight > toReturn) 
      {
          toReturn = maxOfLeftAndRight;
          
          cout<<"Left: ";
          for (int k = 0; k < left.size(); k++) cout << left[k] <<" ";
          cout<<endl<<"Right: ";
          for (int k = 0; k < right.size(); k++) cout << right[k] <<" ";
          cout<<endl;
          cout<<"XOR of Left = " << xorOfLeft << " right = " << xorOfRight << endl;
      }
    }
  }

  if (toReturn > -1) 
  {
    out << toReturn;
    return toReturn;
  }
  out << "NO";
  return -1;
}

int main ()
{
  Task* allTasks;
  int numOfTasks;
  ifstream inp ("input.txt");
  if (inp.is_open())
  {
    inp >> numOfTasks;
    cout<<"num of cases is "<<numOfTasks<<endl;
    allTasks = new Task[numOfTasks];
    for (int i = 0; i < numOfTasks; ++i)
    {
      Task* task = new Task;
      //cout<<"Case #"<<i<<endl;
      int lengthOfTask;
      inp>>lengthOfTask;
      //cout<<"length of task is "<<lengthOfTask<<endl;
      task->input.resize(lengthOfTask);
      for (int j = 0; j < lengthOfTask; ++j)
      {
        int val;
        inp >> val;
        //cout<<"  "<<j<<" : "<< val<<endl;
        task->input[j] = val;
      }
      //cout<<endl<<endl;
      allTasks[i] = *task;
    }
    inp.close();
  }else cout << "Unable to open file"; 

  for (int i = 0; i < numOfTasks; ++i)
  {
    //cout<<"Case #"<<i<<endl;
    //cout<<" num of numbers is "<<allTasks[i].input.size()<<endl;
    //for (int j = 0; j < allTasks[i].input.size(); ++j)      cout<<"  "<<j<<" : "<< allTasks[i].input[j]<<endl;
    //cout<<endl<<endl;
  }

  ofstream out;
  out.open ("output.txt");
  for (int i = 0; i < numOfTasks; ++i)
  {
    //cout<<"Case #"<<(i+1)<<endl;
    out<<"Case #"<<(i+1)<<": ";
    solveCase(allTasks[i], out);
    out<<endl;
  }
  out.close();

  return 0;
}
