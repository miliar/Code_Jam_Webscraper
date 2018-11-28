#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <cstring>
#include <stack>
using namespace std;

vector<int> ma[2];
vector<pair<int,int> >z;

int main()
{
    int T;
    scanf("%d",&T);
    for(int I=0;I<T;I++)
    {
        ma[0].clear();
        ma[1].clear();
        z.clear();
        int n;
        scanf("%d",&n);
        char c[10];
        int a;
        for(int i=0;i<n;i++)
        {
            scanf("%s%d",c,&a);
            if(c[0]=='O')
            {
                ma[0].push_back(a);
                z.push_back(make_pair(0,a));
            }
            else
            {
                ma[1].push_back(a);
                z.push_back(make_pair(1,a));
            }
        }

        //printf("%d\n",n);

        int pa,pb,pos;
        pa=pb=pos=0;

        int xa,xb;
        xa=xb=1;
        int t=0;

        while(pos<z.size())
        {
            bool ok=true;
            //printf("%d %d %d %d %d (%d,%d)%d\n",xa,xb,pa,pb,pos,ma[0][pa],ma[1][pb],t);
            if(pa<ma[0].size())
            {
                if(xa!=ma[0][pa])
                {
                    xa+=(ma[0][pa]-xa)/abs(ma[0][pa]-xa);
                }else
                {
                    if(z[pos].first==0 && ok)
                    {
                        ok=false;
                        pos++;
                        pa++;
                    }
                }
            }
            if(pb<ma[1].size())
            {
                if(xb!=ma[1][pb])
                {
                    xb+=(ma[1][pb]-xb)/abs(ma[1][pb]-xb);
                }else
                {
                    if(z[pos].first==1 && ok)
                    {
                        ok=false;
                        pos++;
                        pb++;
                    }
                }
            }
            t++;
        }

        printf("Case #%d: %d\n",I+1,t);
    }
}