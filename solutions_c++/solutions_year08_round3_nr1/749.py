#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;
#define NUMCASES 1010
#define NUMLETT 10010
struct Case
{
    int P;
    int K;
    int L;
    vector<unsigned int> f;
    vector<unsigned int> fmap[NUMLETT];
    vector<unsigned int> keys[NUMLETT];
    int currentKey;
};

Case cases[NUMCASES];
void incKey(int n)
{
    cases[n].currentKey++;
    if(cases[n].currentKey >= cases[n].K)
        cases[n].currentKey = 0;
}
void doCase(int n,ofstream &out)
{
    sort(cases[n].f.begin(),cases[n].f.end());
    cases[n].currentKey = 0;
    unsigned int total = 0;
    for(int i = cases[n].L -1 ;i>= 0;--i)
    {
        int f = cases[n].f[i];
        vector<unsigned int> FM = cases[n].fmap[f];
        for(int j = 0;j<cases[n].fmap[f].size();j++)
        {
            
            cases[n].keys[cases[n].currentKey].push_back(FM[j]);
            total += cases[n].keys[cases[n].currentKey].size() * f;
            incKey(n);

        }    
        cases[n].fmap[f].clear();
    }
    cout << "Case #" << n+1 << ": "<< total << endl;
    out <<  "Case #" << n+1 << ": "<< total << endl;
}
int main()
{
    char buff[512];
    ifstream infile("search.txt");
    ofstream outfile("searchout.txt");
    int numCases;
    /*infile.getline(buff,256);
      numCases = atoi(buff);;*/
    infile >> numCases;
    for(int n = 0;n<numCases;n++)
    {
        /*infile.getline(buff,512);
        sscanf(buff,"%d %d %d",
               &cases[n].P,
               &cases[n].K,
               &cases[n].L);*/
        infile >> cases[n].P;
        infile >> cases[n].K;
        infile >> cases[n].L;
        for(int t = 0;t<cases[n].L;t++)
        {
            int a;
            infile >> a;
            cases[n].f.push_back(a);
            cases[n].fmap[a].push_back(t);
        }
        infile.clear();
    }
    for(int n = 0;n<numCases;n++)
    {
        doCase(n,outfile);
    }
    return 0;
}
