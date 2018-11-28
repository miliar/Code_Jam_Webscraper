#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<conio.h>

char serv[10][100], query[100][1000],currserv[100];
int N,S,Q;
void getdat(FILE*, char[][100],int);
int process(void);
int getnextser(int);

void main()
{
	clrscr();
	int i,j,k;
	FILE *ptr,*ptr2;
	ptr = fopen("input.txt","rt");
	ptr2= fopen("output.txt","wt");
	fscanf(ptr,"%d\n",&N);
	for(i=0;i<N;i++)
	{
		fscanf(ptr,"%d\n",&S);
		getdat(ptr,serv,S);
		fscanf(ptr,"%d\n",&Q);
		getdat(ptr,query,Q);
		k=process();
		fprintf(ptr2, "Case #%d: %d\n", i+1,k);
	}
	fclose(ptr);
	fclose(ptr2);
	getch();
}

void getdat(FILE *ptr,char abc[][100],int k)
{
	for(int i=0;i<k;i++)
		fgets(abc[i],100,ptr);
}

int process(void)
{
	int i=0,cs=getnextser(0),s=0;
	for(i=0;i<Q;i++)
		if(strcmp(serv[cs],query[i])==0)
		{
			s++;
			cs=getnextser(i);
		}
	return s;
}

int getnextser(int k)
{
	int pos[10],i,j,big=0;
	for(i=0;i<S;i++)
		pos[i]=0;
	for(i=0;i<S;i++)
		for(j=k;j<Q;j++)
			if(strcmp(serv[i],query[j])==0)
			{
				pos[i]=j;
				break;
			}
	for(i=0;i<S;i++)
		if(pos[i]==0 && strcmp(serv[i],query[k])!=0)
			return i;
	for(i=1;i<S;i++)
		if(pos[i]>pos[big])
			big=i;
	return big;
}
