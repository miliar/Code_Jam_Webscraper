#include <stdio.h>
using namespace std;

	int main()
	{
		int a,b,t,k,j,n,s;
		int q,len,p,aux;
		int used[6];
		int no_used;
		scanf("%d",&t);
		for (int i=1;i<=t;i++)
		{
			scanf("%d %d",&a,&b);
			q = 0;
			len = 0;
			p = 1;
			aux = a;
			while (aux>0)
			{
				len++;
				p *= 10;
				aux = aux / 10;
			}
			p /= 10;
			for (k=a;k<=b;k++)
			{
				n = k;
				s = 0;
				for (j=1;j<len;j++)
				{
					n = n/10+(n%10)*p;
					if ((n<=b)&&(n>k))
					{
						s++;
						q++;
					}
					if (n==k)
					{
						q-=s;
						s = 0;
					}
				}
			}
printf("Case #%d: %d\n",i,q); 
		}
		return 0;
	}

