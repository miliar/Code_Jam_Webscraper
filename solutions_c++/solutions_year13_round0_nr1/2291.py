/*
Try Try & Try until you solve the problem...
Nothing is impossible for the problem solvers... :)
*/
/*

*/
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <numeric>

#include <cmath>
#include <cstdio>

#define IP(n) for(i=0;i<n;i++)
#define JP(n) for(j=0;j<n;j++)
#define KP(n) for(k=0;k<n;k++)

#define vi vector<int>
#define vi2 vector<vector<int>>
#define vs vector<string>

#define pb push_back
#define TC int t,check=1;cin>>t;while(check<=t)
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define ms(x,a) memset(x,a,sizeof(x))
#define read(a) freopen(a,"r",stdin)
#define write(a) freopen(a,"w",stdout)

using namespace std;

char brd[10][10],grbg[10];

string m[]={"XXXX","XXXT","XXTX","XTXX","TXXX","OOOO","OOOT","OOTO","OTOO","TOOO"};

int found(string s)
{
    for(int i=0;i<10;i++)
    {
        if(s==m[i]) return i;
    }

    return -1;
}

int solve()
{
    int flag=0;

    string s="";

    for(int i=0;i<4 && !flag;i++)
    {
        s="";

        for(int j=0;j<4;j++)
        s+=brd[i][j];

        int f=found(s);

        if(f!=-1)
        {
            if(f<5) flag=1;
            else flag=2;
        }
    }

    for(int j=0;j<4 && !flag;j++)
    {
        s="";

        for(int i=0;i<4;i++)
        s+=brd[i][j];

        int f=found(s);

        if(f!=-1)
        {
            if(f<5) flag=1;
            else flag=2;
        }
    }

    if(!flag)
    {
        s="";
        for(int i=0;i<4;i++)
        s+=brd[i][i];

        int f=found(s);

        if(f!=-1)
        {
            if(f<5) flag=1;
            else flag=2;
        }
    }

    if(!flag)
    {
        s="";
        for(int i=0;i<4;i++)
        s+=brd[i][3-i];

        int f=found(s);

        if(f!=-1)
        {
            if(f<5) flag=1;
            else flag=2;
        }
    }

    if(!flag)
    {
        flag=3;

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            if(brd[i][j]=='.') return 4;
        }
    }

    return flag;
}

int main()
{
    read("Al.in");
    write("Al.txt");

    int t,check=1;
    scanf("%d",&t);
    while(t--)
    {
        gets(grbg);
        for(int i=0;i<4;i++)
        gets(brd[i]);

        int ans=solve();

        if(ans==1)
        printf("Case #%d: X won\n",check++);
        else if(ans==2)
        printf("Case #%d: O won\n",check++);
        else if(ans==3)
        printf("Case #%d: Draw\n",check++);
        else
        printf("Case #%d: Game has not completed\n",check++);
    }

    return 0;
}
