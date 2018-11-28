#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

void sort(int *a, int L)
{
    int max, maxP, t;
    for (int i = 0; i < L; i++)
    {
        max = a[i]; maxP = i;
        for ( int j = i+1; j<L; j++)
        {
            if (max < a[j])
            {
                max = a[j];
                maxP = j;
            }
        }
        t = a[maxP];  a[maxP] = a[i]; a[i] = t;
    }
}

void main()
{
    ifstream fin;
    fin.open("a.txt");
    int N,P,K,L,j;
    int a[1000];
    fin>>N;
    for (int i = 0; i < N ; i++)
    {
        cout<<"Case #"<<i+1<<": ";
        fin>>P>>K>>L;
        for (j = 0; j < L; j++)
        {
            fin>>a[j];
        }
        sort(a, L);
        int sum = 0;
        int factor = 0;
        for (j = 0;j<L;j++)
        {
            if (j % K == 0)
                factor++;
            sum += factor * a[j];
        }
        cout<<sum<<'\n';
    }
    fin.close();
}
