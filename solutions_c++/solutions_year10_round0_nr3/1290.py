#include<cstdio>
#include<cstring>
#include<queue>
#define cl(a)memset(a,0,sizeof(a))
#define N 1111
using namespace std;
int a[N],vis[N];
long long sum[N];
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int r,k,n;
    scanf("%d%d%d",&r,&k,&n);
    int i;
    queue<int>q;
    for(i=0;i<n;++i){scanf("%d",a+i);q.push(i);}
    cl(vis);
    cl(sum);
    for(i=1;;++i){
      if(vis[q.front()])break;
      vis[q.front()]=i;
      int tmp=0;
      queue<int>in;
      for(;;){
        if(q.empty()||tmp+a[q.front()]>k)break;
        tmp+=a[q.front()];
        in.push(q.front());
        q.pop();
      }
      sum[i]=sum[i-1]+tmp;
      while(in.size()){
        q.push(in.front());
        in.pop();
      }
    }
    int len=i-vis[q.front()];
    long long mon=sum[i-1]-sum[vis[q.front()]-1];
    //printf("len=%d mon=%I64d\n",len,mon);
    mon*=(r-vis[q.front()])/len;
    if(r>vis[q.front()])
      r=(r-vis[q.front()])%len+vis[q.front()];
    //printf("len=%d mon=%I64d\n",len,mon);
    q=queue<int>();
    for(i=0;i<n;++i)q.push(i);
    long long cnt=0;
    while(r--){
      int tmp=0;
      queue<int>in;
      for(;;){
        if(q.empty()||tmp+a[q.front()]>k)break;
        tmp+=a[q.front()];
        in.push(q.front());
        q.pop();
      }
      cnt+=tmp;
      while(in.size()){
        q.push(in.front());
        in.pop();
      }
    }
    printf("Case #%d: %I64d\n",testi,cnt+mon);
  }
  return 0;
}