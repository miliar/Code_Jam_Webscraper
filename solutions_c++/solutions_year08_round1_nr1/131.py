#include<iostream>
using namespace std;
int n;
int mi;
int a[10];
int b[10];
void DFS(int dep)
{
  if(dep==n)
  {
    int temp=0;
    for(int i=0;i<n;i++)
    {
      temp+=a[i]*b[i];
    }
    if(temp<mi) mi=temp;
    return ;
  }
  for(int i=dep;i<n;i++)
  {
    swap(a[i],a[dep]);
    DFS(dep+1);
    swap(a[i],a[dep]);
  }  
}

int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int t;
  int line=0;
  scanf("%d",&t);
  while(t--)
  {
    scanf("%d",&n);
    for(int i=0;i<n;i++)
      scanf("%d ",&a[i]);
    for(int i=0;i<n;i++)
      scanf("%d",&b[i]);
    mi=999999999;  
    DFS(0);    
    printf("Case #%d: %d\n",++line,mi);
  }
}


