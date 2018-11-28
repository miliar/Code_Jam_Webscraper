#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

vector<int> to,tb;

int main()
{
    int t,q,i,j,n,m,res,plb,plo,pos,tmp;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    char c;
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>n;
        plb=1;
        plo=1;
        to.clear();
        tb.clear();
        res=0;
        for (i=0;i<n;i++)
        {
            cin>>c>>pos;
            if (c=='O')
            {
               tmp=abs((double)pos-plo)+1;
               if (to.size()>0)
                 tmp+=to[to.size()-1];
               if (tb.size()>0 && tb[tb.size()-1]+1>tmp)
                 tmp=tb[tb.size()-1]+1;
               to.push_back(tmp);
               plo=pos;
            }
            else
            {
                tmp=abs((double)pos-plb)+1;
                if (tb.size()>0)
                 tmp+=tb[tb.size()-1];
               if (to.size()>0 && to[to.size()-1]+1>tmp)
                 tmp=to[to.size()-1]+1;
               tb.push_back(tmp);
               plb=pos;
            }
        }
        /*for (i=0;i<to.size();i++)
          cout<<to[i]<<" ";
        cout<<endl;
        for (i=0;i<tb.size();i++)
          cout<<tb[i]<<" ";
        cout<<endl;*/
        if (!to.empty())
          res=to[to.size()-1];
        if (!tb.empty())
           res=max(res,tb[tb.size()-1]);
         printf("Case #%d: %d\n",q+1,res);
    }
    return 0;
}
