// Template By Fendy Kosnatha (Seraph)
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
#include <cstring>
#include <string.h>

#define fs first
#define sc second
#define mp make_pair
#define pii pair<int, int>

using namespace std;
int r[1001];
bool cmp(int a, int b)
{
    return a>b;
}
bool comp(pair<int, int> a, pair<int, int> b)
{
    return a.fs > b.fs;
}
double x[1001],y[1001];
pair<int, int> id[1001];
int main()
{
    int tc;
    cin>>tc;
    int count=1;
    while (tc--)
    {
        int n,w,h;
        cin>>n>>w>>h;;
        for (int i=0;i<n;i++)
        {
            cin>>r[i];
            id[i].fs = r[i];
            id[i].sc = i;
        }
        memset(x,0,sizeof(x));
        memset(y,0,sizeof(y));
        
        sort(r,r+n,cmp);
        sort(id,id+n,comp);
        x[0]=0;
        y[0]=0;
        int lain=0;
        int pert=0;
        for (int i=1;i<n;i++)
        {
            int a,b;
            x[i] = x[i-1]+r[i-1]+r[i] + 1;
            y[i] = y[i-1];
            if (x[i]>=w) 
            {
                x[i]=0;
                y[i] = y[pert] + r[pert] + r[i] + 1;
                pert = i;
            }
        }
        cout<<"Case #"<<count++<<":";
        double a[1001];
        double b[1001];
        for (int i=0;i<n;i++)
        {
            a[id[i].sc] = x[i];
            b[id[i].sc] = y[i];
            
        }
        for (int i=0;i<n;i++)
        {
            printf(" %.1lf %.1lf",a[i],b[i]);
        }
        cout<<endl;
    }
    return 0;
}
