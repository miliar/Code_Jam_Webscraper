#include <iostream>

using namespace std;

struct aa
{
	int k;
	aa *next;
};

aa *p,*q,*last;
aa *head;

int i,u,k,j,m,n,x,z,t;
int a[10000];

int main()
{
	freopen("C-small-attempt3.in","r",stdin);
	freopen("1.out","w",stdout);
	t=0;
	cin>>z;
	while (z--)
	{
		t++;
		scanf("%d",&n);
		for (i=0;i<n;i++) a[i]=0;
		head=0;
		head=new aa;
		head->k=0;
		head->next=0;
		for (i=n-1;i>0;i--)
		{
			p=new aa;
			p->k=i;
			p->next=head->next;
			head->next=p;
		}


		p=head;
		for (i=0;i<n;i++)
		{
			for (u=0;u<i;u++)
			{
				
				last=p;
				p=p->next;
				if (p==0) p=head;
				
			}
			if (p==head)
			{
				a[head->k]=i+1;
				q=head;
				head=head->next;
				
					p=head;
				delete q;
			}
			else
			{
				a[p->k]=i+1;
				q=p;
				last->next=p->next;
				p=p->next;
				if (p==0) p=head;
				delete q;
			}
		}

		//for (i=0;i<n;i++) printf(" %d",a[i]);
		scanf("%d",&m);
		printf("Case #%d:",t);

		for (i=0;i<m;i++)
		{
			scanf("%d",&k);
			k--;
			printf(" %d",a[k]);
		}
		printf("\n");

	}
	return 0;
}





