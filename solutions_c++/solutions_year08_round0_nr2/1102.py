#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

class train
{
public:
    char site;
    int time;

    train(char s,int t)
    {
        site=s;
        time=t;
    }

    bool operator<(const train& rhs) const
    {
        return time<rhs.time;
    }
};

int main()
{
    vector<train> a,b;
    int n,t,na,nb;
    int h,m,start,end;
    int ans_a,ans_b;
    int add=1;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        a.clear();
        b.clear();
        ans_a=ans_b=0;
        scanf("%d%d%d",&t,&na,&nb);
        for(int j=0;j<na;j++)
        {
            scanf("%d:%d",&h,&m);
            start=h*60+m;
            scanf("%d:%d",&h,&m);
            end=h*60+m;
            a.insert(a.end(),train('a',start));
            b.insert(b.end(),train('a',end+t));
        }
        for(int j=0;j<nb;j++)
        {
            scanf("%d:%d",&h,&m);
            start=h*60+m;
            scanf("%d:%d",&h,&m);
            end=h*60+m;
            a.insert(a.begin(),train('b',end+t));
            b.insert(b.end(),train('b',start));
        }
        stable_sort(a.begin(),a.end());
        stable_sort(b.begin(),b.end());
        add=0;
        for(vector<train>::iterator it=a.begin();it!=a.end();it++)
        {
            if(it->site=='a' && add==0) ans_a++;
            else if(it->site=='b') add++;
            else add--;
        }
        add=0;
        for(vector<train>::iterator it=b.begin();it!=b.end();it++)
        {
            if(it->site=='b' && add==0) ans_b++;
            else if(it->site=='a') add++;
            else add--;
        }
        printf("Case #%d: %d %d\n",i,ans_a,ans_b);
    }
    return 0;
}
