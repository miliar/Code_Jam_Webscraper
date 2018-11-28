#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
using namespace std;
char word[9000][900],b[900][900],d[900];
int N,D,L;
int check()
{
	int count=0,flag,mark;
	for (int i=0;i<D;i++)
	{
		mark=0;
		for (int j=0;j<L;j++)
		{
			flag=0;
			for (int k=0;k<d[j];k++)
			{
				if (word[i][j]==b[j][k]) {flag=1; break;}
			}
			if (flag==1) mark++; 
		}
		if (mark==L) count++;
	}
	return (count);
}
int main()
{
	char a[9000][900];
	int i,j,k,h,r;
	FILE * rf=fopen("A-large.in","r");
	FILE * wf=fopen("asans.in","w");
	fscanf (rf,"%d%d%d",&L,&D,&N);
	for (i=0;i<D;i++)
	{
		fscanf (rf,"%s",word[i]);
	}
	for (i=0;i<N;i++)
	{
		fscanf (rf,"%s",a[i]);
	}
	for (i=0;i<N;i++)
	{
		r=0;
		//cout<<a[i]<<endl;
		for (j=0;j<strlen(a[i]);j++)
		{
			h=0;
			if (a[i][j]=='(')
			{
				for (k=j+1;k<strlen(a[i]);k++)
				{
					if (a[i][k]==')') {j=k; r++; break;}
					else {b[r][h++]=a[i][k];d[r]=h;}
				}
			}
			else {b[r][h++]=a[i][j];d[r]=h;r++;}
			//cout<<r-1<<" "<<h<<" "<<b[r-1]<<endl;
		}
		//printf ("Case #%d: %d\n",i+1,check());
		fprintf (wf,"Case #%d: %d\n",i+1,check());
	}
	return 0;
}
