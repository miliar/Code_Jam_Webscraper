#include <algorithm>  
#include <iostream>  
#include <iomanip>  
#include <fstream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v)) 

char mat[100][100];
double WP[100];
double OWP[100];

double calculateWP(int team,int teams);
double calculateOWP(int opp,int team, int teams);
double calculateOOWP(int team, int totalTeams);

int main(int argc, char** argv)
{
    ifstream in;
    in.open(argv[1],ios::in);
    ofstream out;
    out.open(argv[2],ios::out);
    int N = 0;
    in>>N;
    cout << " Total  " << N <<endl;
    REP(caseN,N)
    {
        int teams = 0;
        in >> teams;
        
        cout<<"solving case "<<caseN<<endl;
        out << "Case #"<<caseN+1<<":\n";
        REP(i,teams)
            REP(j, teams)
            {
                in >> mat[i][j];
            }

        REP(i,teams)
        {
            WP[i] = calculateWP(i,teams);

            double owp = 0;
            int oppCount = 0;
            REP(j,teams)
            {
                if(mat[i][j] != '.')
                {
                    owp += calculateOWP(j,i,teams);
                    ++oppCount;
                }
            }
             
            owp/=oppCount;
            OWP[i] = owp;
        }

        REP(i,teams)
        {
            out<< setprecision(12)<< (0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * calculateOOWP(i,teams))<<"\n"; 
            
        }
        
    }
    in.close();
    out.close();
    return 0;
}

double calculateWP(int team,int teams)
{
    int wins=0,los=0;
    REP(i,teams)
    {
        if(mat[team][i] == '1')
            ++wins;
        else if(mat[team][i] == '0')
            ++los;
    }
    return ((double)wins/(wins + los));
}

double calculateOWP(int opp,int team,int teams)
{
    int wins=0,los=0;
    REP(i,teams)
    {
        if(i==team)
            continue;
        
        if(mat[opp][i] == '1')
            ++wins;
        else if(mat[opp][i] == '0')
            ++los;
    }
    return ((double)wins/(wins + los));
}

double calculateOOWP(int team, int totalTeams)
{
    double av = 0;
    int oppC = 0;
    REP(i,totalTeams)
    {
        if(mat[team][i] == '.')
            continue;
        av+= OWP[i];
        ++oppC;
    }
    av/=oppC;
    return av;
}
