#include<stdio.h>

int v[41];

int main()
{
    int N, t, i, j, nr, n, aux;
	char s[41];
	freopen("date.in", "rt", stdin);
	freopen("date.out", "wt", stdout);
	scanf("%i",&N);
    for(t=1; t<=N; t++)
	{	
		scanf("%i", &n);
		for(i=1; i<=n; i++)
		{
			scanf("%s", s);
			for(j=n-1; j>=0 && s[j]=='0'; j--);
			v[i] = j+1;
		}
		nr = 0;
		for(i=1; i<n; i++)
			if(v[i]>i)
			{
                for(j=i+1; j<=n && v[j]>i; j++);
				aux = v[j];
				nr+=j-i;
                for(; j>=i; j--) v[j] = v[j-1];
				v[i] = aux;
			}
		printf("Case #%i: %i\n", t, nr);
	}
	return 0;
}
		
			
		
	
		
