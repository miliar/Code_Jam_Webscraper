// Cndy1
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;



int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("small.txt", "w", stdout);
	int t, cno = 1;
	scanf("%d",&t);
	while(t--)
	{
			  int n;
			  scanf("%d",&n);
			  bool pos = false;
			  int x[n];
			  int ans = 0;
			  for(int i = 0; i < n; ++i)
			          scanf("%d",&x[i]);
			  for(int i = 1; i < (1 << n) - 1; ++i)
			  {
					 string rep = "";
					 for(int j = n - 1; j >= 0; j--)
					 {
							 if(i & (1 << j))rep += "1";
							 else rep += "0";
	  		 		 }
	  		 		 int sean = 0, patrix = 0, xsean = 0, xpatrix = 0;

	  		 		 for(int p = 0; p < n; ++p)
	  		 		 {
						if(rep[p] == '1'){sean = sean ^ x[p]; xsean += x[p];}
						else {patrix = patrix ^ x[p]; xpatrix += x[p];}
		  		 	 }
		  		 	 int m1 = max(xpatrix, xsean);
		  		 	 if(sean == patrix){if(m1 > ans)ans = m1; pos = true;}
 		  	  }
 		  	  if(!pos){printf("Case #%d: NO\n", cno++);}
 		  	  else {printf("Case #%d: %d\n", cno++, ans);}
 	}
	return 0;
}
