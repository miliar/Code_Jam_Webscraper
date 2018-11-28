// Google CodeJam 2009 contest qualification round, problem 3: Welcome to code jam
// Author: ..zGr..
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    int caseno;
    ifstream inp;
    inp.open("C-small-attempt0.in");
    ofstream op;
    op.open("C-small_op.txt");
    string welcome="welcome to code jam";
    inp >> caseno;
    inp.ignore(1,'\n');
    for (int i=0;i<caseno;i++)
    {
        string line;
        getline(inp,line);
        int result=0,j=0,k=0,control=17,control_points[19];
        while(k>-1)
        {
            if (line[j]==welcome[k]) { k++; control_points[k]=j; if (k==control) { control_points[k]=j; control--; } }
            j++;
            if (k==19) { result++; k--; }
            if (result>10000) result-=10000;
            if (line[j]=='\0') { j=control_points[k]+1; k--; }
        }
        op << "Case #" << (i+1) << ": ";
        if (result<1000) op << "0";
        if (result<100) op << "0";
        if (result<10) op << "0";
        op << result << endl;
    }
    inp.close();
    op.close();
    return 0;
}