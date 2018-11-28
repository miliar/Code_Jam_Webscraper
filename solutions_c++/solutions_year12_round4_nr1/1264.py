#include <stdio.h>
#include <algorithm>

using namespace std;

struct rope_info
{
	__int64 x;
	__int64 len;
};
rope_info rope[10002],check[100002],empty;

bool ropeslt(rope_info a,rope_info b)
{
	if(a.x<b.x)
		return 1;
	else
		return 0;
}

struct queue_info
{
	__int64 x;
	__int64 num;
	__int64 fl;
};
queue_info queue[1000002],temp,tempin;
int incnt,outcnt;

void push(queue_info x)
{
	queue[incnt++]=x;
	if(incnt==1000002)
		incnt=0;
}
queue_info pop()
{
	queue_info x;
	x=queue[outcnt++];
	if(outcnt==1000002)
		outcnt=0;
	return x;
}

int main()
{
	int i,j,z;
	__int64 t,tcase,st,ed,mid,ls;
	__int64 n,pl,fl,gl;

	FILE *in,*out;
	in=fopen("A-large.in","r");
	out=fopen("output.txt","w");

	fscanf(in,"%I64d",&tcase);
	for(t=0;t<tcase;t++)
	{
		fscanf(in,"%I64d",&n);
		for(i=0;i<n;i++)
		{
			fscanf(in,"%I64d%I64d",&rope[i].x,&rope[i].len);
			check[i]=empty;
		}
		fscanf(in,"%I64d",&gl);
		sort(&rope[0],&rope[n],ropeslt);

		incnt=outcnt=0;
		temp.x=0;
		temp.num=1;
		temp.fl=rope[0].x;
		push(temp);

		pl=0;
		while(1)
		{
			if(incnt==outcnt)
				break;
			temp=pop();
			if(rope[temp.x].x+temp.fl>=gl)
			{
				pl=1;
				break;
			}
			for(i=temp.num;i<n;i++)
			{
				if(rope[temp.x].x+temp.fl<rope[i].x)
					break;
				tempin.x=i;
				tempin.num=i+1;
				if(rope[i].x-rope[temp.x].x>=rope[i].len)
					tempin.fl=rope[i].len;
				else
					tempin.fl=rope[i].x-rope[temp.x].x;
				if(check[i].x<tempin.fl)
				{
					check[i].x=tempin.fl;
					push(tempin);
				}
			}
		}

		fprintf(out,"Case #%d: ",t+1);
		if(pl==0)
			fprintf(out,"NO\n");
		else
			fprintf(out,"YES\n");
	}

	return 0;
}