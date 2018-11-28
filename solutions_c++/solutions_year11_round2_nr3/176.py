#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdlib>
#include <list>
#include <set>
#include <ctime>
#include <list>
#include <fstream>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define vi vector<int>
#define vd vector<double>
#define pii pair<int,int>
#define pdd pair<double,double>
#define ll long long
#define INF (1<<30)
using namespace std;

const int maxn = 10;
int col[maxn], n, m;
int cols;
vector<vector<int> > rooms;
bool isok;
ofstream out("C.out");

void check()
{
    if(isok) return;
    set<int> avail;
    int i, j;
    for(i = 0; i < rooms.size(); ++i)
    {
        avail.clear();
        for(j = 0; j < rooms[i].size(); ++j) avail.insert(col[rooms[i][j]]);
        if(avail.size() != cols) return;
    }
    isok = true;
    out << cols << '\n';
    for(i = 0; i < n - 1; ++i) out << col[i] << ' ';
    out << col[n - 1] << '\n';
}

void gen(int pos)
{
    if(pos == n)
    {
        check();
        return;
    }
    int i;
    for(i = 0; i < cols; ++i)
    {
        col[pos] = i + 1;
        gen(pos + 1);
        if(isok) return;
    }
}

void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    out << "Case #" << case_id << ": ";
    int i, j, k, u[maxn], v[maxn];
    cin >> n >> m;
    rooms.clear();
    vector<int> emp;
    rooms.pb(emp);
    for(i = 0; i < n; ++i) rooms[0].pb(i);
    for(i = 0; i < m; ++i) cin >> u[i];
    for(i = 0; i < m; ++i) cin >> v[i];
    for(i = 0; i < m; ++i)
    {
        --u[i]; -- v[i];
        int upos, vpos;
        for(j = 0; j < rooms.size(); ++j) // tyrsime koq staq razdelq stenata
        {
            upos = -1; vpos = -1;
            for(k = 0; k < rooms[j].size(); ++k)
            {
                if(rooms[j][k] == u[i]) upos = k;
                if(rooms[j][k] == v[i]) vpos = k;
            }
            if(upos >=0 && vpos >=0) break;
        }
        // razdelq j-tata staq
        if(upos > vpos) swap(upos, vpos);
        vector<int> nr1, nr2;
        k = upos;
        while(1)
        {
            nr1.pb(rooms[j][k]);
            if(k == vpos) break;
            k = (k + 1) % (int)rooms[j].size();
        }
        k = upos;
        while(1)
        {
            nr2.pb(rooms[j][k]);
            if(k == vpos) break;
            k = (k - 1 + (int)rooms[j].size()) % (int)rooms[j].size();
        }
        rooms[j] = nr1;
        rooms.pb(nr2);
    } // dotuk namirahme koi sa staite :D
    /*for(i = 0; i < rooms.size(); ++i, printf("\n"))
        for(j = 0; j < rooms[i].size(); ++j) printf("%d ", rooms[i][j]);*/
    // sega probvame da ocvetqvame po nai-debilniq vyzmojen nachin
    for(cols = min(n - 1, 5); cols >= 1; --cols)
    {
        isok = false;
        gen(0);
        if(isok) break;
    }
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}

