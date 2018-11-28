#include <stdio.h>

typedef struct _stack
{
	char s[101];
	int top;
}STACK;

typedef struct _nonbase
{
	char baseseq[2];
	char nonbase;
}NONBASE;
void initialize(STACK* s)
{
	s->top=-1;
}
void push(STACK* s,char c)
{
	s->s[++s->top] = c;
}
char pop(STACK* s)
{
	return s->s[s->top--];
}
int get_nonbase_index(char* base,NONBASE* nblist,int c)
{
	for(int i=0;i<c;i++)
	{
		if(base[0] == nblist[i].baseseq[0] && base[1] == nblist[i].baseseq[1])
			return i;
		if(base[0] == nblist[i].baseseq[1] && base[1] == nblist[i].baseseq[0])
			return i;
	}
	return -1;
}
int are_opposing(char c1,char c2,char oppose[28][2],int d)
{
	for(int i=0;i<d;i++)
	{
		if(c1 == oppose[i][0] && c2 == oppose[i][1])
			return 1;
		if(c1 == oppose[i][1] && c2 == oppose[i][0])
			return 1;
	}
	return 0;
}
int main()
{
	FILE *fin,*fout;
	STACK s;
	fin=fopen("input.txt","r");
	fout=fopen("output.txt","w");
	int t,c,d,n;
	NONBASE nblist[36];
	char oppose[28][2];
	char elem;
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		initialize(&s);
		fscanf(fin,"%d",&c);
		for(int j=0;j<c;j++)
		{
			fgetc(fin);
			nblist[j].baseseq[0]=fgetc(fin);
			nblist[j].baseseq[1]=fgetc(fin);
			nblist[j].nonbase=fgetc(fin);
		}
		fscanf(fin,"%d",&d);
		for(int j=0;j<d;j++)
		{
			fgetc(fin);
			oppose[j][0]=fgetc(fin);
			oppose[j][1]=fgetc(fin);
		}		
		fscanf(fin,"%d",&n);
		fgetc(fin);
		for(int j=0;j<n;j++)
		{
			elem=fgetc(fin);
			push(&s,elem);
			if(s.top > 0)
			{
				int index=get_nonbase_index(&s.s[s.top - 1],nblist,c);
				if(index != -1)
				{
					pop(&s);
					pop(&s);
					push(&s,nblist[index].nonbase);
					continue;
				}
				for(int k=0;k<s.top;k++)
				{
					if(are_opposing(s.s[k],elem,oppose,d))
						initialize(&s);
				}
			}
		}
		fprintf(fout,"[");
		for(int j=0;j<=s.top;j++)
		{
			fprintf(fout,"%c",s.s[j]);
			if(j!=s.top)
				fprintf(fout,", ");
		}
		fprintf(fout,"]");
		if(i!=t-1)
			fprintf(fout,"\n");
	}
	return 0;
}