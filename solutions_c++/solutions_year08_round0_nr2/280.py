#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <memory.h>

using namespace std;

#define LL                  long long
#define pb                  push_back
#define mp                  make_pair
typedef vector <int>        vi;
typedef vector <string>     vs;

int t,na,nb;
int as[100],ae[100],bs[100],be[100];
bool da[100], db[100];
int res1,res2;

void input()
{
    int i,hh,mm;
    string buf;

    cin >> t >> na >> nb;

    for (i=0; i<na; i++)
    {
        cin >> buf; sscanf(buf.c_str(), "%d:%d", &hh, &mm); as[i] = hh*60 + mm;
        cin >> buf; sscanf(buf.c_str(), "%d:%d", &hh, &mm); ae[i] = hh*60 + mm;
    }
    for (i=0; i<nb; i++)
    {
        cin >> buf; sscanf(buf.c_str(), "%d:%d", &hh, &mm); bs[i] = hh*60 + mm;
        cin >> buf; sscanf(buf.c_str(), "%d:%d", &hh, &mm); be[i] = hh*60 + mm;
    }

}

void process()
{
    int i,j,mm,k;

    memset(da, true, sizeof(da));
    memset(db, true, sizeof(db));

    //--
    for (i=0; i<na; i++)
    {
        mm = INT_MAX; k = -1;
        for (j=0; j<nb; j++) if (db[j] && bs[j]>=ae[i]+t && mm>bs[j]) { mm = bs[j]; k=j; }
        if (k==-1) continue;

        db[k] = false;
    }

    //--
    for (i=0; i<nb; i++)
    {
        mm = INT_MAX; k = -1;
        for (j=0; j<na; j++) if (da[j] && as[j]>=be[i]+t && mm>as[j]) { mm = as[j]; k=j; }
        if (k==-1) continue;

        da[k] = false;
    }

    //--
    res1 = res2 = 0;
    for (i=0; i<na; i++) if (da[i]) res1++;
    for (i=0; i<nb; i++) if (db[i]) res2++;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int i,j,numTest;
    char buf[201];
    
    cin >> numTest; 
    for (i=0; i<numTest; i++)
    {
        input();
        process();
        cout << "Case #" << (i+1) << ": " << res1 << " " << res2 << endl;
    }
    return 0;
}
