#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>

int q[45];


int main(int argc, char **argv)
{
	if (argc<=1) {printf("test\n\n"); return 0;}

//	FILE *input=fopen(argv[1], "rt");
	freopen (argv[1], "r", stdin);

	freopen ("output","wt",stdout);

	int N=0;
//	std::cin >> N;

	scanf("%d\n", &N);

	long long int i,j,k,l,m,n,o,p,h, flag;

	long long int r,t,y,u, ans;

	for (i=0; i<N;i++)
	{
	    j=0;
	    do
		{
			q[j++]=getc(stdin);
		}
	    while (q[j-1]>40);
	    j--;
//		printf("%d ", j);
	    
	    for (k=0;k<j;k++)	{q[k]-=48;}

 	    ans=0;
	
		r=1;
	    for (k=0;k<j-1;k++) r*=3;

	    l=0;
	
 	    for (k=0;k<r;k++)
		{
		m=0;
		l=q[0];
		h=k;
		flag=1;                               //+
		   for (p=1;p<j;p++)
			{
	        		o=h%3;
				h=h/3;
				if (o==0) l=l*10+((long long int)q[p]);
				if (o==1) {m+=flag*l; l=q[p]; flag=1;  }
				if (o==2) {m+=flag*l; l=q[p]; flag=-1; }
			}
		m+=flag*l;
		if (m<0) m=-m;
		if (m%2 == 0 || m%3==0 || m%5==0 || m%7==0)	ans++;
//		printf("%d %d\n", m, ans);

		}
		printf("Case #%d: ", i+1);
		std::cout << ans << std::endl;

	}

	fclose(stdout);
	fclose(stdin);

}

