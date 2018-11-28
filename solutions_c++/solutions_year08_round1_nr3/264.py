// GCJr1Prob1.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
typedef long long ll; 
 
using namespace std;



//int _tmain(int argc, _TCHAR* argv[])
int main()
{
    int a[40];
    a[2]=27;a[3]=143;a[4]=751;a[5]=935;
    a[6]=607;a[7]=903;a[8]=991;a[9]=335;
    a[10]=47;a[11]=943;a[12]=471;a[13]=55;
    a[14]=447;a[15]=463;a[16]=991;a[17]=95; //095
    a[18]=607;a[19]=263;a[20]=151;a[21]=855;
    a[22]=527;a[23]=743;a[24]=351;a[25]=135;
    a[26]=407;a[27]=903;a[28]=791;a[29]=135;
    a[30]=647;


    int n;
    scanf("%d",&n);
    REP(z,n)
    {
        int t;
        scanf("%d", &t);
        

        if(a[t]>100)
            printf("Case #%d: %d\n",z+1,a[t]);
        else
            printf("Case #%d: 0%d\n",z+1,a[t]);
    }

    return 0;
}

