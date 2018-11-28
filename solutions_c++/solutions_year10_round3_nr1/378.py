


#include<stdio.h>
#include<memory.h>
#include <iostream>
#include <string.h>
using namespace std;

const int MAX = 10004;
int a[MAX],b[MAX];
int res;
struct NODE
{
	int a;
	int b;
	int index;
}data[MAX];

void merge(int begin,int mid,int end)
{
 int i,j,k = 0;
 for(i = begin,j = mid+1; i <= mid && j <= end; k++){
  if(a[i] <= a[j])
   b[k] = a[i++];
  else {
   b[k] = a[j++];
   res += mid+1-i;
  }
 }
 for(; i <= mid; i++)
  b[k++] = a[i];
 for(; j <= end; j++)
  b[k++] = a[j];
 for(i = 0; i < k; i++)
  a[begin+i] = b[i];
}

void msort(int s, int t)
{
 if(s < t){
  int m = (s+t)>>1;
  msort(s,m);
  msort(m+1,t);
  merge(s,m,t);
 }
}

int cmp(const void *a, const void *b)
{
	NODE *da = (NODE*)a;
	NODE *db = (NODE*)b;
	if( da->a != db->a )
		return da->a - db->a;
	else return da->b - db->b;
}
int cmp2(const void *a, const void *b)
{
	NODE *da = (NODE*)a;
	NODE *db = (NODE*)b;
	if( da->b != db->b )
		return da->b - db->b;
	else return da->a - db->a;
}

int main()
{
    int t,ncase;
    t = ncase = 0;
	freopen( "A-large.in", "r", stdin);
	freopen( "A-large.out", "w", stdout);
    scanf( "%d",&ncase );
    while( ncase-- )
    {
		t++;
		res=0;
		int n;
		scanf("%d",&n);
		for( int i=0;i<n;i++ )
			scanf("%d %d",&data[i].a,&data[i].b);
		qsort( data, n, sizeof(data[0]),cmp );
		for( int i = 0 ; i < n ; i++ )
			data[i].index = i+1;
		qsort(data, n, sizeof(data[0]),cmp2);
		for(int i=0;i<n;i++)		
			a[i] = data[i].index;
		msort(0,n-1);
		printf("Case #%d: %d\n",t,res);
    }
    return 0;
}
