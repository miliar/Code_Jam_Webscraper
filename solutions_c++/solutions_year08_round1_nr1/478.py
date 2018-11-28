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

    int z; int t;
    
    scanf("%d",&t);
    REP(z,t){
        vector<int> a,b;
        int n;
        scanf("%d", &n);
        REP(i,n){ int tmp; scanf("%d", &tmp); a.PB(tmp); }
        REP(i,n){ int tmp; scanf("%d", &tmp); b.PB(tmp); }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        reverse(b.begin(),b.end());
        int min=INT_MAX;
        int prod=0;
                REP(i,n) prod+=(a[i]*b[i]);
                if(prod<min)min=prod;

/*
        do{
            sort(b.begin(),b.end());
            do{
                
            }while(next_permutation(b.begin(),b.end()));


        }while(next_permutation(a.begin(),a.end()));*/

        printf("Case #%d: %d\n",z+1,min);
    }

    return 0;
}

