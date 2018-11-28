#include <iostream>
#include <string>
#include <vector>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

//*
#include <fstream>
fstream fin ("A-large.in",ios::in);
fstream fout ("output.txt", ios::out);
#define cin fin
#define cout fout
//*/

struct step
{
    char color;
    int pos;
    int cost;
};

int max(int num1, int num2)
{
    return num1 > num2 ? num1 : num2;
}

int FindBestToNext(int curPos, int nextPos)
{
    return abs(nextPos - curPos) + 1;
}

int FindBestMethod(vector<step> steps)
{
    vector<int> Oprocess;
    vector<int> Bprocess;

    for(int i=0; i<steps.size(); i++)
        if(steps.at(i).color == 'O')
            Oprocess.push_back(steps.at(i).pos);
        else
            Bprocess.push_back(steps.at(i).pos);

   //cout <<"Bprocess[0]:" << Bprocess.at(0) << endl;

    int* Bcost = new int[Bprocess.size()];
    if(Bprocess.size() >= 1)
        Bcost[0] = FindBestToNext(1, Bprocess[0]);
    for(int i=1; i<Bprocess.size(); i++)
    {
        Bcost[i] = FindBestToNext(Bprocess.at(i-1),Bprocess.at(i));
    }


    int* Ocost = new int[Oprocess.size()];
    if(Oprocess.size() >= 1)
        Ocost[0] = FindBestToNext(1, Oprocess[0]);
    for(int i=1; i<Oprocess.size(); i++)
    {
        Ocost[i] = FindBestToNext(Oprocess.at(i-1),Oprocess.at(i));
    }

    int curCostB = 0, curCostO = 0;
    int curNumB = 0, curNumO = 0;
    if(steps.size() >= 1)
    {
        if(steps.at(0).color == 'O')
        {
            steps.at(0).cost = Ocost[0];
            curCostO = Ocost[0];
            curNumO++;
        }
        else
        {
            steps.at(0).cost = Bcost[0];
            curCostB = Bcost[0];
            curNumB++;
        }
    }

    //cout <<"Bcost 0 "<<Bcost[0]<<endl;

    for(int i=1; i<steps.size(); i++)
    {
        if(steps.at(i).color == 'O')
        {
            int lastCost = steps.at(i-1).cost;

            steps.at(i).cost = max(curCostO + Ocost[curNumO], lastCost+1);
            curCostO = steps.at(i).cost;

            curNumO++;
        }

        else
        {
            int lastCost = steps.at(i-1).cost;

            steps.at(i).cost = max(curCostB + Bcost[curNumB], lastCost+1);
            curCostB = steps.at(i).cost;
            curNumB++;
        }
        //cout <<"step" <<i<< ":" << steps.at(i).cost <<endl;
    }
    int totalCost;
    if(steps.size() >= 1)
        totalCost =  steps.at(steps.size()-1).cost ;
    // TODO¡¡else
    else
        totalCost = steps.at(0).pos+1;

    return totalCost;
}



int main()
{
    int datanum;
    fin >> datanum;


    for(int i=0; i<datanum; i++)
    {
        vector<step> vecSteps;


        int stepNum;
        cin >> stepNum;
        for(int j=0; j<stepNum; j++)
        {
            char color;
            int number;
            cin >> color;
            cin >> number;
            step curStep;
            curStep.color = color;
            curStep.pos = number;
            vecSteps.push_back(curStep);
        }

        int cost = FindBestMethod(vecSteps);
        cout << "Case #"<<i+1<<": "<<cost<<endl;
    }

    fin.close();

    return 0;
}



