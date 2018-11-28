#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{
//    fstream cin("sample.in");
    int n;
    cin >> n;
    for(int i=1; i<=n; i++)
    {
        int t;    //minutes
        int na,nb;
        cin >> t >> na >> nb;
        //A station
        vector<int> startA, stopA, startB, stopB;
        while(na--)
        {
            int hour,min;
            char camma;
            cin >> hour >> camma >> min;
            startA.push_back(hour*60 + min); //saved min
            cin >> hour >> camma >> min;
            stopB.push_back(hour*60 + min + t); //saved min
        }
        //start B station;
        while(nb--)
        {
            int hour,min;
            char camma;
            cin >> hour >> camma >> min;
            startB.push_back(hour*60 + min); //saved min
            cin >> hour >> camma >> min;
            stopA.push_back(hour*60 + min + t); //saved min
        }
        //slove
        sort(startA.begin(), startA.end());
        sort(startB.begin(), startB.end());
        sort(stopA.begin(), stopA.end());
        sort(stopB.begin(), stopB.end());
        for(vector<int>::iterator it = stopA.begin(); it != stopA.end(); it++)
        {
            vector<int>::iterator removeIt = lower_bound(startA.begin(), startA.end(), *it);
            if(removeIt != startA.end())
            {
                startA.erase(removeIt);
            }
        }
        for(vector<int>::iterator it = stopB.begin(); it != stopB.end(); it++)
        {
            vector<int>::iterator removeIt = lower_bound(startB.begin(), startB.end(), *it);
            if(removeIt != startB.end())
            {
                startB.erase(removeIt);
            }
        }
        //output
        string Case = "Case #";
        cout << Case << i << ": " << startA.size() << " " << startB.size() << endl;
    }
    return 0;
}