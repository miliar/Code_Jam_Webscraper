/*
ID: dhxav
PROG: gorosort
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ofstream fout ("D-large.out");
    ifstream fin ("D-large.in");
    
    int T, N;
    int number[1000];
    int cycle[1000];
    int check[1000];
    int buffer, counter;
    int sum;
    
    fin >> T;
    
    for (int i=0; i<T; i++)
    {
        fin >> N;
        
        for (int j=0; j<N; j++)
            fin >> number[j];
            
        for (int j=0; j<N; j++)
        {
            check[j] = 0;
            cycle[j] = 0;
        }
        
        for (int j=0; j<N; j++)
        {
            if (check[j]==0)
            {
               counter = 0;
               buffer = j;
               while (check[buffer]!=1)
               {     
                     check[buffer] = 1;
                     buffer = number[buffer] - 1;
                     counter++;
               }
               cycle[counter-1]++;
            }
        }
        
        sum = 0;
        
        for (int j=1; j<N; j++)
            sum += (j+1)*cycle[j];
            
        fout << "Case #" << i+1 << ": " << sum << endl;
    }
    
    return 0;
}
