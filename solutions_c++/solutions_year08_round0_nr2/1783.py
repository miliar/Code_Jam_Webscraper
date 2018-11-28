#include <iostream>
using namespace std;

struct node
{
	int st_h,st_m;
	int ar_h,ar_m;
}A[105],B[105];

bool VA[105],VB[105];
int  TA[105],TB[105];

int N,NA,NB,T;
int lt,rt;

int cmp(const void *a,const void *b)
{
	node *c=(node *)a;
	node *d=(node *)b;
	if(c->st_h==d->st_h)
		return c->st_m-d->st_m;
	else
		return c->st_h-d->st_h;
}

void solve()
{
	int l=0,r=0;
	bool flag=false;//left for false,right for true;
	while(1)
	{
		if(l>=NA&&r>=NB)break;
		int minn=0;
		
		if(l>=NA || ((A[l].st_h>B[r].st_h||( A[l].st_h==B[r].st_h&&A[l].st_m>=B[r].st_m) )&&l<NA&&r<NB))
		{
			minn=B[r].st_h;
			VB[r]=true;
			flag=true;//right
		}
		else if(r>=NB || ((A[l].st_h<B[r].st_h||(A[l].st_h==B[r].st_h&&A[l].st_m<B[r].st_m))&&l<NA&&r<NB))
		{
			minn=A[l].st_h;
			VA[l]=true;
			flag=false;//left
		}

		if(flag)//right
		{
			if(TB[r]==0)rt++;
			else TB[r]--;
			for(int i=l;i<NA;i++)
				if( !VA[i]&&TA[i]==0&&( B[r].ar_h<A[i].st_h || (B[r].ar_h==A[i].st_h&&B[r].ar_m<=A[i].st_m) ) )
				{
					//VA[i]=true;
					TA[i]++;
					break;
				}
		}
		else//left
		{
			if(TA[l]==0)lt++;
			else TA[l]--;
			for(int i=r;i<NB;i++)
				if( !VB[i]&&TB[i]==0&&( A[l].ar_h<B[i].st_h || (A[l].ar_h==B[i].st_h&&A[l].ar_m<=B[i].st_m) ) )
				{
					//VB[i]=true;
					TB[i]++;
					break;
				}
		}
		
		//ÓÒÒÆ
		while(VA[l]&&l<NA)l++;
		while(VB[r]&&r<NB)r++;

		
	}
}

int main()
{
	//freopen("in.txt","r",stdin);
	scanf("%d",&N);
	int i,count=1;
	while(N--)
	{
		scanf("%d%d%d",&T,&NA,&NB);
		for(i=0;i<NA;i++)
		{
			scanf("%d:%d%d:%d",&A[i].st_h,&A[i].st_m,&A[i].ar_h,&A[i].ar_m);
			A[i].ar_m+=T;
			if(A[i].ar_m>=60)
			{
				A[i].ar_h+=A[i].ar_m/60;
				A[i].ar_m%=60;
			}
		}
		for(i=0;i<NB;i++)
		{
			scanf("%d:%d%d:%d",&B[i].st_h,&B[i].st_m,&B[i].ar_h,&B[i].ar_m);
			B[i].ar_m+=T;
			if(B[i].ar_m>=60)
			{
				B[i].ar_h+=B[i].ar_m/60;
				B[i].ar_m%=60;
			}
		}

		qsort(A,NA,sizeof(A[0]),cmp);
		qsort(B,NB,sizeof(B[0]),cmp);

		lt=0,rt=0;
		memset(VA,false,sizeof(VA));
		memset(VB,false,sizeof(VB));
		memset(TA,0,sizeof(TA));
		memset(TB,0,sizeof(TB));

		solve();
		
		printf("Case #%d: %d %d\n",count++,lt,rt);

		for(int k=0;k<25;k++)
			A[k].ar_h=A[k].ar_m=A[k].st_h=A[k].st_m=B[k].ar_h=B[k].ar_m=B[k].st_h=B[k].st_m=0;
	}
	return 0;
}