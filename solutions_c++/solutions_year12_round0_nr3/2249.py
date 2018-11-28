#include<stdio.h>
#include<set>
using namespace std;

FILE *f = fopen("numbers.in","r");
FILE *g = fopen("numbers.out","w");

#define MaxN 11

int T,A,B,Nr[] = {0,1,10,100,1000,10000,100000,1000000};
set<int> Exist;

inline int Rezolvare(int a,int b)
{
	int Sol, c = a,nr;
	
	for(nr=0;c;c/=10,++nr);
	
	for(int i=a;i<=b;i++)
	{
		c = i;
		Exist.erase(Exist.begin(),Exist.end());
		
		for(int j = 1;j<nr;j++)
		{
			c = c%10 * Nr[nr] + (c/10);
			if(c > i && c <= b && Exist.find(c) == Exist.end())
				++ Sol,Exist.insert(c);
		}
	}
	
	return Sol;
}

int main()
{
	fscanf(f,"%d\n",&T);
	for(int i=1;i<=T;i++)
	{
		fscanf(f,"%d %d",&A,&B);
		fprintf(g,"Case #%d: %d\n",i,Rezolvare(A,B));
	}
}