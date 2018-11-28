#include <cstdio>

int n,k;
int a[100][100];

int main()
{
   int t;
   scanf("%d", &t);
   char c;
   for (int qq = 0; qq < t; qq++)
   {
      scanf("%d%d\n", &n, &k);
      for (int i = 0; i < n; i++)
      {
        for (int j = 0; j < n; j++)
	{
	  scanf("%c", &c);
	  if (c == '.')
	    a[i][j] = 0;
	  else if (c == 'R')
	    a[i][j] = 1;
	  else
	    a[i][j] = -1;
	}
	scanf("\n");
      }
      for (int i = 0; i < n; i++)
      {
         int j;
         for (j = n - 1; j >= 0 && a[i][j]; j--);
	 int s = j;
	 for (; j >= 0; j--)
	 {
	   if (!a[i][j]) continue;
	   a[i][s--] = a[i][j];
	   a[i][j] = 0;
	 }
      }
      bool ok1,ok2;
      ok1 = ok2 = 0;
      for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
	{
	 if (a[i][j])
	 {
	   int cnt1,cnt2,cnt3,cnt4;
	   cnt1 = cnt2 = cnt3 = cnt4 = 1;
	   for (int r = 1; i + r < n; r++)
	   {
	     if (a[i][j] == a[i + r][j])
	       cnt1++;
	     else
	       break;
	   }
	   for (int r = 1; j + r < n; r++)
	   {
	     if (a[i][j] == a[i][j + r])
	       cnt2++;
	     else
	       break;
	   }
	   for (int r = 1; j + r < n && i + r < n; r++)
	   {
	     if (a[i][j] == a[i + r][j + r])
	       cnt3++;
	     else
	       break;
	   }
	   for (int r = 1; j - r >= 0 && i + r < n; r++)
	   {
	     if (a[i][j] == a[i + r][j - r])
	       cnt4++;
	     else
	       break;
	   }
           if (cnt1 == k || cnt2 == k || cnt3 == k || cnt4 == k)
	   {
	     if (a[i][j] == 1)
	       ok1 = 1;
	     else
	       ok2 = 1;
	   }
	  }
	}
     printf("Case #%d: ", qq + 1);
     if (ok1 && ok2)
       puts("Both");
     else if (!ok1 && !ok2)
       puts("Neither");
     else if (ok1 && !ok2)
       puts("Red");
     else if (!ok1 && ok2)
       puts("Blue");
   }
   return 0;
}
