/*******************************************************************************
 * main -- Google Code Jam Contest Template
 *
 * Version 1.0
 *
 * 2011-2-22
 *
 * Copyright (c) 2011 Ryan Henning
 ******************************************************************************/

#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;


#define DEBUGGING false

#define doubt if (DEBUGGING) cerr

#define foo(x) doubt << #x << ": " << x << endl;
#define loopfoo(x) for (int i2 = 0; i2 < x.size(); i2++) \
                          doubt << #x << "[" << i2 << "]: " << x[i2] << endl;
#define looploopfoo(x) for (int i2 = 0; i2 < x.size(); i2++) { \
                           for (int j2 = 0; j2 < x[i2].size(); j2++) \
                               doubt << '\t' << #x << "[" << i2 << "][" \
                                     << j2 << "]: " << x[i2][j2]; \
                           doubt << endl; }

class Schedule
{
    public:

        int me;
        int N;
        vector< vector<char> > rec;
        double rpi;
        double owp;
        double oowp;

        Schedule(int N)
        {
            this->N = N;
            rec = vector< vector<char> >(N, vector<char>(N, '.'));
            rpi = 0.0;
        }

        double winprc()
        {
            double wins = 0.0;
            double total = 0.0;
            for (int i = 0; i < N; i++)
            {
                wins += (rec[me][i] == '1') ? 1 : 0;
                total += (rec[me][i] != '.') ? 1 : 0;
            }
            return wins / total;
        }

        double winprc(int no)
        {
            double wins = 0.0;
            double total = 0.0;
            for (int i = 0; i < N; i++)
            {
                if (i == no)
                    continue;
                wins += (rec[me][i] == '1') ? 1 : 0;
                total += (rec[me][i] != '.') ? 1 : 0;
            }
            return wins / total;
        }

        bool played(int other)
        {
            return rec[me][other] != '.';
        }
};

void calc(vector<Schedule>& scheds)
{
    // Calc owp.
    for (int i = 0; i < scheds.size(); i++)
    {
        double owp = 0.0;
        double total = 0.0;
        for (int j = 0; j < scheds.size(); j++)
        {
            if (!scheds[i].played(j))
                continue;
            owp += scheds[j].winprc(i);
            total += 1;
        }
        owp /= total;
        scheds[i].owp = owp;
        doubt << "  " << i << ".owp = " << scheds[i].owp << endl;
    }

    // Calc oowp.
    for (int i = 0; i < scheds.size(); i++)
    {
        double oowp = 0.0;
        double total = 0.0;
        for (int j = 0; j < scheds.size(); j++)
        {
            if (!scheds[i].played(j))
                continue;
            oowp += scheds[j].owp;
            total += 1;
        }
        oowp /= total;
        scheds[i].oowp = oowp;
    }

    // Calc rpi.
    for (int i = 0; i < scheds.size(); i++)
    {
        scheds[i].rpi = 0.25 * scheds[i].winprc() +
                        0.5  * scheds[i].owp +
                        0.25 * scheds[i].oowp;
    }
}

void run(int caseNum)
{
    int N;   // num teams;
    cin >> N;

    vector< Schedule > scheds(N, Schedule(N));

    vector< vector<char> > rec(N, vector<char>(N, '.'));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> rec[i][j];

    for (int i = 0; i < N; i++)
    {
        scheds[i].rec = rec;
        scheds[i].me = i;
    }

    calc(scheds);

    // Print answer.
    printf("Case #%d:\n", caseNum);
    for (int i = 0; i < N; i++)
        printf("%.9f\n", scheds[i].rpi);
}




int main(int argc, char** argv)
{
    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        run(caseNum);
    }
}
