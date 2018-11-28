#include<iostream>
using namespace std;
int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	
	int n, i, a, b, j;
	scanf("%d", &n);
	
	for(i=0;i<n;i++)
	{
        scanf(" %d %d", &a, &b);
        
		printf("Case #%d: ", i+1);
		for(j=0;j<a;j++)
		{
			if(!(b&1))
			    break;

			b >>= 1;
		}
		if(j==a)
		    printf("ON");
		else
		    printf("OFF");
		printf("\n");
	}

}
