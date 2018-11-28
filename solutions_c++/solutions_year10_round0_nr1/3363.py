#include <iostream>

using namespace std;

int n,k,t,nt,ok,n2;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	nt=t;
for (; nt>0; nt--)
{
	cin >> n >> k;
	n2=1;
	ok=0;
	for (int i=0; i<n; i++)
		n2+=n2;
	if ((k+1)%(n2)==0) ok=1;
	
	
	printf ("Case #%d: ",t-nt+1);
	if (ok) printf( "ON\n");
	else printf("OFF\n");
}
	return 0;
}