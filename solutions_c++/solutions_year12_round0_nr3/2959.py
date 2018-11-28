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

int a,b;

void Input()
{
    cin >> a >> b;
}

string ToString(int n)
{
    string st = "";
    while (n != 0)
    {
        char tmp = (n % 10) + '0';
        st = tmp + st;
        n /= 10;
    }
    return st;
}

void Solve(int t)
{
    int res = 0;
    string B = ToString(b);
    string tmp;
    for (int i = a; i <= b; i++)
    {
        string st = ToString(i);
        for (int j = 0; j < st.length(); j++)
        {
            string S = st.substr(st.length()-j-1, j+1) + st.substr(0,st.length()-j-1);
            if (S != tmp && S > st && S <= B)
            {
                res++;
                tmp = S;
                //cout << st << " -> " << S << endl;
            }
        }            
    }
    printf("Case #%d: %d\n",t,res);
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("ProblemC.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; i++)
    {
        Input();
        Solve(i);
    }
    return 0;
}
