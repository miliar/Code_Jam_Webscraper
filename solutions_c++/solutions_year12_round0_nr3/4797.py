#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
bool isrec(int a, int b)
{
    char astr[10], bstr[10];
    sprintf(astr, "%d", a);
    sprintf(bstr, "%d", b);
    int lena = strlen(astr);
    int lenb = strlen(bstr);
    if(lena != lenb)
	return false;
    int ten = pow(10, lena - 1);

    for(int i=0; i<lenb; i++)
    {
	b = (b%10)*ten + (b/10);
	if(a == b)
	    return true;
    }
    return false;
}
int main()
{
    int I, t, a, b, count;
    scanf("%d", &t);
    for(I = 1; I <= t; I++)
    {
	scanf("%d %d", &a, &b);
	count = 0;
	for(int n = a; n <= b; n ++)
	    for(int m = n + 1; m <= b; m ++)
	    {
		if(isrec(n,m))
		    count ++;
	    }

	printf("Case #%d: %d\n", I, count);
    }
    return 0;
}
