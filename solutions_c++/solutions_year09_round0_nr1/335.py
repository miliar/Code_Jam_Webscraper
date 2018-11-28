
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>
  #include <iostream>
  #include <string>
  #include <vector>
  
  using namespace std;
  
  int dict[5005][15];
  int able[15][26];
  char S[1000];
  int L, D, N;
  
  int main()
    {
        freopen( "A.in", "r", stdin );
	  scanf("%d%d%d", &L, &D, &N);
	  for (int i = 0; i < D; ++ i)
	    for (int j = 0; j < L; ++ j)
	      {
	         char c;
		 while (1)
		   {
		      c = getchar();
		      if (c >= 'a' && c <= 'z') break;
		   }
		 dict[i][j] = c - 'a';
		 //printf("%d", dict[i][j]);
		 //if (j == L - 1) printf("\n");
	      }
	      
	  for (int i = 0; i < N; ++ i)
	    {
	       scanf("%s", &S);
	       memset(able, 0, sizeof(able));
	       int pos = 0;
	       for (int j = 0; j < L; ++ j)
	         {
		    if (S[pos] == '(')
		      {
		        while (1)
			  {
			     ++ pos;
			     if (S[pos] == ')') break;
			     able[j][S[pos] - 'a'] = 1;
			  }
		      } else
		      {
		         able[j][S[pos] - 'a'] = 1;
		      }
		    ++ pos;
		 }
		 
	       /*for (int j = 0; j < L; ++ j)
	         for (int k = 0; k < 3; ++ k)
		   {
		     printf("%d", able[j][k]);
		     if (k == 2) printf("\n");
		   }*/
		   
	       printf("Case #%d: ", i + 1);
	       int ret = 0;
	       for (int j = 0; j < D; ++ j)
	         { 
		    int OK = 1;
		    for (int k = 0; k < L; ++ k)
		      if (!able[k][dict[j][k]]) { OK = 0; break; }
		    ret += OK;
		 }
	       printf("%d\n", ret);
	    }
	    
	return 0;
    }
    