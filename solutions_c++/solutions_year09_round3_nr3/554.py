#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<algorithm>
#include<functional>
#include<utility>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdio>
#include<ctime>
#include<string>
using namespace std;


int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	int i,j,kth=1;
	while(t--)
	{ 
	 int p,q;
	 int i,j;
	 int d[101];
	 int r[5];
	 scanf("%d %d",&p,&q);
	 for(i=0;i<q;i++)
	 {
        scanf("%d",&r[i]);
	 }
     
	 int re=1000000000;
    do        
    {
      memset(d,0,sizeof(d));
		int sum=0;
      for(i=0;i<q;i++)
	  {
		  int z=r[i];
          d[z]=1;
		  for(j=z+1;j<=p;j++)
			  if(d[j]==0)
                 sum++;
			  else
				  break;
		  for(j=z-1;j>0;j--)
              if(d[j]==0)
                 sum++;
			  else
				  break;
	  }
       if(sum<re)
		   re=sum;

    } while ( next_permutation(r,r+q));

	  printf("Case #%d: %d\n",kth++,re);
	} 
	return 0;
}

