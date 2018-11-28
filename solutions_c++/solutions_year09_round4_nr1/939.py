
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

using namespace std;
int m, n;
char a[100][100];
int v[100];
int r[100];
int main()
{
   int k, t, i, j, tests;
   scanf("%d",&tests);
   for (int cases = 0; cases < tests; cases++) 
   {
   	printf("Case #%d: ",cases+1);
	scanf("%d",&t);
	for (i = 0; i < t; i++) 
	{
	   v[i] = 0;
	   r[i] = 0;
	   for (j = 0; j < t; j++) 
	   {
	      scanf(" %c",a[i]+j);
	      if(a[i][j] == '1') v[i] = j;
	   }
	   r[i] = v[i] - i;
//	   printf("%d\n",r[i]);
	}
	int ans = 0;
	for(i = 0; i < t; i++)
	{
	   if(v[i] > i)
	   {
	      for(j = i+1; j < t;j++)
	      {
		 if ( v[j] <= i ) 
		 {
		    for(k = j ; k > i; k --)
		    {
		       swap(v[k],v[k-1]);
		       ans++;
		    }

		    break;
		 }
	      }
	   }
	}
	printf("%d\n",ans);

   }
   return 0;
}
