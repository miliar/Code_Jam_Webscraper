


#include <iostream>
#include <string>
#include <sstream>

using namespace std;




int main(int argc, char ** argv)
{
  int num;
  string str;
  getline(cin, str);
  istringstream iss(str);
  iss >> num;
  for(int i = 1; i <= num; i++)
  {
    cout << "Case #" << i << ": ";
    string line;
    getline(cin, line);
    istringstream linestr(line);
    int tuples, surprise, val;
    linestr >> tuples;
    linestr >> surprise;
    linestr >> val;
    int valmin1 = val - 1;
    if(valmin1 < 0) valmin1 = 0;
    int valmin2 = val - 2;
    if(valmin2 < 0) valmin2 = 0;
    int valplus1 = val + 1;
    if(valplus1 > 10) valplus1 = 10;
    int valplus2 = val + 2;
    if(valplus2 > 10) valplus2 = 10;
    int canGetAlone = 0;
    int targetAloneMin = val + (valmin1*2);
    int targetAloneMax = val + (valplus1*2);
    int canGetWithHelp = 0;
    int targetWithHelpMin = val + (valmin2*2);
    int targetWithHelpMax = val + (valplus2*2);
    for(int j = 0; j < tuples; j++)
    {
      int score;
      linestr >> score;
      if(score >= targetAloneMin/* && score <= targetAloneMax*/)
      {
        canGetAlone++;
      }else if(/*score <= targetWithHelpMax &&*/ score >= targetWithHelpMin)
      {
        canGetWithHelp++;
      }
    }
    if(canGetWithHelp > surprise)
      canGetWithHelp = surprise;
    cout << canGetWithHelp + canGetAlone << endl;
  }
}



