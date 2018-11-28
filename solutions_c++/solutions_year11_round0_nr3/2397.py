#include <cstdio>
#include <algorithm>

void work(const int _)
{
    int n, a, x, z, s;
    scanf("%d%d", &n, &a);
    x = z = s = a;
    while (--n)
    {
	scanf("%d", &a);
	x ^= a;
	z = std::min(z, a);
	s += a;
    }
    printf("Case #%d: ", _);
    if (x)
	printf("NO\n");
    else
	printf("%d\n", s - z);
}

int main()
{
    int _;
    scanf("%d", &_);
    for (int i = 1; i <= _; ++i)
	work(i);
}
