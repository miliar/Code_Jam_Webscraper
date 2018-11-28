#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<fstream>
using namespace std;
int A[1200];
int B[1200];
int main()
{
    ifstream fin("A-large.IN");
    ofstream fout("output.txt");
    int T,N;
    fin>>T;
    for(int i = 1; i <= T; i++)
    {
        fin>>N;
        int count = 0;
        for(int j = 1; j <= N; j++)
            fin>>A[j]>>B[j];
        for(int m = 1;m <= N; m++)
            for(int n = m+1; n <= N; n++)
            {
                if((A[m] < A[n] && B[m] > B[n]) || (A[m] > A[n] && B[m] < B[n]))
                    count++;
            }
        fout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}
