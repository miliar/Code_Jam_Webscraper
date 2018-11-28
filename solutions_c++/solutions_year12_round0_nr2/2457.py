#include <cstdio>

int T, t;
int n, s, p;
int a[200];

int solve()
{
	int i;
	int surp, unsurp;
	surp = 0;
	unsurp = 0;

	for(i = 0; i < n; ++i){
		if(a[i] <= 1){
			if(a[i] >= p)
				++unsurp;
		}
		else if(a[i] == 2){
			if(1 >= p)
				++unsurp;
			else if(2 >= p)
				++surp;
		}
		else if(a[i]%3 == 0){
			if(a[i]/3 >= p)
				++unsurp;
			else if(a[i]/3+1 >= p)
				++surp;
		}
		else if(a[i]%3 == 1){
			if(a[i]/3+1 >= p)
				++unsurp;
		}
		else{
			if(a[i]/3+1 >= p)
				++unsurp;
			else if(a[i]/3+2 >= p)
				++surp;
		}
	}

	if(surp < s)
		return unsurp+surp;
	else
		return unsurp+s;
}

main()
{
	int i;
	scanf("%d", &T);
	for(t = 0; t < T; ++t){
		scanf("%d %d %d", &n, &s ,&p);
		for(i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		printf("Case #%d: %d\n", t+1, solve());
	}
}
