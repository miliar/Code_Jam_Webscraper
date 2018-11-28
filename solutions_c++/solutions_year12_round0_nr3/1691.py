//  -*- mode: c++; coding: utf-8; c-file-style: "stroustrup"; -*-

#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits>
#include <set>

using namespace std;

int main(int narg, char **arg)
{
    int t;
    cin >> t;
    for(int it=0; it<t; it++)
    {
        cout << "Case #" << it+1 << ": ";
        int A, B;
        string strA, strB;
        cin >> strA >> strB;

        A=atoi(strA.c_str());
        B=atoi(strB.c_str());

        int power=1;
        unsigned long long count=0;
        for(unsigned rot=1; rot<strA.size(); rot++) power*=10;
        for(int i=A; i<=B; i++)
        {
            int j=i;
            for(unsigned rot=1; rot<strA.size(); rot++)
            {
                j=(j/10)+(j%10)*power;
                if(j>i && j<=B && j>=power) count++;
                else if(j==i) break;
            }
        }
        cout << count << endl;
    }
    return 0;
}
