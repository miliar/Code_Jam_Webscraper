#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define M 810

long long A[M],B[M];

int n;

void read_data()
{
	scanf("%d",&n);
	int i;
	for (i=1;i<=n;i++) scanf("%I64d",&A[i]);
	for (i=1;i<=n;i++) scanf("%I64d",&B[i]);
}

void work_ans()
{
	sort(A + 1,A + n + 1);
	sort(B + 1,B + n + 1);
	reverse(B + 1,B + n + 1);
	int i;
	long long minans = 0;
	for (i=1;i<=n;i++) minans += A[i] * B[i];
	printf("%I64d\n",minans);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,i;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		read_data();
		printf("Case #%d: ",i);
		work_ans();
	}
	return 0;
}
