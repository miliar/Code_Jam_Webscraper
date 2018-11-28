#include <cstdio>

using namespace std;

int main()
{
  int kil;
  scanf("%d",&kil);
  for (int i=0; i<kil; i++)
   {
      int n;
      scanf("%d",&n);
      int r=0;
      scanf("%d",&r);
	  int sum=0;
	  int m=r;
	  for(int j=0; j<n-1; j++)
	   {
	     int t=0;
		 scanf("%d",&t);
		 r^=t;
		 if (t<m) sum+=m, m=t;
		 else sum+=t;
	   }

      if (r==0)
      {
        printf("Case #%d: %d\n",i+1,sum);
      } else printf("Case #%d: NO\n", i+1);


   }
  return 0;
}
