#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("A-large.IN");
    ofstream fout("output.txt");
    int T;
    fin>>T;
    for(int i = 1; i <= T;i++)
    {
        int N,K;
        fin>>N>>K;
        int start = 1;
        for(int j = 1; j <= N;j++)
            start*=2;
        start--;
        int ON = 0;
        while(K >= start)
        {
           if(K == start)
           {
                ON = 1;
                break;
           }
           else
               K-=start + 1;
        }
        fout<<"Case #"<<i<<": ";
        if(ON)
            fout<<"ON"<<endl;
        else
            fout<<"OFF"<<endl;
    }   
    system("pause");
    return 0;
}
