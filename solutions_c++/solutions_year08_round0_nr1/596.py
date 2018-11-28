#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#include <fstream>
using namespace std;

int memo[1100][110];
int steps[1100];
map<string, int> rev;
int mapcnt;

int numSteps, numEngines;

int recurse(int step, int engine)
{
    if (step == numSteps) return 0;
    if (memo[step][engine] > -1) return memo[step][engine];
    if (steps[step] != engine)
    {
       int rec = recurse(step+1, engine);
       memo[step][engine] = rec;
       return rec;
    }
     
    int min = 2000;
    for (int i = 0; i < numEngines; i++)
    {
        if (i == engine) continue;
        int result = 1 + recurse(step+1, i);
        if (result < min) min = result;
    }
    memo[step][engine] = min;
    return min;
}

int parseString(string str)
{
    if (rev.count(str) == 0)
    {
       rev.insert(make_pair(str, mapcnt));
       mapcnt++;
       return mapcnt-1;
    }
    else
        return rev[str];
}

int main()
{
    ifstream infile("happy.txt");
    int cases;
        char line[200];
    
    infile >> cases;
    infile.getline(line, 200);
            ofstream outfile("sad.txt");

    for (int i = 0; i < cases; i++)
    {
        for (int a = 0; a < 1100; a++)
        for (int b = 0; b < 110; b++)
            memo[a][b] = -1;
        rev.clear();
        mapcnt = 0;
        
        infile >> numEngines;
        infile.getline(line, 200);
        for (int j = 0; j < numEngines; j++)
        {
            infile.getline(line, 150);
            string str(line);
            parseString(str);
        }
        
        infile >> numSteps;
        infile.getline(line, 200);
        for (int j = 0; j < numSteps; j++)
        {
            infile.getline(line, 150);
            string str(line);
            steps[j] = parseString(str);
        }
        
        int min = 2000;
        for (int j = 0; j < numEngines; j++)
        {
            int result = recurse(0, j);
            if (result < min) min = result;
        }
        
        outfile << "Case #" << (i+1) << ": " << min << endl;
    }
    return 0;
}
            
        
    
