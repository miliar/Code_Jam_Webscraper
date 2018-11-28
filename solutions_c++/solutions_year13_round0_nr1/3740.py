#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
/*bool cmp(const int cmp1,const int cmp2){
     return cmp1>cmp2;
}

bool browsing(const int i,const int j, int cnt, char pre)
{
    if (cnt == 4)
        return true;
    if (z[i][j]=='.') return false;
    int l[8]={1,1,1,0,0,-1,-1,-1};
    int c[8]={-1,0,1,-1,1,-1,0,1};
    for(int k=0;k<8;k++)
    {
        if (i+l[k] >= 0 && i+l[k]<4 && j+c[k]>=0 && j+c[k]<4 && (pre == z[i+l[k]][j+c[k]]||z[i+l[k]][j+c[k]]=='T'))
            browsing(i+l[k],j+c[k], cnt+1, z[i][j]=='T'?pre:z[i][j]);
        else 
            return false;
    }
}*/
int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
    int t;
    std::cin>>t;
    for(int zz=0;zz<t;zz++)
    {
        string x;
        getline(cin, x);

        char z[4][4];
        memset(z,0x00,sizeof(z));
        bool empty=false;
        for(int i=0;i<4;i++)
        {
            string s;
            getline(cin,s);
            for(int j=0;j<4;j++)
            {    
                z[i][j]=s[j];
                if (z[i][j]=='.')
                    empty=true;
            }
        }
        bool f=false;
        char out;
        //가로
        for(int i=0;i<4;i++)
        {
            char first=z[i][0];
            if (first=='T')
                first= z[i][1];

            if (first=='.')
                continue;

            int cnt=0;

            for(int j=1;j<4;j++)
            {
                if (first == z[i][j] || z[i][j]=='T')
                {
                    cnt++;
                }
            }
            if (cnt == 3)
            {
                f=true;
                out=first;
                break;
            }
        }

        cout<<"Case #"<<zz+1;
        if (f)
        {
            cout<<": "<<out<<" won\n";
            continue;
        }

        //세로
        for(int j=0;j<4;j++)
        {
            char first=z[0][j];
            if (first=='T')
                first= z[1][j];

            if (first=='.')
                continue;

            int cnt=0;

            for(int i=1;i<4;i++)
            {
                if (first == z[i][j]|| z[i][j]=='T')
                {
                    cnt++;
                }
            }
            if (cnt == 3)
            {
                f=true;
                out=first;
                break;
            }
        }
        if (f)
        {
            cout<<": "<<out<<" won\n";
            continue;
        }

        //대각선1
        char first=z[0][0];
        if (first=='T')
            first= z[1][1];
        int cnt=0;
        for(int i=1;i<4;i++)
        {
            if (first=='.')
                break;
            if (first == z[i][i] || z[i][i]=='T')
            {
                cnt++;
            }
        }

        if (cnt==3)
        {
            cout<<": "<<first<<" won\n";
            continue;
        }
        //대각선2
        first=z[0][3];
        
        if (first=='T')
            first= z[1][2];
        cnt=0;
        for(int i=1;i<4;i++)
        {
            if (first=='.')
                continue;    
            if (first == z[i][3-i] || z[i][3-i]=='T')
            {
                cnt++;
            }
        }
        if (cnt==3)
        {
            cout<<": "<<first<<" won\n";
        }
        else
        {
            if (!empty)
                cout <<": Draw\n";
            else
                cout << ": Game has not completed\n";
        }
    }
}