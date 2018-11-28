#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <iomanip>
using namespace std;

vector<vector<double> > probs;
vector<double> ok;
int total;

void recurse(double prob, int index)
{
     if (index == total)
     {
        ok.push_back(prob);
        return;
     }
    for (int i = 0; i < 4; i++)
    {
        double np = prob * probs[index][i];
            recurse(np, index+1);
            
    }
}

int main()
{
    ifstream in("happy.txt");
    ofstream out("sad.txt");
    int cases;
    in >> cases;
    
    for (int c = 0; c < cases; c++)
    {
        int tries;
        in >> tries >> total;
        
        probs = vector<vector<double> >(total);
        ok = vector<double>();
        
        for (int i = 0; i < total; i++)
        for (int j = 0; j < 4; j++)
        {
            double d;
            in >> d;
            probs[i].push_back(d);
        }
        
        recurse(1, 0);
        double t = 0;
        sort(ok.begin(), ok.end());
        for (int i = 0; (i < tries && i < ok.size()); i++)
        {
            t += ok[ok.size() - 1 - i];
        }
            
        out << "Case #" << (c+1) << setprecision(10) <<  ": " << t << endl;
    }
    return 0;
}
    
