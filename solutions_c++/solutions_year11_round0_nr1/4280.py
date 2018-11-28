#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <stdio.h>
#include <math.h>
using namespace std;


//#define small
#define large


int main()
{
    #ifdef small
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-out.out","w",stdout);
    #endif
    #ifdef large
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.out","w",stdout);
    #endif

    int i,j,t;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        int n,b;
        char bot;
        scanf("%d",&n);
        vector<int> ob;
        vector<int> bb;
        string order="";

        //ob.push_back(1);
        //bb.push_back(1);

        for(j=0;j<n;j++)
        {
            cin>>bot>>b;
            order+=bot;
            if(bot=='O')
                ob.push_back(b);
            else if(bot=='B')
                bb.push_back(b);
        }
        //ob[0]=ob.back();
        //bb[0]=bb.back();
        if(ob.size()>0) reverse(ob.begin(),ob.end());
        if(bb.size()>0) reverse(bb.begin(),bb.end());

        int posb=1,poso=1,ans=0;
        bool pushb,pusho;
        for(j=0;j<order.size();)
        {
            pushb=false;
            pusho=false;
            ans++;
            if(order[j]=='O' && poso == ob.back())
                {/*printf("Orange Pushed  ");*/ ob.pop_back(); pusho=true; j++;}
            else if(order[j]=='B' && posb == bb.back())
                {/*printf("Blue Pushed  ");*/ bb.pop_back(); pushb=true; j++;}

            if(bb.size()>0 && posb!=bb.back() && pushb==false)
            {
                if(posb<bb.back()) posb++;
                else if(posb>bb.back()) posb--;
            }
            if(ob.size()>0 && poso!=ob.back() && pusho==false)
            {
                if(poso<ob.back()) poso++;
                else if(poso>ob.back()) poso--;
            }

            //printf("O %d B %d\n",poso,posb);
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
