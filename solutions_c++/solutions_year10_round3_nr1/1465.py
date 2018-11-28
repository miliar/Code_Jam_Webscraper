#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cmath>
#include <queue>
using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    fin.open("A-small-new.in");
    fout.open("A-small.out");
    
    int tcase = 0;
    int N, a[1001], b[1001];
    
    int i,j,t;
    
    fin >> tcase;
    
    for (t = 1; t <= tcase; t++)
    {
        fout << "Case #"<<t<<": ";
        fin >> N;
        int counter = 0;
        for (i = 0; i < N; i++)
        {
            fin >> a[i] >> b[i];
            
        }
        
        for (i = 0; i < N - 1; i++)
        {
            for (j = 1; j < N; j++)
            {
                if ((a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j]))
                    counter++;    
            }    
        }
        fout << counter << endl;
    }
    
    return 0;    
}
