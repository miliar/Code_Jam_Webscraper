//Copyright by Le Viet Thanh Long
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <iomanip>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <cstdlib>

#define maxn 1000+7
#define eps 1e-6
#define oo 1000000000

using namespace std;
typedef long long LL;
typedef pair<int,int> II;
typedef pair<II,int> III;

string Moon,st;

void Input()
{
    getline(cin,st);
}

void Solve(int t)
{
    printf("Case #%d: ",t);
    for (int i = 0; i < st.length(); i++)
        if (st[i] == ' ')
            cout << " ";
        else cout << Moon[ st[i] - 'a' ];
    printf("\n");
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("ProblemA.out","w",stdout);
    Moon = "yhesocvxduiglbkrztnwjpfmaq";
    int t;
    cin >> t;
    getline(cin,st);
    for (int i = 1; i <= t; i++)
    {
        Input();
        Solve(i);
    }
    return 0;
}
