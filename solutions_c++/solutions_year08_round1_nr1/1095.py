#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;

#ifdef WIN32
typedef __int64 i64;
#else
typedef long long i64;
#endif

i64 sum;

bool les(long a,long b)
{
	return abs(a)<=abs(b);
}


long Noftest;
long nn;
long A1[1000];
long A2[1000];
long B1[1000];
long B2[1000];
long na1;
long na2;
long nb1;
long nb2;
int main()
{
	FILE* fp2;
	fp2=fopen("test.out","w");
	cin>>Noftest;
	
	long i;
	for(i=0;i<Noftest;i++)
	{
		cin>>nn;
		na1=0;na2=0;
		long temp;
		long j;
		for(j=0;j<nn;j++)
		{
			cin>>temp;
			if(temp<=0)
			{
				A1[na1]=temp;na1++;
			}
			else
			{
				A2[na2]=temp;na2++;
			}
		}
		nb1=0;nb2=0;
		for(j=0;j<nn;j++)
		{
			cin>>temp;
			if(temp<=0)
			{
				B2[nb2]=temp;nb2++;
			}
			else
			{
				B1[nb1]=temp;nb1++;
			}
		}
		sort(&A1[0],&A1[na1],les);
		sort(&A2[0],&A2[na2],les);
		sort(&B1[0],&B1[nb1],les);
		sort(&B2[0],&B2[nb2],les);

		sum=0;
		while(na1!=0&&nb1!=0)
		{
			sum+=A1[na1-1]*B1[nb1-1];
			na1--;nb1--;
		}
		while(na2!=0&&nb2!=0)
		{
			sum+=A2[na2-1]*B2[nb2-1];
			na2--;nb2--;
		}
		if(0==na1)
		{
			int ii;
			
			for(ii=0;ii<nb1;ii++)
			{
				sum+=B1[ii]*A2[na2-1-ii];
			}
		}
		else
		{
			int jj;
			for(jj=0;jj<na1;jj++)
			{
				sum+=A1[jj]*B2[nb2-1-jj];
			}
		}

		fprintf(fp2,"Case #%i: %I64d\n",i+1,sum);





	}

	return 0;
}
