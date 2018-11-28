// Author: ..zGr..
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    int L,D,N;
    ifstream inp;
    inp.open("A-large.in");
    ofstream op;
    op.open("A-large_op.txt");
    inp >> L >> D >> N;
    string * words,cases;
    words=new string [D];
    for (int i=0;i<D;i++)
    {
        inp >> words[i];
    }
    for (int i=0;i<N;i++)
    {
        inp >> cases;
        int n=0,t=0,result=0; 
        string * str=new string [L];
        char a;
        while (cases[n]!='\0')
        {
            if (cases[n]=='(')
            {
                n++;
                while (cases[n]!=')') { str[t]+=cases[n]; n++; }
            }
            else str[t]+=cases[n];
            n++;
            t++;
        }
        n=0;
        t=0;
        for (int j=0;j<D;j++)
        {
            for (int k=0;k<L;k++)
            {
                while (str[k][n]!='\0') { if (str[k][n]==words[j][k]) t++; n++;  }            
                n=0;
            }
            if (t==L) result++;
            t=0;
        }
        op << "Case #" << (i+1) << ": " << result << endl;
    }
    inp.close();
    op.close();
    return 0;
}
            
                