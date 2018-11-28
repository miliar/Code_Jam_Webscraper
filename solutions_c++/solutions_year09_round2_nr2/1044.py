
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>
#include<sstream>
#include<iostream>
#include<queue>
#include<set>
#include<map>

using namespace std;

#define clr(i,n) memset(i,n,sizeof(i))
#define fo(i,a) for(i=0;i<a;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define sz size()

typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
    freopen( "B-large.in" , "r" , stdin );
    freopen( "B-large.out" , "w" , stdout );
    int T,p=0;
    scanf("%d",&T);
    while(T--)
    {
        p++;
        char c[55];
        scanf("%s",&c);
        string h=c;
        int i;
        for(i=0;i<h.sz-1;i++)
            if(h[i]<h[i+1])break;
        printf("Case #%d: ",p);
        if(i==h.sz-1)
        {
            int k;
            sort(h.begin(),h.end());
            for(int j=0;j<h.sz;j++)if(h[j]!='0'){k=j;break;}
            printf("%c",h[k]);
            printf("0");
            h.erase(k,1);
            printf("%s\n",h.c_str());
        }
        else
        {
            i=h.sz-1;
            while(i>=1 && h[i-1]>=h[i])
            {
                i--;
            }
            //printf("done");
            //printf("done");
            string g=h.substr(i,h.sz-i);
            sort(g.begin(),g.end());
            int k=0;
            for(int j=0;j<g.sz;j++)if(g[j]>h[i-1]){k=j;break;}
            printf("%s",h.substr(0,i-1).c_str());
            printf("%c",g[k]);
            g.erase(k,1);
            g+=h[i-1];
            sort(g.begin(),g.end());
            printf("%s\n",g.c_str());
        }
    }
    return 0;
}






























