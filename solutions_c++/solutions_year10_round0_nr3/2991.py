#include<iostream>
#include<fstream>
#include<stdio.h>
#include<queue>

using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR2(i,m,n) for(int i=m;i<n;i++)

int arr[16];
int R,k,N,n,cost,val,res,sz,sz1;;

int main()
{
    queue<int> myq;
    freopen("C-small-attempt1.in","rt",stdin);
    freopen("C-small.out","wt",stdout);
    cin>>n;
    for(int i=0;i<n;i++)
    {
            cost=0,res=0;
            while (!myq.empty())
                  myq.pop();
            cin>>R>>k>>N;
            for(int l=0;l<N;l++)
            {
            cin>>val;
            myq.push(val);
            }
            sz=myq.size();
            printf("Case #%d: ",(i+1));
            for(int j=0;j<R;j++)
            {
                cost=0;
                int f=0;
                sz1=sz;
                    while(sz1--)
                    {
                    val=myq.front();
                    cost=cost+val;
                    if(cost>k )
                              {
                              cost-=val;
                              goto END;
                              }
                    myq.pop();
                    myq.push(val);
                    }
              END:      res+=cost;
            }
            cout<<res<<endl;
    }
}
                           
                         
            
