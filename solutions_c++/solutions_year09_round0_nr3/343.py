
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>
  #include <iostream>
  #include <string>
  #include <vector>
  
  using namespace std;

  string A;
  char B[505];
  int f[505][19];
  int sum[19];
  
  int main()
    {
        A = "welcome to code jam";
        //freopen("C.in", "r", stdin );
	int caseNo;
	scanf("%d\n", &caseNo);
	for (int T = 1; T <= caseNo; ++ T)
	  {
	      printf("Case #%d: ", T);
	      int n = 0;
	      char c;
	      while (1)
	        {
		   c = getchar();
		   if (c == '\n') break;
		   B[n ++] = c;
		}
	      memset(sum, 0, sizeof(sum));
	      memset(f, 0, sizeof(f));
	      for (int i = 0; i < n; ++ i)
	        for (int j = 0; j < 19; ++ j)
		  if (B[i] == A[j])
		    {
		       if (j == 0) f[i][j] = 1;
		         else f[i][j] = sum[j - 1];
		       sum[j] = (sum[j] + f[i][j]) % 10000;
		    }
	
	      printf("%d%d%d%d\n", sum[18] / 1000 % 10, sum[18] / 100 % 10, sum[18] / 10 % 10, sum[18] % 10);
	  }
	return 0;
    }