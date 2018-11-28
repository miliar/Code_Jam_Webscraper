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

using namespace std;

int main()
{
    //freopen("inp.txt","r",stdin);
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt1.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,cs,n,r,c,i,j,k;
    int x[]={1,0,1}, y[]={0,1,1};
    vector <string> inp;
    cin>>cases;
    for(cs=1;cs<=cases;cs++)
    {
        cin>>r>>c;
        inp.resize(r);
        for(i=0;i<r;i++)
            cin>>inp[i];
        int flag=0;
        for(i=0;i<r && flag!=1;i++)
        {
            for(j=0;j<c && flag!=1;j++)
            {
                int count=0;
                if(inp[i][j]=='#')
                {
                    for(k=0;k<3;k++)
                    {
                        if(i+x[k]<r && j+y[k]<c && inp[i+x[k]][j+y[k]]=='#')
                            count++;
                    }
                    if(count==3)
                    {
                        inp[i][j]='/';
                        inp[i+1][j]='\\';
                        inp[i][j+1]='\\';
                        inp[i+1][j+1]='/';
                    }
                    else
                    {
                        flag=1;
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<cs<<":\n";
        if(flag==0)
        {
            for(i=0;i<r;i++)
                cout<<inp[i]<<endl;
        }
        else cout<<"Impossible\n";
    }
    return 0;
}
