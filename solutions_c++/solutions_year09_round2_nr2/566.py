#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#define f(i, n) for(int i = 0; i < n; i++)
#define s(n) scanf("%d", &n)
#define sc(n) scanf("%s", &n)
#define fill(a, v) memset(a, v, sizeof a)
#define inf (int)1e9
using namespace std;

int n, dig, zz = 1;
char a[30];

    bool nextPermutation(char a[])
	{
		int i, j;
		for(i = dig - 1; i >= 0; i--)
			if(a[i] < a[i + 1]) break;
		if(i < 0)
			return false;
		
		for(j = dig; j > i; j--)
			if(a[i] < a[j]) break;
		
		char temp = a[i];
		a[i] = a[j];
		a[j] = temp;
		
		for(j = dig + 1; ++i < --j;)
		{
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
		}
		return true;
	}

main()
{
	int t;
    s(t);
    
    while(t--)
    {
          printf("Case #%d: ", zz++);
          sc(a);
          //ut << a << endl;
          dig = strlen(a);
          int temp = n;
          //r(int i = dig; i >= 0; i--) {a[i] = n % 10; n /= 10;}
          n = temp;
          bool bb = next_permutation(a, a + dig);
          if(bb)
          {
              printf("%s\n", a);
          }
          else
          {
              int p = 0, pp = 0;
              sort(a, a + p);
              //ut << a << endl;
              while(a[p] == '0') p++;
              char temp = a[p];
              a[p] = a[0];
              a[0] = temp; 
              string ans = "";
              ans.push_back(a[0]);
              ans.push_back('0');
              for(int i = 1; i < dig; i++) ans.push_back(a[i]);
              cout << ans << endl;
          }
    }
}
