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
#include <queue>

using namespace std;

struct Vine
{
    int dist, length;
    int best_length;
};

int main(int narg, char **arg)
{
    int t;
    cin >> t;
    cout.precision(10);
    for(int it=0; it<t; it++)
    {
        cout << "Case #" << it+1 << ": ";
        int n_vine;
        cin >> n_vine;
        vector<Vine> vines(n_vine);
        for(int i=0; i<n_vine; i++) { cin >> vines[i].dist >> vines[i].length; vines[i].best_length=-1; }
        int total;
        cin >> total;

        //printf("\n"); for(int i=0; i<n_vine; i++) printf("%3d %4d %4d\n", i, vines[i].dist, vines[i].length); printf("%d!!\n", total);

        bool yes=false;
        vines[0].best_length=vines[0].dist;
        for(int i=0; i<n_vine && !yes; i++)
        {
            if(vines[i].best_length<0) break;
            if(vines[i].dist+vines[i].best_length>=total) { yes=true; break; }

            for(int j=1; j+i<n_vine && vines[i].dist+vines[i].best_length>=vines[i+j].dist; j++)
            {
                int dist=min(vines[i+j].length, vines[i+j].dist-vines[i].dist);
                vines[i+j].best_length=max(vines[i+j].best_length, dist);
                if(vines[i+j].best_length + vines[i+j].dist>=total) { yes=true; break; }
            }
        }
        if(yes) cout << "YES" << endl; else cout << "NO" << endl;
    }
    return 0;
}
