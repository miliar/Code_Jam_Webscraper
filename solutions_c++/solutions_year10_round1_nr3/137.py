#include <algorithm>

#include <cstdio>
#include <cmath>

using namespace std;

const double RATIO = 0.5 * (1.0 + sqrt(5.0));

// count the number of pairs (A,B) such that A1<=A<=A2, B1<=B<=B2, A/B>(1+sqrt(5))/2
long long count(int A1, int A2, int B1, int B2)
{
	long long res = 0;
	for (int B = B1; B <= B2; ++B)
	{
		int amin = max(A1, (int)ceil(RATIO * B));
		if (amin <= A2)
			res += A2 - amin + 1;
	}
	return res;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int idxCase = 0; idxCase < T; ++idxCase)
    {
        int A1, A2, B1, B2;
        scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
    	printf("Case #%d: %lld\n", idxCase + 1, count(A1, A2, B1, B2) + count(B1, B2, A1, A2));
    }
    return 0;
}
