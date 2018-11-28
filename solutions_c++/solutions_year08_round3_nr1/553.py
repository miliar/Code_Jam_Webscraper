#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

#define PI 3.142857142857142857142857
int cases;
long long res;
//long long res;


//void sortlh(long long *a, int sz)
void sorthl(long *a, long sz)
{
	long temp;
	//long long temp;

	for( int i=0;i<sz-1;i++)
	{
		for(int j=i+1; j<sz;j++)
		{
			if(a[i]<a[j])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
}

//void sortlh(long long *a, int sz)
void sortlh(int *a, int sz)
{
	int temp;
	//long long temp;

	for( int i=0;i<sz-1;i++)
	{
		for(int j=i+1; j<sz;j++)
		{
			if(a[i]>a[j])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
}

int main(int argc, char **argv)
{
long num, maxl, nkey, alph;
long fr[1002];

    freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	scanf("%d",&cases);
	for(int N=1; N<=cases; N++)
	{
		maxl=0;
		nkey=0;
		alph=0;
		res=0;

		scanf("%ld%ld%ld",&maxl,&nkey,&alph);
		for(int i=0;i<alph;i++)
		{
				scanf("%ld",&fr[i]);
					
		}

		sorthl(fr,alph);

		int k=0;
		for(int j=1;j<=maxl;j++)
		{
			for(int i=0;i<nkey;i++)
			{
				res+=fr[k]*j;
				k++;
				if(k==alph)break;
			}
			if(k==alph)break;
		}

		printf("Case #%d: %lld\n",N,res);
		//getch();

	}

	return 0;

}


