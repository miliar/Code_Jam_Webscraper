/*
 * Author: xn_rookie
 * Created Time:  2011/5/22 17:22:31
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;



const int N = 50;

string block[N];
int n, m;


void init()
{
    cin >> n >> m;
    for(int i=0;i<n;i++)
        cin>>block[i];
}

#define IMPOS cout << "Impossible" << endl; return;

void solve()
{
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<m-1;j++)
        {
            if (block[i][j] == '#'){
                if (block[i][j+1] != '#' || block[i+1][j] != '#' || block[i+1][j+1] != '#'){
                    IMPOS
                }
                else {
                    block[i][j] = block[i+1][j+1] = 47, block[i][j+1] = block[i+1][j] = 92;
                }
            }
        }
        if (block[i][m-1] == '#') {
            IMPOS
        }
    }
    
    for(int j=0;j<m;j++)
    {
        if (block[n-1][j] == '#') {
            IMPOS
        }
    }
    
    for(int i=0;i<n;i++)
        cout<<block[i]<<endl;
}


int main(){
    
    int T; cin >> T;
    for(int i=1;i<=T;i++)
    {
        init();
        printf("Case #%d:\n", i);
         solve();
    }
}

