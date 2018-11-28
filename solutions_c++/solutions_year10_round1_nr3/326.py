#include <cstdio>

bool win(int a, int b)
{
	int t;
	if (b > a){
		t = a;
		a = b;
		b = t;
	}
	if (b <= 0)
		return true;
	t = a / b;
	if (t > 1)
		return true;
	else{
		if (win(b,a - b))
			return false;
		else
			return true;
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int test,testnum;
	int a1,a2,b1,b2;
	int i,j,sum;

	scanf("%ld",&testnum);
	for (test = 1; test <= testnum; ++ test){
		printf("Case #%ld: ",test);
		
		scanf("%ld %ld %ld %ld",&a1,&a2,&b1,&b2);
		sum = 0;
		for (i = a1; i <= a2; ++ i)
			for (j = b1; j <= b2; ++ j)
				if (win(i,j)){
					//printf("\n%ld %ld",i,j);
					++sum;
				}

		printf("%ld\n",sum);
	}
	return 0;
}
