#include <iostream>
#include <cstdio>
#include <deque>
using namespace std;
deque<int> q;
int main(){
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int test,cas,r,k,n,i,tmp,cnt,t,ans;
    scanf("%d",&test);
    for( cas=1; cas<=test; cas++){
         scanf("%d%d%d",&r,&k,&n);
         q.clear();
         for( i=0; i<n; i++){
              scanf("%d",&tmp);
              q.push_back(tmp);
         }
         ans=0;
         while( r-- ){
                tmp=cnt=0;
                while( true ){
                       t=q.front();cnt++;
                       if( tmp+t>k || cnt>n ) break;
                       tmp+=t;
                       q.pop_front();
                       q.push_back(t);
                }
                ans+=tmp;
         }
         printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
              
