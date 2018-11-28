/* 
 * File:   Rotate.cpp
 * Author: kimi
 *
 * Created on May 22, 2010, 9:10 AM
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
#include <climits>
#define Fill(A,n) memset(A,n,sizeof(A))
#define pb push_back

using namespace std;

string Filename="A-large";

const int MAX_N=50;
int N,K;
string Board[MAX_N];

int main() {
    freopen((Filename+".in").c_str(),"r",stdin);
    freopen((Filename+".out").c_str(),"w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=0; t<T; t++) {
        // Process input;
        scanf("%d%d",&N,&K);
        for (int i=0; i<N; i++)
            while (getline(cin,Board[i]),Board[i]=="");

        // Rotate;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N/2; j++)
                swap(Board[i][j],Board[i][N-j-1]);
            int L=0;
            for (int j=0; j<N; j++)
                if (Board[i][j]!='.') {
                    char ch=Board[i][j];
                    Board[i][j]='.';
                    Board[i][L++]=ch;
                }
        }

        // Count;
        bool Red=false,Blue=false;
        // Part I: Vertical;
        for (int i=0; i<=N-K; i++)
            for (int j=0; j<N; j++) {
                bool same=true;
                if (Board[i][j]=='.') continue;
                for (int k=1; k<K; k++)
                    if (Board[i+k][j]!=Board[i][j]) {
                        same=false;
                        break;
                    }
                if (same) if (Board[i][j]=='R') Red=true;
                else Blue=true;
            }

        // Part II: Horizontal;
        for (int i=0; i<N; i++)
            for (int j=0; j<=N-K; j++) {
                bool same=true;
                if (Board[i][j]=='.') continue;
                for (int k=1; k<K; k++)
                    if (Board[i][j+k]!=Board[i][j]) {
                        same=false;
                        break;
                    }
                if (same) if (Board[i][j]=='R') Red=true;
                else Blue=true;
            }

        // Part III: Diagonal from left upper corner;
        for (int i=0; i<=N-K; i++)
            for (int j=0; j<=N-K; j++) {
                bool same=true;
                if (Board[i][j]=='.') continue;
                for (int k=1; k<K; k++)
                    if (Board[i+k][j+k]!=Board[i][j]) {
                        same=false;
                        break;
                    }
                if (same) if (Board[i][j]=='R') Red=true;
                else Blue=true;
            }

        // Part IV: Diagonal from right upper corner;
        for (int i=0; i<=N-K; i++)
            for (int j=K-1; j<N; j++) {
                bool same=true;
                if (Board[i][j]=='.') continue;
                for (int k=1; k<K; k++)
                    if (Board[i+k][j-k]!=Board[i][j]) {
                        same=false;
                        break;
                    }
                if (same) if (Board[i][j]=='R') Red=true;
                else Blue=true;
            }

        // Process output;
        printf("Case #%d: %s\n",t+1,Blue?Red?"Both":"Blue":Red?"Red":"Neither");
    }
    return (EXIT_SUCCESS);
}
