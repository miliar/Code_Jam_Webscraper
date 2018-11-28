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
        int n_googlers, n_surprise, min_score, count=0;
        cin >> n_googlers >> n_surprise >> min_score;
        for(int i=0; i<n_googlers; i++)
        {
            int sum;
            cin >> sum;
            sum-=min_score;
            if(sum<0) continue;
            if(sum>=(min_score-1)*2) count++;
            else if(n_surprise && sum>=(min_score-2)*2) { count++; n_surprise--; }
        }
        cout << count << endl;
    }

    return 0;
}
