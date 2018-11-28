//Headers
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <climits>
#include <clocale>
//Defines
#define pow2(i) (1<<i)
#define bit(i) (1<<i)
#define isOdd(i) (i&1)
#define isEven(i) (!(i&1))
#define isPrime(i) ((i==2) || ((i&1) && !pTest[i])) //pTest has to be the bool array's name
#define sz(i) i.size()
#define vec(type,name) vector< type > name
#define rep(i,a,b) for(int i=a ; i<=b ; i++)
#define swap(type,a,b) {type t=a; a=b; b=t;}
#define sum(a,n) ( (n*(n+1)/2) - (a-1)*a/2 )
#define iscap(i) (i>='A'&&i<='Z')
#define issmall(i) (i>='a'&&i<='z')
#define isnum(i) (i>='0'&&i<='9')
#define issymbol(i) (!(i>='a'&&i<='z') && !(i>='A'&&i<='Z') && !(i>='0'&&i<='9'))
#define mk(i,j) make_pair(i,j)
#define ERROR 1e-11
//Type Defs
typedef long long lint;
typedef unsigned long long ulint;
typedef long double ldouble;

using namespace std;

class trp
{
    public:
    int a, b, c;
};

vector< vector<trp> > triplets;

int triplet_finder(int n)
{
    int i, j, k;
    vector<trp> lst;
    for (i=n ; i>=0 ; i--)
    {
        for (j=n ; j>=0 ; j--)
        {
            for (k=n ; k>=0 ; k--)
            {
                if (i + j + k  == n && abs(i-j)<=2 && abs(j-k)<=2 && abs(k-i)<=2)
                {
                    lst.push_back((trp){i,j,k});
                }
            }
        }
    }
    triplets.push_back(lst);
}

vector<trp> test, fin_list;
int l[200], mx_res;

int test_list(int s, int p)
{
    int sc, pc, i, a, b, c;
    //printf("Start %d\n",test.size());
    for (i=0, sc=0, pc=0 ; i<test.size() ; i++)
    {
        a = test[i].a;
        b = test[i].b;
        c = test[i].c;

        //printf("{ %d %d %d }\n",a,b,c);

        if (abs(a-b)==2 || abs(b-c)==2 || abs(c-a)==2)
        {
            sc++;
        }
        if (sc > s) return -1;

        if (a >= p || b>=p || c>=p)
            pc++;
    }
    //printf("End %d\n",pc);

    return pc;
}


int find (int i, int lim, int s, int p)
{
    int t, res;

    for (t=0 ; t<triplets[l[i]].size() ; t++)
    {
        test.push_back(triplets[l[i]][t]);

        if (i<lim)
        {
            find(i+1, lim, s, p);
        } else {
            res = test_list(s,p);
            if (res > mx_res)
            {
                mx_res = res;
            }
        }
        test.pop_back();
    }
}

int main()
{
    //     TEST CASE     //
    int kase=1, kounter=1;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w+",stdout);
    int i, n, s, p, res;

    for (i=0 ; i<=30 ; i++)
    {
        triplet_finder(i);
    }

    /*while ( cin >> n )
    {
        for (i=0 ; i<triplets[n].size() ; i++)
        {
            cout << n << " -> " << triplets[n][i].a << " " << triplets[n][i].b << " " << triplets[n][i].c << endl;
        }
    }*/


    scanf("%d",&kase);

    while (kase--)
    {
        scanf("%d %d %d",&n,&s,&p);

        for (i=0 ; i<n ; i++)
        {
            scanf("%d",&l[i]);
        }

        test.clear();
        fin_list.clear();
        mx_res = -10000;
        find (0, n-1, s, p);
        printf("Case #%d: %d\n",kounter++, mx_res);
    }







    return 0;
}
