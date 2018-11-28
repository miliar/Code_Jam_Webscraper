#include <stdio.h>
#include <memory.h>

//using namespace std;


#define MIN(x,y) x<y?x:y
#define MAX(x,y) x>y?x:y

bool fn(long long x,long long y,bool t)
{
	if(y%x==0 || (2*x<y))
	{
		return t;
	}
	return fn(MIN(x,y-x),MAX(x,y-x),!t);
	
}

int main(int argc, char **argv)
{
	if(argc!=2)
	{
		printf("Usage: <prog> <input_file>\n");
		return 1;
	}

	FILE *fin = fopen("a.in","r");
	FILE *fout = fopen("a.out","w");

		
	int cnt;
	fscanf(fin,"%d",&cnt);
	for(int i=0;i<cnt;i++)
	{
		long long a1,a2,b1,b2;
		fscanf(fin,"%lld %lld %lld %lld",&a1,&a2,&b1,&b2);

		long long sum=0;
		for(long long j=a1;j<=a2;j++)
			for(long long k=b1;k<=b2;k++)
			{
				if(j==k)
					continue;
				long long x=MIN(j,k);
				long long y=MAX(j,k);

				if(y%x==0)
				{
					sum++;
					continue;
				}
				if(y>2*x)
				{
					sum++;
					continue;
				}
				if(fn(x,y,true))
					sum++;
			}
		
		fprintf(fout,"Case #%d: %lld\n",i+1,sum);
	}
	fclose(fin);
	fclose(fout);
}
