// =========================================================
//
//       Filename:  Dancing With the Googlers.cpp
//
//    Description:
//
//        Version:  1.0
//        Created:  04/14/2012
//       Revision:  none
//       Compiler:  g++
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 04/14/2012
//
// =========================================================

#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

#define MAXNUM 200

int triplete(int t, int p, bool surprising)
{
    bool result;

    if (t == 0)
        return (!surprising) && (p == 0)?1:0;

    if (t == 1)
        return (!surprising) && (p <= 1)?1:0;

    switch (t % 3)
    {
        case 0: result = surprising?((t/3)+1)>=p:(t/3)>=p; break;
        case 1: result = surprising?((t/3)+1)>=p:((t/3)+1)>=p; break;
        case 2: result = surprising?((t/3)+2)>=p:((t/3)+1)>=p; break;
    }

    return result?1:0;
}

unsigned int solve()
{
    unsigned int N;
    unsigned int S;
    unsigned int p;
    unsigned int googler[MAXNUM];

    unsigned int n;
    unsigned int s;

    // load parameters
    cin >> N;
    cin >> S;
    cin >> p;

    // init
    for (n=0; n<=N; ++n)
        googler[n] = 0;

    // load points
    for (n=1; n<=N; ++n)
    {
        int t;
        cin >> t;

        //googler[n] = googler[n-1] + triplete(t, p, true);
        for (s=n; s>0; --s)
        {
            unsigned int foo;
            googler[s] += triplete(t, p, false);
            foo = googler[s-1] + triplete(t, p, true);
            if (foo > googler[s])
                googler[s] = foo;
        }
        googler[0] = googler[0] + triplete(t, p, false);
    }

    return googler[S];
}

int main()
{
    unsigned int case_no;
    unsigned int result;

    // load input
    cin >> case_no;

    for (unsigned int i = 0; i < case_no; i++)
    {
        // sove problem
        result = solve();
        cout << "Case #" << i+1 << ": ";
        cout << result << endl;
    }

    return 0;

}
