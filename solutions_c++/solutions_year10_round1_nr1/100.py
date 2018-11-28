#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

char c[60][60],a[60];
int n,m;

bool check(char key)
{
    for (int i=0;i<n;i++)
    {
        int s=0;
        for (int j=0;j<n;j++)
        {
            if (c[i][j]==key) s++;
                else s=0;
            if (s==m) return true;
        }
    }
    for (int i=0;i<n;i++)
    {
        int s=0;
        for (int j=0;j<n;j++)
        {
            if (c[j][i]==key) s++;
                else s=0;
            if (s==m) return true;
        }
    }
    
    for (int i=0;i<n;i++)
    {
        int s=0,x=i;
        for (int y=0;y<n && x>=0;x--,y++)
        {
            if (c[x][y]==key) s++;
                else s=0;
            if (s==m) return true;
        }
    }
    
    for (int i=0;i<n;i++)
    {
        int s=0,y=i;
        for (int x=n-1;y<n && x>=0;x--,y++)
        {
            if (c[x][y]==key) s++;
                else s=0;
            if (s==m) return true;
        }
    }
    
    for (int i=0;i<n;i++)
    {
        int s=0,x=i;
        for (int y=0;y<n && x<n;x++,y++)
        {
            if (c[x][y]==key) s++;
                else s=0;
            if (s==m) return true;
        }
    }
    
    for (int y=0;y<n;y++)
    {
        int s=0,x=0;
        for (int y=0;y<n && x<n;x++,y++)
        {
            if (c[x][y]==key) s++;
                else s=0;
            if (s==m) return true;
        }
    }
    return false;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d\n",&T);
    for (int casenum=1;casenum<=T;casenum++)
    {
        scanf("%d %d\n",&n,&m);
      //  cout << m << endl;
        for (int i=0;i<n;i++)
        {
            gets(c[i]);
            for (int j=0;j<n;j++)
                a[j]='.';
            a[n]='\0';
            int tot=n-1;
            for (int j=n-1;j>=0;j--)
                if (c[i][j]!='.') a[tot--]=c[i][j];
            memcpy(c[i],a,sizeof(a));
          //  puts(c[i]);
        }
        bool p1=check('R'),p2=check('B');
        if (p1 && p2) printf("Case #%d: Both\n",casenum);
        else
        if (p1) printf("Case #%d: Red\n",casenum);
        else
        if (p2) printf("Case #%d: Blue\n",casenum);
        else
            printf("Case #%d: Neither\n",casenum);
    }
}
