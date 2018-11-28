#include<iostream>
#include<set>
using namespace std ;
#define MAXN 1000002

int tree[MAXN*22] ;
void create(int node,int low,int high)
{
 tree[node] = high - low + 1 ;    
 if(low == high) return ;
 int mid = (low + high)/2 ; 
 create(node*2,low,mid) ;
 create(node*2 + 1,mid + 1,high) ;
}

int query(int node,int low,int high,int sum)
{
 tree[node] -- ;
 if(low == high) return low ;
 int mid = (low + high)/2 ;
 if(sum < tree[2*node]) return query(node*2,low,mid,sum) ;
 return query(node*2 + 1,mid + 1,high,sum - tree[2*node]) ;
}

int arr[MAXN] ;
main()
{
 int i,j,k,n,runs ;

 freopen("a.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;

 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  scanf("%d",&n) ;
  create(1,0,n-1) ;
  int sum = 0,mod = n ;
  for(i=0;i<n;i++)
  {
   arr[query(1,0,n-1,sum)] = i + 1 ;
   if(i + 1 < n) sum = (sum + i+1)%(--mod) ;               
  }        
  
  int queries,need[105] ;
  scanf("%d",&queries) ;
  for(i=0;i<queries;i++) scanf("%d",&need[i]) ;
  printf("Case #%d:",t) ;
  for(i=0;i<queries;i++) printf(" %d",arr[need[i]-1]) ; 
  printf("\n") ;
 }
}
