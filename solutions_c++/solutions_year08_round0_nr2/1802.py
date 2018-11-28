#include<iostream>
#include<fstream>
#include<cstdlib>
#include<string>
#include<algorithm>
using namespace std;

int Case,NA,NB,result;

struct timeTable
{
    int time;
    char type;
    char station;
};

bool compare(timeTable a, timeTable b)
{
    if(a.time<b.time)
        return true;
    else if(a.time==b.time)
    {
        if(a.type=='D'&&b.type=='A')
            return false;
        else if(a.type=='A'&&b.type=='D')
            return true;
        else
            return true;
    }
    else
        return false;    
}


int main()
{
    ifstream FIN("input.txt");
    ofstream FOUT("output.txt");
    
    timeTable t[500];
    int train[2];
    int start[2];
    int delay;
    
    FIN >> Case;
//    cout << Case << endl;
    for(int caseNumber=1;caseNumber<=Case;caseNumber++)
    {
        train[0] = 0;
        train[1] = 0;
        start[0] = 0;
        start[1] = 0;
        FIN >> delay;
        FIN >> NA;
        FIN >> NB;
        cout << NA << " " << NB << endl;
        string tmp;
        int i=0;
        for(i=0;i<NA;i++)
        {
            FIN >> tmp; // startTime;
            int time = ((tmp[0]-'0')*10+(tmp[1]-'0'))*60+(tmp[3]-'0')*10+(tmp[4]-'0');
            t[2*i].time = time;
            t[2*i].station = 'A';
            t[2*i].type = 'D'; //depart
            FIN >> tmp; // ArriveTime;
            time = ((tmp[0]-'0')*10+(tmp[1]-'0'))*60+(tmp[3]-'0')*10+(tmp[4]-'0') + delay;
            t[2*i+1].time = time;
            t[2*i+1].station = 'B';
            t[2*i+1].type = 'A'; //arrive           
        }
        for(;i<NA+NB;i++)
        {
            FIN >> tmp; // startTime;
            int time = ((tmp[0]-'0')*10+(tmp[1]-'0'))*60+(tmp[3]-'0')*10+(tmp[4]-'0');
            t[2*i].time = time;
            t[2*i].station = 'B';
            t[2*i].type = 'D'; //depart
            FIN >> tmp; // ArriveTime;
            time = ((tmp[0]-'0')*10+(tmp[1]-'0'))*60+(tmp[3]-'0')*10+(tmp[4]-'0') + delay;
            t[2*i+1].time = time;
            t[2*i+1].station = 'A';
            t[2*i+1].type = 'A'; //arrive           
        }        
        sort(t,t+2*(NA+NB),compare);
        for(i=0;i<2*(NA+NB);i++)
        {
            cout << t[i].time << " " << t[i].type << " " << t[i].station << endl;
            if(t[i].type == 'A')
            {
                train[t[i].station-'A']++;
            }
            else // 'D'
            {
                 if(train[t[i].station-'A']>0)
                     train[t[i].station-'A']--;
                 else
                     start[t[i].station-'A']++;
            }
        }


        cout << "Case #" << caseNumber << ": " << start[0] << " " << start[1] << endl;
        FOUT << "Case #" << caseNumber << ": " << start[0] << " " << start[1] << endl;      
    
    }
    cin >> NA;
}
