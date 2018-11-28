#include<stdio.h>
#include<conio.h>

int main()
{
	
	int x, T,a[1000],b[1000],n,i,j,A,B,c;
	
	FILE * ifp=fopen("A-large.in","r");
	FILE * ofp=fopen("A-large.out","w");
	
	fscanf(ifp,"%d\n",&T);
	for (x=1;x<=T;x++)
	{
		fscanf(ifp,"%d\n",&n);
		c=0;
		for(i=0;i<n;i++)
		{
			fscanf(ifp,"%d %d\n",&A,&B);
			for(j=0;j<i;j++)
			{
				if(A>a[j] && B < b[j])
					c++;
				if(A<a[j] && B > b[j])
					c++;
			}

			a[i] = A;
			b[i] = B;
			
		}
		fprintf(ofp,"Case #%d: %d\n",x,c);

	}

	fclose(ifp);
	fclose(ofp);
	return 0;
	
}
