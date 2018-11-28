#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;

long process(string data)
{
  long mark = mark = data.find(' ', 0);
  long low = atoi((data.substr(0, mark)).c_str());
  long high = atoi(data.substr(mark+1).c_str());
  cout << "low: " << low << " high: " << high << endl;
  long count = 0;
  for(long i = low; i < high; i++)
  {
    stringstream ss;
    ss << i;
    ss << i;
    for(long j = i+1; j <= high; j++)
    {
      stringstream s2;
      s2 << j;
      //cout << ss.str() << " " << s2.str() << endl;
      if ((ss.str()).find(s2.str()) != string::npos)
        count++;
    }
  }
  cout << "count: " << count << endl;
  return count;
}

int main (long argc, char **argv) {
  ifstream inputFile(argv[1]);
  cout << "process file: " << argv[1] << endl;
  string lines;
  getline(inputFile, lines);
  long numOfLines = atoi(lines.c_str());
  cout << "number of cases: " << numOfLines << endl;
  string inputData;
  ofstream output("output_p3");
  for(long i = 0; i < numOfLines; i++)
  {
    getline(inputFile, inputData);
    long result = process(inputData);
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









