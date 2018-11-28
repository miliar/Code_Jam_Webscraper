#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;


char a[22];

int main()
{
    freopen("b.in", "r",stdin);
    
    freopen("b.out","w",stdout);

    int T;
    scanf("%d\n", &T);

    for(int t = 1; t <= T; ++t)
    {
	scanf("%s\n", &a);

	int nn = strlen(a);

	char b[22];
	for(int i = 0; i < nn; ++i) b[i] = a[i];

    	int p = next_permutation(b, b+nn);



	printf("Case #%d: ",t);

	if(p == 0)
	{
	    sort(a,a+nn);
	    int mn = 10, pp = -1;

	    for(int i =0; i < nn; ++i)
		if(a[i] != '0')
		if(a[i] - '0' < mn) mn = a[i]-'0', pp = i;

	    if(pp != -1)
	    {
	    char c = a[0];
	    a[0] = a[pp];
	    a[pp] = c;
	    }
	    printf("%c", a[0]);
	    printf("0");
	    for(int i = 1; i < nn; ++i)
		printf("%c", a[i]);
	    printf("\n");
	}
	else
	{
	    next_permutation(a, a+nn);
	    printf("%s\n", a);
	}
	    
//	printf("Case #%d: %s\n", t,a);

    }



    return 0;;
}
