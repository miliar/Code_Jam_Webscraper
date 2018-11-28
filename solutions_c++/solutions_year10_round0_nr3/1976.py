#include <iostream> 
#include <fstream>

using namespace std;

ifstream dat ("c.in");
ofstream sol ("c.out");

#define mmax 1000002

typedef struct Tp
{
	int data;
	int id;
	struct Tp* next;
	struct Tp* prev;
} TP;

TP *last,*a;
int fl[mmax];
int count[mmax];
long long sumC[mmax];
long long res,sumAll;
int kk;

void Add(int index, int num)
{
	TP *p=(TP*)malloc(sizeof(TP));
	p->data=num;
	p->id=index;
	p->next=NULL;
	p->prev=last;
	if (a==NULL) { a=p; a->prev=NULL; }
	last->next=p;
	last=p;
}
void print ()
{
	TP *pt=a;
	while (pt) { cout << pt->data << " "; pt=pt->next; }
	cout << endl;
}
int main ()
{
	TP *ptr;
	last=(TP*)malloc(sizeof(TP));
	a=(TP*)malloc(sizeof(TP));
	int t,p;
	int n,k,r,i,num;
	dat >> t;
	for(p=0;p<t;p++)
	{
		sumAll=0; kk=0;
		dat >> r >> k >> n;		
		for(i=0;i<n*n+1;i++) fl[i]=false;
		a=NULL;
		for(i=0;i<n;i++)
		{
			dat >> num;
			Add(i,num);
		}
//		print();
		res=0;
		int s=0;
		for(i=0;i<r;i++)
		{
			ptr=a; s=0;
			while(ptr && s+ptr->data<=k) { s+=ptr->data; ptr=ptr->next; }
			int x=a->id,y,eq; 
			if (!ptr)
			{
				y=last->id;
			} else y=ptr->prev->id;
			eq=x*n+y;
			if (fl[eq])
			{
				int ost=r-i,dist=kk-fl[eq]+1;
				long long ss=sumAll-sumC[fl[eq]]+s;
				res+=(int)(ost/dist)*ss;
				if (ost%dist!=0) res+=sumC[fl[eq]+(ost%dist)-1]-sumC[fl[eq]]+s;
				break;
			} 
			res+=s;
			kk++;
			sumAll+=s;
			fl[eq]=kk; sumC[kk]=sumAll;			
			count[kk]=s;			
			if (!ptr) continue;
//			cout << a->id << " " << ptr->prev->id << endl;
			last->next=a;
			a->prev=last;
			ptr->prev->next=NULL;
			last=ptr->prev;			
			ptr->prev=NULL;
			a=ptr;
			//print();
		//	cout << s << endl;
		}
		sol << "Case #" << p+1 << ": " << res << endl;		
	}
	return 0;
}