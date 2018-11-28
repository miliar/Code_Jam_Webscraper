/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2010 /
/  Qualification Round, Task 'Snapper Chain' */
#include <cstdio>

using namespace std;

int main()
{
    unsigned int t,n,k,i,bitmask,j;
    scanf("%u",&t);
    for(i=1;i<=t;++i)
    {
	scanf("%u%u",&n,&k);
	bitmask=0;
	for(j=1;j<=n;++j)
	{
	    bitmask=bitmask<<1;
	    bitmask++;	//we're setting the bitmask to 1111...11 (length=n)
	}
	++bitmask;	//the moment when it's 000...000 (n)
	if(k%bitmask==bitmask-1)
	    printf("Case #%u: ON\n",i);
	else
	    printf("Case #%u: OFF\n",i);
    }
    return 0;
}
