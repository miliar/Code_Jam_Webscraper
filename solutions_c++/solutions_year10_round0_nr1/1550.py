#include <iostream>
#include <fstream>

using namespace std;
int a,b;
int main ()
{
	freopen ("input", "r", stdin);
	freopen ("output", "w", stdout);
	int cases;
	scanf ("%d", &cases);
	for (int i=1;i<=cases;i++)
	{

		scanf ("%d%d", &a, &b);
		a=1<<(a);
		printf ("Case #%d: ",i);
		if (b%a==a-1) printf ("ON\n");
		else printf ("OFF\n");
	}
	
}
