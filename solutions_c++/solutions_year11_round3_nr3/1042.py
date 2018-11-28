#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
using namespace std;

int main()
{
	FILE *f=fopen("c.in","r");
	FILE *g=fopen("c.out","w");

	int t;
	fscanf(f,"%i",&t);

	for(int u=0;u<t;u++)
	{
		int n,l,h;
		fscanf(f,"%i%i%i",&n,&l,&h);

		int freq[200];
		for(int i=0;i<n;i++)
			fscanf(f,"%i",&freq[i]);

		int sol=-1;
		for (int i=l;i<=h;i++)
		{
			int found=1;
			for(int j=0;j<n;j++)
				if(i%freq[j]!=0 && freq[j]%i!=0)
				{
					found=0;
					break;
				}
			if(found==1)
			{
				sol=i;
				break;
			}
		}
		if(sol==-1)
			fprintf(g,"%s%i%s%s\n","Case #",u+1,": ","NO");
		else
			fprintf(g,"%s%i%s%i\n","Case #",u+1,": ",sol);
	}
	fclose(f);
	fclose(g);
}

			
				
			
