/*
ID: dhxav
PROG: candy_splitting
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ofstream fout ("C-large.out");
    ifstream fin ("C-large.in");
    
    int T, N;
    int number[1000];
    int bin[1000][20];
    int buffer, temp, min, sum;
    bool counter;
    
    fin >> T;

    for (int i=0; i<T; i++)
    {
        fin >> N;
        
        for (int j=0; j<N; j++)
            fin >> number[j];
            
        for (int j=0; j<N; j++)
        {
            buffer = number[j];
            
            for (int k=0; k<20; k++)
            {
                bin[j][k] = buffer%2;
                buffer /= 2;
            }
        }
        
        counter = 0;
        sum = 0;
        min = 1000000;
        
        for (int j=0; j<20; j++)
        {
            temp = 0;
            
            for (int k=0; k<N; k++)
                temp += bin[k][j];
            
            if (temp%2==0)
               continue;
            else
            {
                counter = 1;
                break;
            }
        }
        
        fout << "Case #" << i+1 << ": ";
        
        if (counter==1)
           fout << "NO" << endl;
        else
        {
            for (int j=0; j<N; j++)
                if (min>number[j])
                   min = number[j];
               
            for (int j=0; j<N; j++)
                sum += number[j];
            
            sum -= min;
            
            fout << sum << endl;
        }
    }
    
    return 0;
}
