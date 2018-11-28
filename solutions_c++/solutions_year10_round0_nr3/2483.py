#include<stdio.h>
struct person
{
	int n;
	struct person *next; 
};
typedef struct person person;
typedef struct person * link;
int t,r,k,n;
int ans;
link last;
link creat(link head)
{
link pointer,now;
int data;
scanf("%d",&data);
head=new person;
head->n=data;
head->next=head;
pointer=head;
for(int i=1;i<n;i++)
	{
	 now=new person;
	 scanf("%d",&data);
	 now->n=data;
	 now->next=head;
	 pointer->next=now;
	 pointer=now;
	}
last=pointer;
return head;
}
link work(link head)
{
int re=k;
int time=1;
link pointer;
for(pointer=head;pointer;pointer=pointer->next)
	{
	 if(time>n) break;
	 if(re>=pointer->n)
		{
		 re-=pointer->n;
		 ans+=pointer->n;
		
		 head=pointer->next;
		 last->next=pointer;
		 last=pointer;
		}
	 else 
		 break;
	 //printf("pk=%d  %d\n",pointer->n,time);
	 time++;
	}
return head;
}
int main()
{
freopen("3.in","r",stdin);
freopen("3.out","w",stdout);
scanf("%d",&t);
int time=1;
while(t--)
{
scanf("%d%d%d",&r,&k,&n);
ans=0;
link head;
head = new person;
head=creat(head);
while(r--)
{
head=work(head);
//printf("head =%d\n",head->n);
}
printf("Case #%d: %d\n",time,ans);
time++;
}
return 0;
}