#include<iostream>
#include<string>
#include<fstream>

using namespace std;

string getState(int numSnappers, int numClicks)
{
     int onState = 1 << (numSnappers);
     if(((numClicks+1)%onState) == 0)
     {
         return "ON";
     }
     else
     {
         return "OFF";
     }
}

int main()
{
     char line = 40;
     int numTestCases=0;
     int numSnappers=0;
     int numClicks=0;
     ifstream inputFile("A-large.in");
     ofstream outputFile("A-large.out");
     inputFile >> numTestCases;
     for(int i=1;i<=numTestCases;i++)
     {
          inputFile >> numSnappers;
          inputFile >> numClicks;
          outputFile << "Case #" << i <<":  " << getState(numSnappers,numClicks) << endl;                  
     }
}
