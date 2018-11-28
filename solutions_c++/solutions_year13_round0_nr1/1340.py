#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

#define clr(name,val) memset(name,(val),sizeof(name));
#define EPS .000000001
#define ll long long
#define psb(b) push_back((b))
#define ppb() pop_back()
#define oo 10000000
#define mp make_pair
#define fs first
#define sc second
#define rep(var,s,n) for(var=(s);var<(n);(var)++)
#define rvp(var,s,n) for(var=(n-1);var>(s-1);(var)--)
#define read_ freopen("input.txt","r",stdin)
#define write_ freopen("output.txt","w",stdout)

using namespace std;

int main()
{
    read_;
    write_;
    int test,cas=0;
    char arr[5][5];
    scanf("%d",&test);
    while(test--)
    {
        bool x=false,o=false,emt=false;
        clr(arr,0);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf(" %c",&arr[i][j]);
                if(arr[i][j]=='.') emt=true;
            }
        }
        int cntx,cnto;
        for(int i=0;i<4;i++)
        {
            cntx=0,cnto=0;
            for(int j=0;j<4;j++)
            {
                if(arr[i][j]=='X'||arr[i][j]=='T') cntx++;
                if(arr[i][j]=='O'||arr[i][j]=='T') cnto++;
            }
            if(cntx==4)
            {
                x=true;
                break;
            }
            else if(cnto==4)
            {
                o=true;
                break;
            }
        }
        for(int i=0;i<4;i++)
        {
            cntx=0,cnto=0;
            for(int j=0;j<4;j++)
            {
                if(arr[j][i]=='X'||arr[j][i]=='T') cntx++;
                if(arr[j][i]=='O'||arr[j][i]=='T') cnto++;
            }
            if(cntx==4)
            {
                x=true;
                break;
            }
            else if(cnto==4)
            {
                o=true;
                break;
            }
        }
        cntx=0,cnto=0;
        for(int j=0;j<4;j++)
        {
            if(arr[j][j]=='X'||arr[j][j]=='T') cntx++;
            if(arr[j][j]=='O'||arr[j][j]=='T') cnto++;
        }
        if(cntx==4)
        {
            x=true;
        }
        else if(cnto==4)
        {
            o=true;
        }
        cntx=0,cnto=0;
        for(int j=0;j<4;j++)
        {
            if(arr[j][3-j]=='X'||arr[j][3-j]=='T') cntx++;
            if(arr[j][3-j]=='O'||arr[j][3-j]=='T') cnto++;
        }
        if(cntx==4)
        {
            x=true;
        }
        else if(cnto==4)
        {
            o=true;
        }
        printf("Case #%d: ",++cas);
        if(x)
        {
            printf("X won\n");
        }
        else if(o)
        {
            printf("O won\n");
        }
        else if(emt)
        {
            printf("Game has not completed\n");
        }
        else printf("Draw\n");

    }
    return 0;
}
