#include <iostream>
#include <fstream>
using namespace std;
struct Trip
{
    int startTime;
    int endTime;
};

struct Case
{
    int turnAround;
    int na;
    int nb;
    int depA[1500];
    int depB[1500];
    int arrA[1500];
    int arrB[1500];
};
Case cases[105];
int timeToMin(int h,int m)
{
    return h*60 + m;
}
void doCase(int n)
{
    int newTA = 0;
    int newTB = 0;
    int TA = 0,TB =0;
    for(int time = 0;time < 1440;time++)
    {
        while(cases[n].depA[time])
        {
            if(TA)
                TA--;
            else
            
                if((cases[n].arrA[time]))
                {
                    (cases[n].arrA[time])--;
                }
                else
                {
                    newTA++;
                }
            
            cases[n].depA[time]--;
        }
        while(cases[n].depB[time])
        {

            if(TB)
                TB--;
            else
                if((cases[n].arrB[time]))
                {
                    (cases[n].arrB[time])--;
                }
            else
            {
                newTB++;
            }
            cases[n].depB[time]--;
        }
        TB+= (cases[n].arrB[time]);
        TA+= (cases[n].arrA[time]);
    }
    cout << "Case #" << n+1 << ": " << newTA << " " << newTB << endl;
}
int main()
{
    memset(cases,0,sizeof(cases));
    ifstream infile("train.txt");
    int numCases;
    infile >> numCases;
    for(int n = 0;n<numCases;n++)
    {
        infile >> cases[n].turnAround;
        infile >> cases[n].na;
        infile >> cases[n].nb;
        for(int t = 0;t<cases[n].na;t++)
        {
            int h;
            int m;
            char t;
            infile >> h;
            infile >> t;
            infile >> m;
            cases[n].depA[timeToMin(h,m)]++;
            infile >> h;
            infile >> t;
            infile >> m;
            cases[n].arrB[cases[n].turnAround+timeToMin(h,m)]++;
        }
        for(int t = 0;t<cases[n].nb;t++)
        {
            int h;
            int m;
            char t;
            infile >> h;
            infile >> t;
            infile >> m;
            cases[n].depB[timeToMin(h,m)]++;
            infile >> h;
            infile >> t;
            infile >> m;
            cases[n].arrA[cases[n].turnAround+timeToMin(h,m)]++;
        }
    }
    for(int n = 0;n<numCases;n++)
    {
        doCase(n);
    }

    return 0;
}
