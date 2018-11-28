#include<iostream>
using namespace std;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)

int main()
{
    freopen("D-large.in", "rt", stdin);
	freopen("D-large-output.txt", "wt", stdout);

    int t, n, x, num, ans;
    int a[1001], v[1001];
    
    memset(a,0,sizeof(a));

	scanf("%d", &t);
	For(test, 1, t)
    {
              scanf("%d", &n);
              ans = 0;
              memset(v, 0, sizeof(v));
              For(i, 1, n) scanf("%d", &a[i]);
              For(i, 1, n)
              if(v[i] == 0)
              {
                     x = i;
                     num = 0;
                     while(v[x] == 0)
                     {
                              v[x] = 1; //printf("%d,%d ", x, v[x]);
                              num++;
                              x = a[x];
                     }
                     if (num ==1) num = 0;
                     ans += num;
                     //printf("Num: %d, Ans: %d \n", num,ans);
              }
              printf("Case #%d: %.6f\n", test, ans+0.0);
	}

	exit(0);
}
