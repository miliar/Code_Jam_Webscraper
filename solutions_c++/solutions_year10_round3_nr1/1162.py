#include"cstdio"
#include"algorithm"
#include"map"
#define MAX 10005
using namespace std;
int t[MAX],T2[MAX][2],x0,x1;
long long ans=0;
int number[MAX]={0},a[MAX]={0};
map<int,int>::reverse_iterator ci;
map<int,int> point1,point2;
int merge(int l1,int r1,int l2,int r2)
{
  int t1=l1,t2=l1;
  while(l1<=r1&&l2<=r2)
  {
    if(a[l1]>a[l2])
    {
      ans+=r1-l1+1;
      t[t2++]=a[l2++];
    }
    else
      t[t2++]=a[l1++];
  }
  while(r1>=l1)
    t[t2++]=a[l1++];
  while(r2>=l2)
    t[t2++]=a[l2++];
  while(r2>=t1)
    a[t1++]=t[t1];
}
int m_sort(int l1,int r1)
{
  int mid=(l1+r1)/2;
  if(r1>l1)
  {
    m_sort(l1,mid);
    m_sort(mid+1,r1);
    merge(l1,mid,mid+1,r1);
  }
}
int main()
{
  int c1,c2,t1,n,t;
  freopen("A-large.in","r",stdin);
  freopen("out","w",stdout);
  scanf("%d",&t);
  for(c2=0;t>c2;c2++,ans=0)
  {
    scanf("%d",&n);
    for(c1=0;n>c1;c1++)
      scanf("%d %d",&T2[c1][0],&T2[c1][1]);
    for(c1=0;n>c1;c1++)
    {
      point1[T2[c1][0]]=c1;
      point2[T2[c1][1]]=c1;
    }
    for(c1=0,ci=point1.rbegin();ci!=point1.rend();c1++,ci++)
      number[ci->second]=c1;
    for(c1=0,ci=point2.rbegin();ci!=point2.rend();c1++,ci++)
      a[c1]=number[ci->second];
    t1=0;
    m_sort(0,n-1);
    printf("Case #%d: %lld\n",c2+1,ans);
    point1.clear();
    point2.clear();
  }
}
