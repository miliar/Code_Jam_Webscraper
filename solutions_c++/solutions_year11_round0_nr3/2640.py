#include <cstdio>

#include <string>
#include <numeric>
#include <algorithm>

using namespace std;

const int MAX_N = 1024;

int N;
int data[MAX_N];

void read_input()
{
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &data[i]);
}

string solve()
{
	int xor = 0;
	for (int i = 0; i < N; i++)
		xor ^= data[i];
	if (xor != 0)
		return "NO";

	char output[1024];
	sprintf(output, "%d", accumulate(data, data+N, 0) - *min_element(data, data+N));
	return output;
}

int main()
{
//	freopen("C-small-attempt0.in", "rt", stdin);
//	freopen("C-small-attempt0.out", "w", stdout);

	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "w", stdout);

//	freopen("input.txt", "rt", stdin);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 0; iTest < nTest; iTest++) {
		read_input();
		printf("Case #%d: %s\n", iTest+1, solve().c_str());
	}
	return 0;
}
