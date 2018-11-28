#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int n, K;
int main()
{
    int T;
    scanf("%d", &T);
    int id = 0;
    while (T --)
    {
	scanf("%d%d", &n, &K);
	printf("Case #%d: %s\n", ++id, (K & ((1 << n) - 1)) == (1 << n) - 1 ? "ON" : "OFF");
    }
    return 0;
}

