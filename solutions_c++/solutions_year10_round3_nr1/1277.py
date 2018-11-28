/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2010, Round 1 /
/  Sub-Round C, Task 'Rope Intranet' */
#include <cstdio>
#include <set>

#define SIZE 1010
#define P first
#define K second

using namespace std;

pair<unsigned int, unsigned int> ropes[SIZE];


int main()
{
    unsigned int j,t,n,i,result,k;
    scanf("%u",&t);
    for(j=1;j<=t;++j)
    {
	result=0;
	scanf("%u",&n);
	for(i=0;i<n;++i)
	    scanf("%u%u",&ropes[i].P,&ropes[i].K);
	    
	for(i=0;i<n;++i)
	    for(k=i+1;k<n;++k)
		if((ropes[i].P<ropes[k].P && ropes[i].K>ropes[k].K) || (ropes[i].P>ropes[k].P && ropes[i].K<ropes[k].K))
		    ++result;

	printf("Case #%u: %u\n",j,result);
    }
    return 0;
}