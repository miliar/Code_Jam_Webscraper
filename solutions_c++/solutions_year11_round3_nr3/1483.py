/*
ID: dhxav
PROG: c
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
    ofstream fout ("C-small-attempt1.out");
    ifstream fin ("C-small-attempt1.in");
    
    int T;
    int N;
    long long int L, H;
    long long int member[10000];
    int counter, check, freq;
    
    fin >> T;

    for (int i=0; i<T; i++)
    {
        fin >> N >> L >> H;
        
        for (int j=0; j<N; j++)
            fin >> member[j];
        
        check = 0;
        
        for (int j=L; j<=H; j++)
        {      
            counter = 0;
            for (int k=0; k<N; k++)
            {
                if (j%member[k]==0 || member[k]%j==0)
                   counter++;
                else
                    break;
            }
            
            if (counter==N)
            {
               check = 1;
               freq = j;
               break;
            }
        }
        
        fout << "Case #" << i+1 << ": ";
        
        if (check==1)
           fout << freq << endl;
        else
            fout << "NO" << endl;
    }
    
    return 0;
}
