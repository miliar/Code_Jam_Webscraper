#include <iostream>
#include <fstream>

using namespace std;
int num[50];
char in[50];
int t;
int n,res,sum;
int main ()
{
	//freopen ("a.in", "r", stdin);
	freopen ("b.out", "w", stdout);
	scanf ("%d", &t);

	for (int cas=1;cas<=t;cas++)
	{
		memset (num,0,sizeof (num));
		scanf ("%d", &n);

			gets (in);
		for (int i=0;i<n;i++)
		{
			gets (in);
			for (int j=0;j<n;j++)
				if (in[j]=='1')
					num[i]=j;
		}
		res=0;
		for (int i=0;i<n;i++)
		{	
			sum=0;
			for (int j=0;j<n;j++)
			{
				if (num[j]!=-1)
				{
					if (num[j]<=i)
					{	
						num[j]=-1;
						res+=sum;
						break;
					}
					else
						sum++;
				}	
			}
		}

		printf ("Case #%d: %d\n", cas, res);
	}
	return 0;
}