#include<iostream>
#include<cstdio>
#include<cstdlib>
struct type
{
	long long s,data;
	int y,cnt;
	type *l,*r;
};
type* new_element()
{
	type *a=(type*)malloc(sizeof(type));
	a->l=a->r=NULL;
	a->y=rand()*32717+rand();
	return a;
}
void fix(type *&T)
{
	if(T==NULL) return;
	T->cnt=1;
	T->s=T->data;
	if(T->l!=NULL)
	{
		T->cnt+=T->l->cnt;
		T->s+=T->l->s;
	}
	if(T->r!=NULL) 
	{
		T->cnt+=T->r->cnt;
		T->s+=T->r->s;
	}
}
int count(type *&T)
{
	if(T!=NULL) return T->cnt;
	return 0;
}
void show(type *T)
{
	if(T==NULL) return;
	show(T->l);
	printf("%d ",T->data);
	show(T->r);
}
void del(type *T)
{
	if(T==NULL) return;
	del(T->l);
	del(T->r);
	T->l=T->r=NULL;
	free(T);
}
void split(type *T,type *&L,type *&R,int x)
{
	if(T==NULL)
	{
		L=R=NULL;
		return;
	}
	type *ll,*rr;
	int k=count(T->l)+1;
	if(x<k)
	{
		split(T->l,ll,rr,x);
		L=ll;
		T->l=rr;
		R=T;
	}
	else
	{
		split(T->r,ll,rr,x-k);
		T->r=ll;
		R=rr;
		L=T;
	}
	fix(T);
	fix(L);
	fix(R);
}
type* merge(type *L,type *R)
{
	if(L==NULL) return R;
	if(R==NULL) return L;
	if(L->y>R->y)
	{
		L->r=merge(L->r,R);
		fix(L);
		return L;
	}
	R->l=merge(L,R->l);
	fix(R);
	return R;
}
type* add(type *&T,long long data)
{
	type *a=new_element();
	a->data=data;
	fix(a);
	return merge(T,a);
}

type* move(type *&T,int r)
{
	type *q,*w;
	q=w=NULL;
	split(T,q,w,r);
	return merge(w,q);
}
long long sum(type *T,int k)
{
	if(T==NULL) return 0;
	int n=count(T->l)+1;
	if(n>k) return sum(T->l,k);
	if(T->l) return T->l->s+T->data+sum(T->r,k-n);
	return T->data+sum(T->r,k-n);
}

type *T;

int search(int l,int r,long long key)
{
	if(l+1>=r)
	{
		if(sum(T,r)<=key) return r;
		return l;
	}
	int m=(l+r)/2;
	if(sum(T,m)<key) return search(m,r,key);
	return search(l,m,key);
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int N,M,i,k,F,tests;
	long long q,ans;
	scanf("%d",&tests);
	for(int tt=1;tt<=tests;tt++)
	{
		T=NULL;
		ans=0;
		scanf("%d%d%d",&M,&F,&N);
		for(i=0;i<N;i++) 
		{
			scanf("%I64d",&q);
			T=add(T,q);
		}
		for(i=0;i<M;i++)
		{
	//		show(T);
			k=search(1,N,F);
			ans+=sum(T,k);
		//	printf("k=%d\n",k);
			T=move(T,k);
		}
		del(T);
		printf("Case #%d: %I64d\n",tt,ans);
	}
	return 0;
}