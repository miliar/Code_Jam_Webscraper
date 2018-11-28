#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<sstream>
#define vi vector<int>
#define vvi vector<vector<int> >
#define pii pair<int,int> 
#define vs vector<string> 
 
using namespace std;

int t,na,nb;
vector<pii> a,b;
int at[2010];
int tim[2010];
struct cmp
{
    bool operator()(pair<pii,int> _one,pair<pii,int> _two)
    {
        pii one=_one.first;
        pii two=_two.first;
        if(one.first<two.first)
        return false;
        if(one.first==two.first && one.second<two.second)
        return false;
        if(one.first>two.first)
        return true;
    }
};
int main()
{
    int tes;
    cin>>tes;
    int tesno=1;
    while(tes--)
    {
        memset(at,-1,sizeof(at));
        a.clear();
        b.clear();
        cin>>t>>na>>nb;
        int i,j,k;
        priority_queue<pair<pii,int>,vector<pair<pii,int> >,cmp> q;
        for(i=0;i<na;i++)
        {
            int w,x,y,z;
            scanf("%d:%d %d:%d",&w,&x,&y,&z);
            int t1,t2;
            t1=w*60+x;
            t2=y*60+z;
            a.push_back(make_pair(t1,t2));
            q.push(make_pair(a.back(),0));
        }
        for(i=0;i<nb;i++)
        {
            int w,x,y,z;
            scanf("%d:%d %d:%d",&w,&x,&y,&z);
            int t1,t2;
            t1=w*60+x;
            t2=y*60+z;
            b.push_back(make_pair(t1,t2));
            q.push(make_pair(b.back(),1));
        }
        /*while(!q.empty())
        {
            cout<<q.top().first.first<<" "<<q.top().first.second<<" "<<q.top().second<<endl;
            q.pop();
        }*/
        int var[2]={0};
        int count=0;
        while(!q.empty())
        {
            pair<pii,int> pp=q.top();
            int nowat=pp.second;
            pii p=pp.first;
            q.pop();
            int trno=-1;
            int mtim=10000000;
            for(i=0;i<count;i++)
            {
                if(at[i]!=nowat)continue;
                if(tim[i]>p.first)continue;
                if(mtim>tim[i])
                {
                    mtim=tim[i];
                    trno=i;
                }
            }
            if(trno==-1)
            {
                count++;    
                at[count-1]=(nowat+1)%2;
                tim[count-1]=p.second+t;
                var[nowat]++;
                continue;
            }
            at[trno]=(nowat+1)%2;
            tim[trno]=p.second+t;
        }
        cout<<"Case #"<<tesno<<": ";
        tesno++;
        cout<<var[0]<<" "<<var[1]<<endl;
    }
    return 0;
}

        
                
