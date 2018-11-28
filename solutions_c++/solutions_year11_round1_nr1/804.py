/*
ID: dhxav
PROG: FreeCell Statistics
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    
    int T, Pd, Pg;
    long long int N;
    
    fin >> T;

    for (int i=0; i<T; i++)
    {
        fin >> N >> Pd >> Pg;
        
        fout << "Case #" << i+1 << ": ";
        
        if ((Pd<100 && Pg==100) || (Pd>0 && Pg==0))
        {
           fout << "Broken" << endl;
           continue;
        }
        
        if ((N>=100) || (Pd==100) || (Pd%2==0 && 50<=N) || (Pd%4==0 && 25<=N) || (Pd%5==0 && 20<=N) || (Pd%10==0 && 10<=N) || (Pd%20==0 && 5<=N) || (Pd%25==0 && 4<=N) || (Pd%50==0 && 2<=N))
           fout << "Possible" << endl;
        else
            fout << "Broken" << endl;
    }
    
    return 0;
}
