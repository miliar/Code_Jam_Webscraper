#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <stdlib.h>

using namespace std;

int main()
{
    ifstream fin("a.in");
    ofstream fout("a.out");
    
    int testcase;  
    fin >> testcase;
    
    for (int i = 0; i < testcase; i++)
    {
        string str,prevstr; bool b;
        double num, prevnum;

        fin >> str;
        
        prevnum = atoi(str.c_str());        
        
        b = next_permutation(str.begin(),str.end());
        //cout << b;
        if (b == 0)
        {
            str.insert(0,"0");
            num = atoi(str.c_str());
             while (num <= prevnum)
             {
                   next_permutation(str.begin(),str.end());
                   num = atoi(str.c_str());
             }
        }

        cout << "Case #" << i+1 << ": " << str << endl;
        fout << "Case #" << i+1 << ": " << str << endl;
     }
     //system("pause");      
     return 0;

}
