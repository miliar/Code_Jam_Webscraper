#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

int process(string data)
{
  int mark = 0;
  int init = mark;
  mark = data.find(' ', init);
  int numOfDancers = atoi((data.substr(init, mark-init)).c_str());
  init = mark + 1;
  mark = data.find(' ', init);
  int numOfSurprises = atoi((data.substr(init, mark-init)).c_str());
  init = mark + 1;
  mark = data.find(' ', init);
  int p = atoi((data.substr(init, mark-init)).c_str());
  //cout << "dancer: " << numOfDancers << " surprises: " << numOfSurprises << " p: " << p << " scores:"; 
  if (mark == string::npos)
    return -1;
  if( p <= 0)
    return numOfDancers;
  int numOfGood = 0;
  int numOfPossible = 0;
  for(int i = 0; i < numOfDancers; i++)
  {
    int score;
    init = mark + 1;
    mark = data.find(' ', init);
    if (mark == string::npos)
    {
      if (i != numOfDancers - 1)
        return -1;
      else
        score = atoi((data.substr(init)).c_str());
    }
    else
    {
      score = atoi((data.substr(init, mark-init)).c_str());
    }
    cout << " " << score;
    if (score >= (3*p-2))
      numOfGood++;
    else if (score >= (3*p-4) && (3*p-4) > 0) 
      numOfPossible++;
  }
  int result;
  if (numOfPossible < numOfSurprises)
    result = numOfGood + numOfPossible;
  else
    result = numOfGood + numOfSurprises;
  cout << "\nresult: " << result << endl;
  return result;
}

int main (int argc, char **argv) {
  ifstream inputFile(argv[1]);
  cout << "process file: " << argv[1] << endl;
  string lines;
  getline(inputFile, lines);
  int numOfLines = atoi(lines.c_str());
  cout << "number of groups: " << numOfLines << endl;
  string inputData;
  ofstream output("output_p2");
  for(int i = 0; i < numOfLines; i++)
  {
    getline(inputFile, inputData);
    int result = process(inputData);
    output << "Case #";
    output << i+1;
    output << ": ";
    output << result;
    output << "\n";
  }
  inputFile.close();
  output.close();
  return 0;
}









