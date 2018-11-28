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

char pic[50][50];

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
        int rows = 0;
        int cols = 0;
        in >> rows >> cols;
        
        cout<<"solving case "<<caseN<<endl;
        out << "Case #"<<caseN+1<<":"<<endl;

        REP(r,rows)
        {
            REP(c,cols)
            {
                in >> pic[r][c];
            }
        }
        
        bool fail = false;
        REP(r,rows)
        {
            REP(c,cols)
            {
                if(pic[r][c] == '#')
                {
                    if(c+1 == cols || r+1 ==rows)
                    {
                        fail = true;
                        break;
                    }
                    if(pic[r][c+1] == '#' &&
                       pic[r+1][c+1] == '#' &&
                       pic[r+1][c] == '#')
                    {
                        pic[r][c] = pic[r+1][c+1] = '/';
                        pic[r+1][c] = pic[r][c+1] = '\\';
                    }
                    else
                    {
                        fail = true;
                        break;
                    }
                        
                }
            }
            if(fail)
                break;
        }

        if(fail)
        {
            out << "Impossible\n";
        }
        else
        { 
            REP(r,rows)
            {
                REP(c,cols)
                {
                    out << pic[r][c];
                }
                out << endl;
            }
        }
    }
    in.close();
    out.close();
    return 0;
}
