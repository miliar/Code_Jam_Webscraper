#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


//*
#include <fstream>
fstream fin ("D://CodeJamRound1/A-small-attempt2.in",ios::in);
fstream fout ("D://CodeJamRound1/outputout.txt", ios::out);
#define cin fin
#define cout fout
//*/


bool IsInteger(float f)
{
    int i = (int)f;
    if( fabs((float)i - f) < 0.000001 || fabs(fabs((float)i - f)-1.0f) < 0.000001 )
        return true;

    return false;
}

template<class T> inline T gcd(T a,T b)//NOTES:gcd(
{
    if(a<0)return gcd(-a,b);
    if(b<0)return gcd(a,-b);
    return (b==0)?a:gcd(b,a%b);
}

int main()
{
    int caseNum;
    cin >> caseNum;


    for(int mm=0; mm<caseNum; mm++)
    {
        int N , PD, PG;
        cin >> N >> PD >> PG;

        if(PD == 0)
        {
            if(PG < 100)
                cout << "Case #"<<mm+1<<": Possible" << endl;
            else
                cout << "Case #"<<mm+1<<": Broken" << endl;
            continue;
        }

        if(PD == 100)
        {
            if(PG != 0 )
                cout << "Case #"<<mm+1<<": Possible" << endl;
            else
                cout << "Case #"<<mm+1<<": Broken" << endl;
            continue;
        }

        if(PD < 100 && PG == 100)
        {
            cout << "Case #"<<mm+1<<": Broken" << endl;
            continue;
        }

        if(PD > 0 && PG == 0)
        {
            cout << "Case #"<<mm+1<<": Broken" << endl;
            continue;
        }



        bool bPossible = false;

        int pdFactor = PD / gcd(PD, 100);
        //cout << "pdFactor: " << pdFactor <<  endl;

        int pgFactor = PG / gcd(PG, 100);
        for(int i=pdFactor; i<=N; i+= pdFactor)
        {
            if(i > N)
                break;

            int possibleN = (float)i / (float) PD * 100;
            if( possibleN > N )
                continue;
            bPossible = true;
        }

        if(true == bPossible)
            cout << "Case #"<<mm+1<<": Possible" << endl;
        else
            cout << "Case #"<<mm+1<<": Broken" << endl;
    }

    return 0;
}
