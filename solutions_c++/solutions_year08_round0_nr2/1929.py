#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {

  int testCases, currCase = 1;
  cin >> testCases;
  while(currCase <= testCases){
    int turnTime;
    int depsA,depsB;
    int startA = 0, startB = 0;
    int trainsA = 0, trainsB = 0;
    multiset< pair<int,char> > sched;
    multiset< pair<int,char> >::iterator msi;
    
    cin >> turnTime;
    cin >> depsA >> depsB;
    for (int i = 0; i < depsA; i++){
      string timeD, timeA, temp;
      pair<int,char> tSched;
      cin >> timeD >>timeA;
      temp = timeD.substr(0,2)+timeD.substr(3,2);
      tSched.first = atoi(temp.c_str());
      tSched.second = 'X';
      sched.insert(tSched);
      
      temp = timeA.substr(0,2)+timeA.substr(3,2);
      tSched.first = atoi(temp.c_str());
      tSched.first += turnTime;
      if (tSched.first%100 >= 60)
        tSched.first += 40;
      tSched.second = 'B';
      sched.insert(tSched);
    }
    for (int i = 0; i < depsB; i++){
      string timeD, timeA, temp;
      pair<int,char> tSched;
      cin >> timeD >>timeA;
      temp = timeD.substr(0,2)+timeD.substr(3,2);
      tSched.first = atoi(temp.c_str());
      tSched.second = 'Y';
      sched.insert(tSched);
      
      temp = timeA.substr(0,2)+timeA.substr(3,2);
      tSched.first = atoi(temp.c_str());
      tSched.first += turnTime;
      if (tSched.first%100 >= 60)
        tSched.first += 40;
      tSched.second = 'A';
      sched.insert(tSched);
    }
    
    for ( msi = sched.begin(); msi != sched.end(); msi++ ){
      /*ABXY used for sorting measures. -1 & 1 would be easier to read, but more complex to program*/
      if      (msi->second == 'A') trainsA += 1;
      else if (msi->second == 'B') trainsB += 1;
      else if (msi->second == 'X'){
        if (trainsA == 0) startA += 1;
        else trainsA -= 1;
      }
      else if (msi->second == 'Y'){
        if (trainsB == 0) startB += 1;
        else trainsB -= 1;
      }
    }
    cout << "Case #" << currCase << ": " << startA << " " << startB << endl;
    currCase ++;
  }
  return 0;
}
