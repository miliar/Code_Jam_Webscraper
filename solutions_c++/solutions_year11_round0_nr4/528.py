#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int n;
int list[10000];

//map<int, int> id;
int pos[10000];

void init()
{
    scanf("%d", &n);
    for (int  i = 0; i < n; i++)
    {
        scanf("%d", list + i);
        list[i] --;
    }
}

void solve2()
{
    int    ret = 0;
    for (int i = 0; i < n; i ++)
        if (list[i] - i) ret ++;
    printf("%d.000000\n", ret);
}

void solve()
{/*
    vector< pair<int, int> > sortlist;
    for (int i = 0; i < n; i ++)
        sortlist.push_back( make_pair(list[i], i) );
    sort(sortlist.begin(), sortlist.end());
    
    for (int i = 0; i < n; i ++)
    {
        id[ sortlist[i].first ] = i;
        pos[i] = sortlist[i].second;
    }
    */

   
    for (int i = 0; i < n; i ++)
        pos[ list[i] ] = i;


/*
    int ans = 0;

    for (int i = 0; i < n; i ++)
//        if (id[ list[i] ] != i)
        if (list[i] != i)
        {
            int j = pos[ i ];
            int t = list[i]; list[i] = list[j]; list[j] = t;
            //pos[ id[ list[i] ] ] = i;
            //pos[ id[ list[j] ] ] = j;
            pos[ list[i] ] = i;
            pos[ list[j] ] = j;
            ans ++;
        }

    printf("%d.000000\n", ans * 2);
    */

    solve2();
}

int main()
{
//    freopen("in.txt", "r", stdin);

//    freopen("D-small-attempt1.in", "r", stdin);
//    freopen("D-small.out", "w", stdout);

    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t ++)
    {
         printf("Case #%d: ", t);

         init();
         solve();
    }

    return 0;
}