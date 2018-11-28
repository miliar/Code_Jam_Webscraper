#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
using namespace std;

typedef struct _ride
{
       int start;
       int end;
       char dest;
       bool startsAtA;
} ride;

int getTime(string str)
{
    int hours = atoi(str.substr(0,2).c_str());
    int min = atoi(str.substr(3).c_str());
    return hours * 60 + min;
}

ride schedule[200];
int numRides;

void sortMe()
{
     for (int i = 0; i < numRides; i++)
     for (int j = i+1; j < numRides; j++)
     {
         if (schedule[i].start > schedule[j].start)
         {
            ride temp = schedule[i];
            schedule[i] = schedule[j];
            schedule[j] = temp;
         }
     }
}

int totalA, totalB;
int arrival[200];
bool destA[200];

int getNextTrain(int index)
{
     int start = schedule[index].start;
     for (int i = 0; i < (totalA + totalB); i++)
     {
         if (arrival[i] > start) continue;
         if (destA[i] != schedule[index].startsAtA) continue;
         return i;
     }
     return -1;
}
                 
void calculate()
{
     for (int i = 0; i < numRides; i++)
     {
         ride theRide = schedule[i];
         int nextTrain = getNextTrain(i);
         if (nextTrain >= 0)
         {
            arrival[nextTrain] = theRide.end;
            destA[nextTrain] = !destA[nextTrain];
         }
         else
         {
             int total = totalA + totalB;
             arrival[total] = theRide.end;
             destA[total] = !theRide.startsAtA;
             if (theRide.startsAtA) totalA++; else totalB++;
         }
     }
}

int main()
{
    int cases;
    int turn;
    ifstream infile("happy.txt");
    ofstream outfile("sad.txt");
    infile >> cases;
    for (int c = 0; c < cases; c++)
    {
        infile >> turn;
        int numa, numb;
        infile >> numa >> numb;
        numRides = numa + numb;
        totalA = 0;
        totalB = 0;
        for (int i = 0; i < numRides; i++)
        {
            string str1, str2;
            infile >> str1 >> str2;
            ride r;
            r.start = getTime(str1);
            r.end = getTime(str2) + turn;
            if (i < numa) r.startsAtA = true; else r.startsAtA = false;
            schedule[i] = r;
        }
        
        sortMe();
        calculate();
        
        outfile << "Case #" << (c+1) << ": " << totalA << " " << totalB << endl;
    }
    system("PAUSE");
    return 0;
}
