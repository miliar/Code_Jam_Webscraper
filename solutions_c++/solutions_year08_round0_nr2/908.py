#include <iostream>
#include <string>
#include <algorithm>


using namespace std;
int strToInt(string a)
{
    int ans = 0;
    
    for(int i = 0; i < a.length(); ++i)
        ans = ans*10 + (a[i] - '0');
    
    return ans;
}

int timeToMinutes(string a)
{
    return strToInt(a.substr(0, 2))*60 + strToInt(a.substr(3, 2));
}

int N;
int T;

int NA;
int NB;

int timesLeavingA[1000];
int timesArrivingB[1000];

int timesLeavingB[1000];
int timesArrivingA[1000];

int main()
{
    cin >> N;
    
    for(int i = 1; i <= N; ++i)
    {
        cin >> T;
        
        cin >> NA >> NB;
        
        for(int j = 0; j < NA; ++j)
        {
            string temp;
            
            cin >> temp;
            timesLeavingA[j] = timeToMinutes(temp);
            
            //cout << "TLA: " << temp << " " << timeToMinutes(temp) << endl;
            
            cin >> temp;
            timesArrivingB[j] = timeToMinutes(temp) + T;
            
            //cout << "TAB: " << temp << " " << timeToMinutes(temp) << endl;
        }
        
        for(int j = 0; j < NB; ++j)
        {
            string temp;
            
            cin >> temp;
            timesLeavingB[j] = timeToMinutes(temp);
            
            //cout << "TLB: " << temp << " " << timeToMinutes(temp) << endl;
            
            cin >> temp;
            timesArrivingA[j] = timeToMinutes(temp) + T;
            
            //cout << "TAA: " << temp << " " << timeToMinutes(temp) << endl;
        }
        
        sort(timesLeavingA, timesLeavingA+NA);
        sort(timesArrivingB, timesArrivingB+NA);
        
        sort(timesLeavingB, timesLeavingB+NB);
        sort(timesArrivingA, timesArrivingA+NB);
        
        int ansA = 0;
        int ansB = 0;
        
        int trainsAtA = 0;
        int trainsAtB = 0;
        
        int cLA = 0;
        int cLB = 0;
        int cAA = 0;
        int cAB = 0;
        
        while((cLA < NA) || (cLB < NB) || (cAB < NA) || (cAA < NB))
        {
            //cout << cLA << "/" << NA << " " << cLB << "/" << NB << " " << cAB << "/" << NA << " " << cAA << "/" << NB << " " << ansA << " " << ansB << endl;;
            
            int eTime = 999999;
            
            if((cAB < NA) && (timesArrivingB[cAB] < eTime))
                eTime = timesArrivingB[cAB];
            
            if((cAA < NB) && (timesArrivingA[cAA] < eTime))
                eTime = timesArrivingA[cAA];
            
            if((cLA < NA) && (timesLeavingA[cLA] < eTime))
                eTime = timesLeavingA[cLA];
            
            if((cLB < NB) && (timesLeavingB[cLB] < eTime))
                eTime = timesLeavingB[cLB];
            
            //cout << eTime << " " << timesArrivingB[cAB] << " " << timesArrivingA[cAA] << " " << timesLeavingA[cLA] << " " << timesLeavingB[cLB] << endl;
            
            if(eTime == timesArrivingB[cAB])
            {
                //cout << "Train arrives at B" << endl;
                ++trainsAtB;
                ++cAB;
                continue;
            }
            
            if(eTime == timesArrivingA[cAA])
            {
                //cout << "Train arrives at A" << endl;
                ++trainsAtA;
                ++cAA;
                continue;
            }
            
            if(eTime == timesLeavingA[cLA])
            {
                if(trainsAtA == 0)
                {
                    //cout << "Creating train arrives at A" << endl;
                    ++ansA;
                }
                else
                {
                    //cout << "Train leaving A" << endl;
                    --trainsAtA;
                }
                ++cLA;
                continue;
            }
            
            if(eTime == timesLeavingB[cLB])
            {
                if(trainsAtB == 0)
                {
                    //cout << "Creating train arrives at B" << endl;
                    ++ansB;
                }
                else
                {
                    //cout << "Train leaving B" << endl;
                    --trainsAtB;
                }
                ++cLB;
                continue;
            }
        }
         
        cout << "Case #" << i <<  ": " << ansA << " " << ansB << endl;
    }
}

