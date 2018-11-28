#include <stdio.h>
#include <iostream>
using namespace std;
int *tl;
int count=0;
int max=0;
int p,cs;
int main()
{
	int scorecouldbe(bool iss,int score);
	void greed(int rest,int pos);
	FILE *fp1,*fp2;
	int num,s,i,j=1;
	fp1=fopen("B-small-attempt0.in","r");
	fp2=fopen("B-small-attempt0.out","w");
	fscanf(fp1,"%d",&num);
	while(num--)
	{
		count=0;
		max=0;
		fgetc(fp1);
		fscanf(fp1,"%d %d %d",&cs,&s,&p);
		tl=new int[cs];
		for(i=0;i<cs;i++)
		{
			fscanf(fp1," %d",&tl[i]);
		}
		greed(s,0);
		fprintf(fp2,"Case #%d: %d\n",j++,max);
	}
	return 0;
}

void greed(int rest,int pos)
{
	int scorecouldbe(bool iss,int score);
	int flag=0;
	if(pos==cs)
	{
		if(count>max)
			max=count;
		return;
	}
	else if(rest==0||tl[pos]<2||tl[pos]>28)
	{
		if(scorecouldbe(false,tl[pos])>=p)
		{
			count++;
			flag=1;
		}
		greed(rest,pos+1);
		if(flag==1)
		{
			count--;
			flag=0;
		}
	}
	else
	{
		if(scorecouldbe(true,tl[pos])>=p)
		{
			count++;
			flag=1;
		}
		greed(rest-1,pos+1);
		if(flag==1)
		{
			count--;
			flag=0;
		}
		if(scorecouldbe(false,tl[pos])>=p)
		{
			count++;
			flag=1;
		}
		greed(rest,pos+1);
		if(flag==1)
		{
			count--;
			flag=0;
		}
	}
}

int scorecouldbe(bool iss,int score)
{
	if(score%3==0)
	{
		if(iss)
		{
			return score/3+1;
		}
		else
			return score/3;
	}
	else if(score%3==1)
	{
		if(iss)
		{
			return score/3+1;
		}
		else
			return score/3+1;
	}
	else if(score%3==2)
	{
		if(iss)
		{
			return score/3+2;
		}
		else
			return score/3+1;
	}
	return 0;
}
