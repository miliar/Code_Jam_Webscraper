#include<iostream>
using namespace std;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("C-large-output.txt", "wt", stdout);

    int t,n;
    int x, sum, min, b;

	scanf("%d", &t);
	For(test, 1, t)
    {
              cin >> n;
              sum = 0;
              min=0x7fffffff;
              b = 0;
              For(i, 0, n-1)
              {
                     cin >> x;
                     if (x < min) min = x;
                     sum += x;
                     b ^= x;
                    // printf("%d %d\n", x, b);
              }
              printf("Case #%d: ", test);
              if (b != 0) printf("NO\n");
              else printf("%d\n",sum - min);

	}

	exit(0);
}
