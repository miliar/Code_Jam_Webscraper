


#include <iostream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

int main(int argc, char ** argv)
{
  int num;
  string line;
  getline(cin, line);
  istringstream iss(line);
  iss >> num;
  for(int i = 1; i <= num; i++)
  {
    cout << "Case #" << i << ": "; 
    getline(cin, line);
    istringstream iss(line);
    int a, b;
    iss >> a;
    iss >> b;
    int pot = 1;
    int dig = 1;
    int count = 0;
    while(pot <= a){
      pot *= 10;
      dig++;
    }
    pot = pot/10;
    dig--;
    for(int j = a; j < b ; j++)
    {
      int trial = j;
      set<int> taken;
      for(int k=0; k < dig; k++)
      {
        int rem = trial % 10;
        trial = (rem*pot) + (trial/10);
        if(taken.count(trial) == 0 && trial > j && trial <= b)
        {
          count++;
          taken.insert(trial);
        }
      }
    }
    cout << count << endl;
  }
}

