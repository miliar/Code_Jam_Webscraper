#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;

#define runc true
#define DIGIT 51
#define MAXN 1001

void convert(int *arr);
bool iszero(int *a);
int mod(int *x, int *y);
int compare(int* x,int* y);
int intlen(int *x);

int base[DIGIT], other[DIGIT];
char buf[DIGIT];
int gcd[DIGIT], divide[DIGIT];

int GCD(int a, int b)
{
	if(b==0){
		return a;
	}
	else{
		return GCD(b, a % b);
	}
}

#if runc
int main()
#else
int C()
#endif
{
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int arr[MAXN];
	int sub[MAXN];
	int N;
	int cse, cnt;
	scanf("%d\n", &cse);
	for(cnt=1;cnt<=cse;cnt++){
		printf("Case #%d: " ,cnt);

		scanf("%d", &N);

		for(int i=0;i<N;i++){
			scanf("%d", &arr[i]);
			if(i>0)
				sub[i] = abs(arr[i] - arr[i-1]);
		}
		int g = sub[1];
		for(int i=2;i<N;i++){
			//printf("%d %d\n", g, sub[i]);

			g = GCD(g, sub[i]);
		}
		if (arr[0] % g){
			printf("%d\n", g - arr[0]%g);
		}
		else
			printf("0\n");
		/*
		scanf("%s", buf);
		convert(base);
		for(int i=1;i<N;i++){
			scanf("%s", buf);
			if(i&1)
				convert(other);
			else
				convert(base);

		}

		if(compare(base, other) > 0)
			mod(base, other);
		else
			mod(other, base);
		*/

	}
	return 0;
}

void convert(int *arr){
	int e = strlen(buf);
    for (int i=0;i<DIGIT;i++){
    	if(e>0)
    		arr[i] = buf[--e]-48;
    	else
    		arr[i] = 0;
    }
}

bool iszero(int *a){
    for(int i=0;i<DIGIT;i++)if(a[i]>0)return false;
    return true;
}

int intlen(int *x){
	for(int i=DIGIT-1;i>=0;i--){
		if(x[i]>0)
			return i;
	}
	return 0;
}

int mod(int *x, int *y){
	int lenx = intlen(x), leny = intlen(y), times = lenx-leny+1;
	int div[DIGIT];
	for(int i=0;i<leny;i++)
		div[i] = y[i];

	printf("%d %d\n", lenx, leny);

	for(int i=lenx, j=leny; i>=0; i--, j--){
		if(j < 0)
			div[i] = 0;
		else
			div[i] = y[j];
	}

	while(times--){

	}

	return 0;
}

int compare(int* x,int* y){
    for (int i=DIGIT-1;i>=0;i--){
        if(x[i]>y[i]){return 1;}
        if(x[i]<y[i]){return -1;}
    }
    return 0;
}
