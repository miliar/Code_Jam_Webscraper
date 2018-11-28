#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
  int t,n,s,a[22],flag=0;
  int sum,num,x,y;
  int v[2000000];
  scanf("%d",&t);
  num=0;
  int i,j,yes;
  vector<int> one;
  vector<int> two;
  while(t--)
  {
    one.clear();
    two.clear();
    num++;
    scanf("%d",&n);
    s=0;
    for(i=0;i<n;i++)
    {
      scanf("%d",&a[i]);
      s+=a[i];
    }
    int *b=(int*)calloc(s+1,sizeof(int));
    b[0]=1;
    flag=0;
    for(i=0;i<n;i++)
    {
      for(j=s;j>=0;j--)
      {
	if(b[j]!=1 || j+a[i]>s)
	  continue;
	if(b[j+a[i]]==1)
	{
	  flag=1;
	  break;
	}
        else
	{
	  b[j+a[i]]=1;
	  v[j+a[i]]=a[i];
	}
      }
      if(flag==1) break;
    }
    if(flag==1)
    {
      printf("Case #%d:\n",num);
      sum=j+a[i];
      while(sum>0)
      {
	one.push_back(v[sum]);
	sum-=v[sum];
      }
      two.push_back(a[i]);
      sum=j;
      while(sum>0)
      {
	two.push_back(v[sum]);
	sum-=v[sum];
      }
      sort(one.begin(),one.end());
      sort(two.begin(),two.end());

      x=one.size();
      y=two.size();
/*      for(i=0;i<x;i++)
	printf("%d ",one[i]);
      printf("\n");
      for(i=0;i<x;i++)
	printf("%d ",two[i]);
      printf("\n");*/
      for(i=0;i<x;i++)
      {
	y=two.size();
	yes=0;
	for(j=0;j<y;j++)
	  if(one[i]==two[j])
	  {
	    yes=1;
	    two.erase(two.begin()+j);
	    break;
	  }
	if(yes==1) 
	  continue;
	else
	  printf("%d ",one[i]);
      }
      printf("\n");
      y=two.size();
      for(i=0;i<y;i++)
	printf("%d ",two[i]);
      printf("\n");
      continue;
    }
    printf("Impossible\n");
  }
  return 0;
}

