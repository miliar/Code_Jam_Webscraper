#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

struct Case
{
    int numE;
    map<string,int> engines;
    int numQ;
    int queries[1050];
};
#define NUMCASES 60
Case cases[NUMCASES];

int tryWork(int n,int start)
{
    if(start >= cases[n].numQ) return 1;
    int E[101];
    memset(E,-1,sizeof(E));
    int numHit = 0;
    for(int place = start;place <cases[n].numQ;place++)
    {
        if(E[cases[n].queries[place]] == -1)
        {
            E[cases[n].queries[place]] = place;
            numHit++;
        }
    }
    if(numHit != cases[n].numE)
        return 0;
    //otherwise go back and retry all the others
    int mini = cases[n].numQ;
    for(int eng = 0;eng < cases[n].numE;eng++)
    {
        int ret = tryWork(n,E[eng]+1);
        if(ret < mini)
            mini = ret;
    }
    return mini+1;
}
int findFurthest(int n,int pos,int current)
{
    int E[101];
    int numHit = 0;
    memset(E,-1,sizeof(E));

    for(int p = pos;p<cases[n].numQ;p++)
    {
        if(E[cases[n].queries[p]] == -1)
        {
            numHit++;
            E[cases[n].queries[p]] = p;
        }
        if(numHit == (cases[n].numE -1))
        {
            break;
        }
    }
    for(int a = 0;a<cases[n].numE;a++)
    {
        if(E[a] == -1)
        {
            return a;
        }
    }
    cout << "BAD BAD!" << endl;
}
void doCase(int n,ofstream &out)
{
    int cPos = 0;
    int current = findFurthest(n,0,-1);
    int switches = 0;
    while(cPos < cases[n].numQ)
    {

        if(cases[n].queries[cPos] == current)
        {
            current = findFurthest(n,cPos,current);
            switches++;
        }
        cPos++;
    }
    cout << "Case #" << n+1 << ": "<< switches << endl;
    out <<  "Case #" << n+1 << ": "<< switches << endl;
}
int main()
{
    char buff[256];
    ifstream infile("search.txt");
    ofstream outfile("searchout.txt");
    int numCases;
    infile.getline(buff,256);
    numCases = atoi(buff);;
    for(int n = 0;n<numCases;n++)
    {
        infile.getline(buff,256);
        cases[n].numE = atoi(buff);

        for(int t = 0;t<cases[n].numE;t++)
        {
            infile.getline(buff,256);
            string e(buff);
            cases[n].engines[e] = t;  
        }
        infile.getline(buff,256);
        cases[n].numQ = atoi(buff);
        for(int t = 0;t<cases[n].numQ;t++)
        {
            infile.getline(buff,256);
            string e(buff);
            cases[n].queries[t] = cases[n].engines[e];            
        }
    }
    for(int n = 0;n<numCases;n++)
    {
        doCase(n,outfile);
    }

    return 0;
}
