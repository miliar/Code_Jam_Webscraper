#include <cstdio>

int n;
int a,b,c,d;

int gcd(int a, int b)
{
	if (b == 0)
		return a;
	else
		return gcd(b, a % b);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int test,testnum;
	scanf("%ld",&testnum);
	for (test = 1; test <= testnum; ++ test){
		scanf("%ld",&n);

		printf("Case #%ld: ",test);

		if (n == 2){
			scanf("%ld %ld",&a,&b);
			if (a < b)
				d = b - a;
			else
				d = a - b;  //gcd(a,b);	
		}else{
			scanf("%ld %ld %ld",&a,&b,&c);
			if (a < b)
				if (b < c)
					d = gcd(c - b, b - a);
				else if (a < c)
						  d = gcd(c - a, b - c);
					 else d = gcd(a - c, b - a);
			else
				if (a < c)
					d = gcd(c - a, a - b);
				else if (b < c)
						  d = gcd(a - c, c - b);
					 else d = gcd(a - b, b - c);
		}

		printf("%ld\n", (d - a % d) % d);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}