#include <cstdio>

const int maxn = 1000;

int r,k,n;
int g[maxn];
int tp[maxn],gmax[maxn];

inline int next(int i)
{
	if (i < n - 1)
		 return i + 1;
	else return 0;
}

void init()
{
	scanf("%ld %ld %ld",&r,&k,&n);
	int i,j,sum;
	for (i = 0; i < n; ++ i)
		scanf("%ld",&g[i]);
	// prepare
	for (i = 0; i < n; ++ i){
		j = next(i);
		sum = g[i];
		while (j != i && sum + g[j] <= k){
			sum += g[j];
			j = next(j);
		}
		gmax[i] = sum;
		tp[i] = j;
	}
}

void doit()
{
	int num;
	int j = 0;
	__int64 sum = 0;
	for (num = 0; num < r; ++ num){
		sum += gmax[j];
		j = tp[j];
	}
	printf("%I64d\n",sum);
}

int main()
{
	freopen("c-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int num,in;
	scanf("%ld",&num);
	for (in = 1; in <= num; ++ in){
		init();
		printf("Case #%ld: ",in);
		doit();
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
