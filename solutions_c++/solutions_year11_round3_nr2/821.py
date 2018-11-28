#include <iostream>
using namespace std;

__int64 a[20000];
__int64 b[1001000];
__int64 c[1001000];
int lenc;

void fill(__int64 C , __int64 N)
{
	int index = 0;
	for (int i=0 ; i<N ; i++ ) {
		b[i] = a[index];
		index++;
		if (index == C)
			index = 0;
	}
}

int find(__int64 t, __int64 N)
{
	__int64 temp = 0;
	__int64 total = t / 2;
	int index = 0;
	for (int i=0 ; i<N ; i++) {
		temp += b[i];
		if (temp >=total) {
			index = 0;
			c[index++] = temp - total;
			for (int j = i + 1 ; j < N ; j++) {
				c[index++] = b[j];
			}
			lenc = index;
			return i;
		}
	}

	return -1;
}

int cmp(const void *a , const void *b)
{
	__int64 *c = (__int64 *)a;
	__int64 *d = (__int64 *)b;
	__int64 temp = *c - *d;
	if (temp < 0)
		return 1;
	else
		return -1;
}

int main()
{	
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int t;
	__int64 L , T , N , C;
	__int64 total;
	__int64 speedLength;
	__int64 ans;
	int cas = 0;
	int temp;
	
	scanf("%d" , &t);
	while (t--) {
		cas++;
		scanf("%I64d %I64d %I64d %I64d" , &L , &T , &N , &C);
		for (int i=0 ; i<C ; i++) {
			scanf("%I64d" , &a[i]);
		}
		fill(C , N);
		total = 0;
		lenc = 0;

		for (int i=0 ; i<N ; i++) {
			total += b[i];
		}

		temp = find(T , N);
		qsort(c , lenc , sizeof(c[0]) , cmp);
		
		speedLength = 0;
		for (int i=0 , j = 0 ; i<lenc && j<L ; i++ , j++) {
			speedLength += c[i];
		}	

		ans = (total - speedLength) * 2 + speedLength;
		printf("Case #%d: %I64d\n" , cas , ans);
	}

	return 0;
}
