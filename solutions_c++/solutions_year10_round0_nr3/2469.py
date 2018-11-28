#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<set>
#include<queue>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<functional>
const int INF=(1<<31)-1;
const double EPS=1e-8;
using namespace std;
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int t,r,k,n,x,ca=1;
    cin>>t;
    while(t--)
    {
       scanf("%d%d%d",&r,&k,&n);  
       queue<int>q;
       for(int i=0;i<n;i++)
       {
         scanf("%d",&x);
         q.push(x);
       }
       __int64 sum=0;
       int s[1010];
       int len;
       for(int i=0;i<r;i++)
       {
         __int64 temp=0;
         len=0;
         while(!q.empty()&&temp+q.front()<=k)
         {
             int steven=q.front();
             q.pop();       
             temp+=steven;
             //q.push(steven);          
             //sum+=temp;
             s[len++]=steven;          
         }
         for(int j=0;j<len;j++)
          q.push(s[j]);
         sum+=temp;                       
       }  
       cout<<"Case #"<<ca++<<": "<<sum<<endl;                    
    }
    //system("pause");
    return 0;
}
