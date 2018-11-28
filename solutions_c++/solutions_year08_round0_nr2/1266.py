#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

#define SZ 105

typedef struct{
	long start;
	long end;
}trip;

trip atob[SZ],btoa[SZ];
bool flagab[SZ],flagba[SZ];
long na,nb;

int sortfunc(const void *a,const void *b);
void process(long tag,long ind,long t);

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	long inp,i,num,kase,t,curab,curba,ares,bres;
	char str1[25],str2[25];
	char *ptr;
	scanf("%ld",&inp);
	for(kase=1;kase<=inp;kase++)
	{
		scanf("%ld",&t);
		scanf("%ld %ld",&na,&nb);
		for(i=0;i<na;i++)
		{
			scanf(" %s %s",str1,str2);
			ptr=strtok(str1,":");
			num=atol(ptr);
			ptr=strtok(NULL,":");
			num=num*60+atol(ptr);
			atob[i].start=num;
			ptr=strtok(str2,":");
			num=atol(ptr);
			ptr=strtok(NULL,":");
			num=num*60+atol(ptr);
			atob[i].end=num;
		}
		for(i=0;i<nb;i++)
		{
			scanf(" %s %s",str1,str2);
			ptr=strtok(str1,":");
			num=atol(ptr);
			ptr=strtok(NULL,":");
			num=num*60+atol(ptr);
			btoa[i].start=num;
			ptr=strtok(str2,":");
			num=atol(ptr);
			ptr=strtok(NULL,":");
			num=num*60+atol(ptr);
			btoa[i].end=num;
		}
		qsort(atob,na,sizeof(trip),sortfunc);
		qsort(btoa,nb,sizeof(trip),sortfunc);
		memset(flagab,false,sizeof(flagab));
		memset(flagba,false,sizeof(flagba));
		curab=curba=0;
		ares=bres=0;
		while(curab<na||curba<nb)
		{
			while(flagab[curab]==true)
				curab++;
			while(flagba[curba]==true)
				curba++;
			if(curab>=na&&curba>=nb)
				break;
			if(curab>=na)
			{
				for(i=curba;i<nb;i++)
				{
					if(flagba[i]==false)
						bres++;
				}
				break;
			}
			if(curba>=nb)
			{
				for(i=curab;i<na;i++)
				{
					if(flagab[i]==false)
						ares++;
				}
				break;
			}
			if(atob[curab].start<btoa[curba].start)
			{
				ares++;
				flagab[curab]=true;
				process(0,curab,t);
			}
			else
			{
				if(atob[curba].start>btoa[curba].start)
				{
					bres++;
					flagba[curba]=true;
					process(1,curba,t);
				}
				else
				{
					if(atob[curab].end<btoa[curba].end)
					{
						ares++;
						flagab[curab]=true;
						process(0,curab,t);
					}
					else
					{
						bres++;
						flagba[curba]=true;
						process(1,curba,t);
					}
				}
			}
		}
		printf("Case #%ld: %ld %ld\n",kase,ares,bres);
	}
	return 0;
}

void process(long tag,long ind,long t)
{
	long avail,i;
	if(tag==0)
	{
		avail=atob[ind].end+t;
		for(i=0;i<nb;i++)
		{
			if((btoa[i].start>=avail)&&(flagba[i]==false))
			{
				flagba[i]=true;
				process(1,i,t);
				return;
			}
		}
	}
	if(tag==1)
	{
		avail=btoa[ind].end+t;
		for(i=0;i<na;i++)
		{
			if((atob[i].start>=avail)&&(flagab[i]==false))
			{
				flagab[i]=true;
				process(0,i,t);
				return;
			}
		}
	}
	return;
}

int sortfunc(const void *a,const void *b)
{
	trip *x=(trip *)a;
	trip *y=(trip *)b;
	if(x->start>y->start)
		return 1;
	if(x->start<y->start)
		return -1;
	if(x->end>y->end)
		return 1;
	if(x->end<y->end)
		return -1;
	return 0;
}