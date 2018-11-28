// CodeJam.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>

using namespace std;

int main()
{
  string line;
  fstream myfile ("B-large.in");
  ofstream outFile;
  outFile.open("B-large.out");

  int cases;
  myfile>>cases;
  for( int i = 0; i < cases; i++ )
  {
  outFile<<"Case #"<<i+1<<": ";
  cout<<"Case #"<<i+1<<": ";

  // Read input.
  int num_googlers;
  int surprise;
  int target;

  myfile >> num_googlers;
  myfile >> surprise;
  myfile >> target;

  int total_score[num_googlers];
  int high_score[num_googlers];
  int awesome = 0;
  for (int g = 0; g < num_googlers; ++g) {
    myfile >> total_score[g];
    high_score[g] = total_score[g] / 3;
    if (total_score[g] % 3)
      ++high_score[g];
    if (high_score[g] >= target) {
      ++awesome;
    } else if (surprise > 0 &&
               ((total_score[g] % 3) != 1) &&
               (total_score[g] > 1) &&
               (high_score[g] + 1) == target) {
        ++awesome;
        --surprise;
    }
  }
  // Write output.
  outFile<<awesome<<endl;
  cout<<awesome<<endl;
}

myfile.close();
outFile.close();
return 0;
}



