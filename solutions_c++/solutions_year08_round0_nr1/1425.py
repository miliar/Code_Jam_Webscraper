#include<iostream>
#include<cstdio>
#include<bitset>
#include<map>
#include<stdio.h>

using namespace std;
int main()
{
	int t,n,n2,i,count;
	
	char stemp[110];
	int shift;
	int c=1;
	FILE *f1,*f2;
	f1=fopen("A-large.in","r");
	f2=fopen("A-large.out","w");
	fscanf(f1,"%d\n",&t);
	while(t--)
	{
		map<string,int> s;
		string str;
		bitset < 100 > b;
		shift=0;
		
		fscanf(f1,"%d\n",&n);
		for(i=0;i<n;i++)
		{
			fgets(stemp,256,f1);
			str=stemp;
			s[str]=i;
		}
		
		fscanf(f1,"%d\n",&n2);
		for(i=0;i<n2;i++)
		{
			fgets(stemp,256,f1);
			str=stemp;
			b.set( s[str] );
			count=b.count();
			
			if(count==n)
			{
				shift++;
				b.reset();
				b.set( s[str] );
			}
		}
		
		fprintf(f2,"Case #%d: %d\n",c,shift);
		c++;
	}
	fclose(f1);
	fclose(f2);
	return 0;
}	 
				
		
		
