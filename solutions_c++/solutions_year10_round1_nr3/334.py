#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

bool ask(int a,int b)
{
    vector<int> r;
    if(a<b)
    {
        swap(a,b);
    }
    while(b!=0)
    {
        r.push_back(a/b);
        a=a%b;
        swap(a,b);
    }
    bool state = true;
    while(!r.empty())
    {
        if(state==false)
        {
            state = true;
            r.pop_back();
        }
        else if(state==true)
        {
            if(r.back()==1)
                state = false;
            r.pop_back();
        }
    }
    return state;
}

map<pair<int,int>,bool> mem;

bool ask2(int a,int b)
{
    if(a<b)
        swap(a,b);
    if(mem.find(make_pair(a,b))!=mem.end())
        return mem[make_pair(a,b)];
    if(a<=0 || b<=0)
        return true;
    for(int k=1;k<=(a/b);k++)
        if(ask2(a-k*b,b)==false)
            return mem[make_pair(a,b)]=true;
    return mem[make_pair(a,b)]=false;
    
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int a1,a2,b1,b2;
        scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
        int ans=0;
        for(int a=a1;a<=a2;a++)
            for(int b=b1;b<=b2;b++)
            {
                ans += ask(a,b);
//                if(ask(a,b)!=ask2(a,b))
//                printf("%d %d -> %s\n",a,b,ask2(a,b)?"YES":"NO");
            }
        printf("Case #%d: %d\n",i,ans);
    }
}
