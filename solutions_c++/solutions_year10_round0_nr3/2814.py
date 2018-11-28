#include<stdio.h>
#include<malloc.h>

struct queue
{
	int data;
	struct queue *link;
};

void ins_queue(struct queue ** p,int d);
int del_queue(struct queue **p);
int getdata_queue(struct queue *p);
main()
{
	int Sum=0,Money_Earned=0,i,j,l,Elem=0,R,K,N,T,ch,count;
	struct queue *p_queue=NULL;
	char temp_ch;
	bool sum_exceed=0;
	
	FILE *pFile,*pFile1;

	pFile=fopen("C:\\Documents and Settings\\kaku\\Desktop\\C-small-attempt5.in","r");
	fscanf(pFile,"%d",&T);
	
	temp_ch=fgetc(pFile);

	

	for(j=1;j<=T;j++)
	{
		
		fscanf(pFile,"%d",&R);
		temp_ch=fgetc(pFile);

		
		fscanf(pFile,"%d",&K);
		temp_ch=fgetc(pFile);

		
		fscanf(pFile,"%d",&N);
		temp_ch=fgetc(pFile);
		
		for(i=0;i<N;i++)
		{
			
			fscanf(pFile,"%d",&ch);
			temp_ch=fgetc(pFile);
			ins_queue(&p_queue,ch);
			
		}

		for(l=0;l<R;l++)
		{
			count=0;
			while(Sum<=K&&sum_exceed==0&&count<N)
			{
				Elem=getdata_queue(p_queue);
				Sum=Sum+Elem;
				if(Sum<=K)
				{
					del_queue(&p_queue);
					count++;
					ins_queue(&p_queue,Elem);
				}
				else
				{
					Sum=Sum-Elem;
					sum_exceed=1;
				}
			}
			Money_Earned=Money_Earned+Sum;
			Sum=0;
			count=0;
			sum_exceed=0;
		}
		
		pFile1=fopen("C:\\Documents and Settings\\kaku\\Desktop\\output.txt","a");
		fprintf(pFile1,"Case #%d: %d\n",j,Money_Earned);
		fclose(pFile1);
		Money_Earned=0;
		free(p_queue);
		p_queue=NULL;
	}
	fclose(pFile);

}

int getdata_queue(struct queue *p)
{
	return p->data;

}
int del_queue(struct queue **p)
{
	int d;
	struct queue *q=*p;
	
    d=q->data;
	(*p)=q->link;

	free(q);

	return d;
}

void ins_queue(struct queue ** p,int d)
{
	struct queue *q=*p;
	struct queue *r;
	
	if(*p==NULL)
	{
		*p=(struct queue *)malloc(sizeof(queue) );
		(*p)->data=d;
		(*p)->link=NULL;
	}
	else
	{
		while(q->link!=NULL)
			q=q->link;
		r=(struct queue *)malloc(sizeof(queue) );
		r->data=d;
		r->link=NULL;
		q->link=r;
		

	}
}
