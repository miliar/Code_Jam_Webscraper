/* 
 * File:   PA.cpp
 * Author: Kimi
 *
 * Created on 2009年9月3日, 下午6:50
 */

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
#include <complex>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#define Fill(A,n) memset(A,n,sizeof(A))
#define pb push_back

using namespace std;

/*
 *
 */
string wd[6000];
vector<int> h,hh;
int pp;

bool ok(string s,int p,int pt)
{
    if (s[pp]!='(') return s[pp]==wd[p][pt];
    bool y=false;
    for (int i=pp+1; i<s.size(); i++)
        if (s[i]==')') break;
        else if (s[i]==wd[p][pt]) y=true;
    return y;
}
int push(string s,int p)
{
    if (s[p]!='(') return p+1;
    for (int i=pp+1; i<s.size(); i++)
        if (s[i]==')') return i+1;
}

int main() {
    int L,D,N;
    scanf("%d%d%d",&L,&D,&N);
    for (int i=0; i<D; i++)
        cin >> wd[i];
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        h.clear();
        for (int j=0; j<D; j++) h.pb(j);
        pp=0;
        for (int j=0; j<L; j++) {
            hh.clear();
            for (int k=0; k<h.size(); k++)
                if (ok(s,h[k],j)) hh.pb(h[k]);
            pp=push(s,pp);
            h=hh;
        }
        printf("Case #%d: %d\n",i+1,h.size());
    }
    return (EXIT_SUCCESS);
}

