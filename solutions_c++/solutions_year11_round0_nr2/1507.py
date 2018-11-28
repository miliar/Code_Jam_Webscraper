#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int c,d,n;
char c1[40][10],d1[40][10];
char a[110];
int b[110];

int main()
{
	int t,cas;
	fin>>t;
	for(cas=1;cas<=t;cas++)
	{
		int n,i,j,k,w;
		fin>>c;
		for(i=0;i<c;i++)
		fin>>c1[i];
		fin>>d;
		for(i=0;i<d;i++)
		{
			fin>>d1[i];
		}
		fin>>n;
		fin>>a;
		int tot=0;
		char p;
		for(i=0;i<n;i++)
		{
			if(tot==0)
			{
				b[tot++]=a[i]-'A';
			}
			else
			{
				j=b[tot-1];
				for(k=0;k<c;k++)
				{
					if(j==(c1[k][0]-'A') && a[i]==c1[k][1])
					{
						b[tot-1]=c1[k][2]-'A';
						break;
					}
					else if((j==c1[k][1]-'A') && a[i]==c1[k][0])
					{
						b[tot-1]=c1[k][2]-'A';
						break;
					}
				}
				if(k==c)
				{
					for(k=0;k<d;k++)
					{
						if(a[i]==d1[k][0])
						{
							for(w=0;w<tot;w++)
							if(b[w]==d1[k][1]-'A') break;
							if(w!=tot)
							{
								tot=0;
								break;
							}
						}
						else if(a[i]==d1[k][1])
						{
							for(w=0;w<tot;w++)
							if(b[w]==d1[k][0]-'A') break;
							if(w!=tot)
							{
								tot=0;
								break;
							}
						}
					}
					if(k==d)
					{
						b[tot++]=a[i]-'A';
					}
				}
			}
		}
		fout<<"Case #"<<cas<<": [";
		if(tot>0)
		{
			for(i=0;i<tot-1;i++)
			{
				p=b[i]+'A';
				fout<<p<<", ";
			}
			p=b[tot-1]+'A';
			fout<<p;
		}
		fout<<']'<<endl;
	}
	return 0;
}
