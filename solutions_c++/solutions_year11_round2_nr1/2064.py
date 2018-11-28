#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
using namespace std;

const int NMAX=150;
int main()
{
	FILE *f=fopen("a.in","r");
	FILE *g=fopen("a.out","w");

	int t,a[NMAX][NMAX];
	fscanf(f,"%i\n",&t);

	float w1=(double) 0.25;
	float w2=(double) 0.5;
	float w3=(double) 0.25;
	for(int u=0;u<t;u++)
	{
		int n;
		fscanf(f,"%i\n",&n);

		char c;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				fscanf(f,"%c",&c);
				if(c=='.')
					a[i][j]=-1;
				else if(c=='0')
					a[i][j]=0;
				else
					a[i][j]=1;
			}
			fscanf(f,"%c",&c);
		}
		float wp[NMAX],opo[NMAX];
		for(int i=0;i<n;i++)
		{
			int win=0,played=0;
			for(int j=0;j<n;j++)
				if(a[i][j]==0 || a[i][j]==1)
				{
					++played;
					if(a[i][j]==1)
						++win;
				}
			wp[i]=(float) win/played;
		}
		float avg[NMAX];
		for(int i=0;i<n;i++)
		{
			int op=0;
			for(int j=0;j<n;j++)
			{
				if(a[i][j]==0 || a[i][j]==1)
				{
					++op;
					int win=0,played=0;
					for(int k=0;k<n;k++)
					{
						if(k!=i)
						{
							if(a[j][k]==0 || a[j][k]==1)
							{
								++played;
								if(a[j][k]==1)
									++win;
							}
						}
					}
					avg[j]=(float) win/played;
				}
			}
			float suma=0;
			for(int j=0;j<n;j++)
			{
				if(a[i][j]==0 || a[i][j]==1)
					suma+=avg[j];
			}
			opo[i]=(float) suma/op;
			for(int j=0;j<n;j++)
				avg[j]=0;
		}

		float oopo[NMAX];
		for(int i=0;i<n;i++)
		{
			int op=0;
			float suma=0;
			for(int j=0;j<n;j++)
			{
				if(a[i][j]==0 || a[i][j]==1)
				{
					++op;
					suma+=opo[j];
				}
			}
			oopo[i]=(float) suma/op;
		}
		fprintf(g,"%s%i%s\n","Case #",u+1,":");
		for(int i=0;i<n;i++)
		{
			float score=w1*wp[i]+w2*opo[i]+w3*oopo[i];
			fprintf(g,"%.6f\n",score);
		}
	}
	fclose(f);
	fclose(g);
}

