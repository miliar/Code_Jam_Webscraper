#include <iostream>
using namespace std;

int main () 
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

int t,k,x,n;
int q=0;
scanf("%d",&t);
	while(t--) {
		scanf("%d%d",&n,&k);
		q++;
		
	int x=(1<<n)-1;
        if((k&x)==x)
           printf("%s%d%s\n", "Case #",q,": ON");
		    else
            printf("%s%d%s\n", "Case #",q,": OFF");
		}		
	return 0;
 }
