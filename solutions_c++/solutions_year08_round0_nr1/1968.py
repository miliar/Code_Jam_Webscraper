#include <stdio.h>
#include <string.h>

#define END -1

int N,S,Q;
char eng[100][101];
char qer[1000][101];
int nbr[100];
int activ;


int make_output();
int calc(int pos,char seng[]);

int main(int argc,char* argv[])
{
	int index=1;
	FILE *in=fopen("infile.txt","r");
	fscanf(in,"%d",&N);
	for(int i=0;i<N;i++)
	{
		fscanf(in,"%d",&S);
		fseek(in,1,SEEK_CUR);
		for(int a=0;a<S;a++)
		{
			fgets(eng[a],101,in); 
		}
		fscanf(in,"%d",&Q);
		fseek(in,1,SEEK_CUR);
		for(int a=0;a<Q;a++)
		{
			fgets(qer[a],101,in);
		}
		int ret=make_output();
		if(ret==-1)
			ret=ret;
		printf("Case #%d: %d\n",index++,ret);
	}
	return 0;
}

int make_output()
{
	int switches=0;
	for(int a=0;a<Q;a++)
	{
		for(int b=0;b<S;b++)
		{
			nbr[b]=calc(a,eng[b]);
		}
		for(int b=0;b<S;b++)
		{
			if(nbr[b]==END)
			{
				//if(switches==0)
				return switches;
			}
		}
		int far=nbr[0],farid=0;
		for(int b=1;b<S;b++)
		{
			if(nbr[b]>far)
			{
				far=nbr[b];
				farid=b;
			}
		}
		//printf("far: %d\n",far);
		
		switches++;
		a+=far-1;
		//printf("A: %d\n",a);
	}
	return switches;
}

int calc(int pos,char seng[])
{
	int far=0;
	int broke=false;
	for(int a=pos;a<Q;a++)
	{
		if(strcmp(qer[a],seng))
			far++;
		else
		{
			broke=true;
			break;
		}
	}
	if(broke)
		return far;
	else
		return END;
}
