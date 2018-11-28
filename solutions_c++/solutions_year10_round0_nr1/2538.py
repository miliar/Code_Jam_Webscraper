#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    fin.open("A-large.in");
    fout.open("A-large.out");
    
    int tcase = 0;
    int n,k;
    
    fin >> tcase;
    for (int i = 1; i <= tcase; i++)
    {
        fin >> n >> k;
        fout << "Case #"<<i<<": ";
        int res = 0;
            
        res = k % (int)pow(2.0,(double)n);
      //  cout << res << endl;
        
        if (res == (int)pow(2.0,(double)n) - 1)
            fout << "ON"<<endl;
        else
            fout << "OFF" << endl;
        
    }
    
    //system("pause");
            
}
