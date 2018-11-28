/*
 * Author: FreePascal
 * Created Time:  2012/4/14 10:29:30
 * File Name: gcj2.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <list>
#include <stack>
#include <fstream>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
vector<int> vt;
int t,n,s,p;
int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    cin>>t;
    for(int cs = 1; cs <= t;cs ++)
            {
                cin>>n>>s>>p;
                vt.clear();
                for(int i = 0;i < n;i ++)
                {
                    int k;
                    cin>>k;
                    vt.push_back(k);
                }
                sort(vt.begin(),vt.end());
                int ans = 0;
                for(int i = 0;i < n;i ++)
                {
                    if(vt[i] == 0) {
                        if(p == 0){ ans++;continue;}
                        else continue;
                    }
                    if(vt[i] == 1){
                        if(p <= 1){ ans++;continue;}
                        else continue;
                    }
                    if(vt[i] >= 3*p - 2) {ans++; continue;}
                    if(s && vt[i] >= 3*p - 6){ ans++,s--;}
                }
            cout<<"Case #"<<cs<<": "<<ans<<endl;
            }
    return 0;
}

