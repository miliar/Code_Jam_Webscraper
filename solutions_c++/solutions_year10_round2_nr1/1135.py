#include<stdio.h>
#include<conio.h>
#include<string.h>

int len[10000],n,y;
char list[10000][101];

int createDir(char dir[101])
{
	int i,j,l;
	int c=0;
	char prnt[100];
	l = strlen(dir);
	if(l <= 1)
		return 0;
	for(i=0;i<n;i++)
	{
		if(l == len[i])
			if(!strcmp(dir,list[i]))
				return 0;
	}
	strcpy(list[n],dir);
	len[n++]=l;
	for(i=l-1;i>=0;i--)
		if(dir[i]=='/') 
			break;
	strncpy(prnt,dir,i);
	prnt[i] = '\0';
	return 1 + createDir(prnt);
}

int main()
{
	
	int x, T,i,M,N,j;
	char dir[101];
	
	FILE * ifp=fopen("A-large.in","r");
	FILE * ofp=fopen("A-large.out","w");
	
	fscanf(ifp,"%d\n",&T);
	for (x=1;x<=T;x++)
	{
		fscanf(ifp,"%d %d\n",&N,&M);
		y=0;
		for(n=0;n<N;n++	)
		{
			fscanf(ifp,"%s\n",&list[n]);
			len[n]=strlen(list[n]);
		}

		for(i=0;i<M;i++)
		{
			fscanf(ifp,"%s\n",dir);
			y+=createDir(dir);
		}
		fprintf(ofp,"Case #%d: %d\n",x,y);
	}

	fclose(ifp);
	fclose(ofp);
	return 0;
}
