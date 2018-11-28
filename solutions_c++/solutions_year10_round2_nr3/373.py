#include <cstdio>


int ret,N,rank[35],a[35],Ret[105];
inline bool check()
{
int i=N;
for (;i>1;i=rank[i]);
return i==1;
}
inline void dfs(int dep,int len)
{
if (dep>N)
{
ret+=check();
return;
}
a[len]=dep;
rank[dep]=len;
dfs(dep+1,len+1);
a[len]=rank[dep]=0;
dfs(dep+1,len);
}
int main()
{
freopen("C.in","r",stdin);
freopen("C.out","w",stdout);
for (int i=2;i<=25;++i)
{
N=i;ret=0;
dfs(2,1);
Ret[i]=ret%100003;
}
int Test;
scanf("%d",&Test);
for (int Te=1;Te<=Test;++Te)
{
scanf("%d",&N);
printf("Case #%d: %d\n",Te,Ret[N]);
}
return 0;
}
