#include <iostream>
#include <string.h>
using namespace std;
const int MAXN = 1008;
int A[MAXN];
int B[MAXN];
int T, N, ans;
int i, j, cas;

bool ju(int x, int y)
{
	if ((A[x] > A[y]) && (B[x] < B[y]))
		{
		return true;
		}
	if ((A[x] < A[y]) && (B[x] > B[y]))
		{
		return true;
		}
	return false;
}

int main()
{
	cin>>T;
	for (cas = 1; cas <= T; cas++)
		{
		ans = 0;
		cin>>N;
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		for (i = 0; i < N; i++)
			{
			cin>>A[i]>>B[i];
			}
		for (i = 0; i < N; i++)
			{
			for (j = i + 1; j < N; j++)
				{
				if (ju(i, j))
					{
					ans++;
					}
				}
			}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
		}
}

