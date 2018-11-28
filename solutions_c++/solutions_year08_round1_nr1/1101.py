#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
using namespace std;

#ifdef WIN32
typedef __int64 i64;
#else
typedef long long i64;
#endif

i64 sum;
struct tt{
	long val;
};
bool operator<(tt a,tt b)
{
	return abs(a.val)<abs(b.val);
}


long Noftest;
long nn;
tt A1[2000];
tt A2[2000];
tt B1[2000];
tt B2[2000];
long na1;
long na2;
long nb1;
long nb2;
int main()
{
	ifstream fin;
	fin.open("test.in");
	FILE* fp2;
	fp2=fopen("test.out","w");
	fin>>Noftest;
	
	long i;
	for(i=0;i<Noftest;i++)
	{
		fin>>nn;
		na1=0;na2=0;
		long temp;
		long j;
		for(j=0;j<nn;j++)
		{
			fin>>temp;
			if(temp<=0)
			{
				A1[na1].val=temp;na1++;
			}
			else
			{
				A2[na2].val=temp;na2++;
			}
		}
		nb1=0;nb2=0;
		for(j=0;j<nn;j++)
		{
			fin>>temp;
			if(temp<=0)
			{
				B2[nb2].val=temp;nb2++;
			}
			else
			{
				B1[nb1].val=temp;nb1++;
			}
		}
		sort(&A1[0],&A1[na1]);
		sort(&A2[0],&A2[na2]);
		sort(&B1[0],&B1[nb1]);
		sort(&B2[0],&B2[nb2]);

		sum=0;
		while(na1!=0&&nb1!=0)
		{
			sum+=A1[na1-1].val*B1[nb1-1].val;
			na1--;nb1--;
		}
		while(na2!=0&&nb2!=0)
		{
			sum+=A2[na2-1].val*B2[nb2-1].val;
			na2--;nb2--;
		}
		if(0==na1)
		{
			int ii;
			
			for(ii=0;ii<nb1;ii++)
			{
				sum+=B1[ii].val*A2[na2-1-ii].val;
			}
		}
		else
		{
			int jj;
			for(jj=0;jj<na1;jj++)
			{
				sum+=A1[jj].val*B2[nb2-1-jj].val;
			}
		}

		fprintf(fp2,"Case #%i: %I64d\n",i+1,sum);





	}
	fin.close();

	return 0;
}
