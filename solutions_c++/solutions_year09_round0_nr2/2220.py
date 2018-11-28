/* 
 * File:   PB.cpp
 * Author: Kimi
 *
 * Created on 2009年9月3日, 下午8:01
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
typedef pair<int,int> Tque;
const int add[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int g[100][100],m,n,tsp;
char gg[100][100];
vector<int> edge[100][100];

bool inrange(int a, int b, int ma, int mb)
{
    return a>=0 && a<ma && b>=0 && b<mb;
}

void dfs(int x, int y)
{
    for (int i=0; i<4; i++)
        if (inrange(x+add[i][0],y+add[i][1],m,n) && gg[x+add[i][0]][y+add[i][1]]==tsp) {
            gg[x+add[i][0]][y+add[i][1]]=gg[x][y];
            dfs(x+add[i][0],y+add[i][1]);
        }
}

int main() {
    int tt;
    scanf("%d",&tt);
    for (int t=0; t<tt; t++) {
        scanf("%d%d",&m,&n);
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) scanf("%d",&g[i][j]);
        }
        queue<Tque> que;
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++)
                edge[i][j].clear();
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                int p=-1, pp=g[i][j];
                for (int k=0; k<4; k++)
                    if (inrange(i+add[k][0],j+add[k][1],m,n)) {
                        if (g[i+add[k][0]][j+add[k][1]]<pp) {
                            pp=g[i+add[k][0]][j+add[k][1]];
                            p=k;
                        }
                    }
                if (p<0) {
                    gg[i][j]=que.size();
                    que.push(make_pair(i,j));
                }
                else edge[i+add[p][0]][j+add[p][1]].pb(3-p);
            }
        }
        while (!que.empty()) {
            for (vector<int>::iterator iter=edge[que.front().first][que.front().second].begin(); iter!=edge[que.front().first][que.front().second].end(); iter++) {
                gg[que.front().first+add[*iter][0]][que.front().second+add[*iter][1]]=gg[que.front().first][que.front().second];
                que.push(make_pair(que.front().first+add[*iter][0],que.front().second+add[*iter][1]));
            }
            que.pop();
        }
        char ch='a';
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++)
                if (gg[i][j]<40) {
                    tsp=gg[i][j];
                    gg[i][j]=ch;
                    dfs(i,j);
                    ch++;
                }
        }
        printf("Case #%d:\n",t+1);
        for (int i=0; i<m; i++) {
            for (int j=0; j+1<n; j++)
                printf("%c ",gg[i][j]);
            printf("%c\n",gg[i][n-1]);
        }
    }
    return (EXIT_SUCCESS);
}

