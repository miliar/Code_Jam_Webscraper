#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <cstring>
#include <ctype.h>

#define inputfilename "a_5.in"
#define outputfilename "a_5.out"

using namespace std;

struct node
{
	int start, over;
	int id;
};
struct node a[100] , b[100];
bool hasha[100], hashb[100];
int t;		
int na, nb;

int cmp(const void *p , const void *q)
{
	struct node *a = (struct node *)p;
	struct node *b = (struct node *)q;
	if ((a->start) > (b->start)) return 1;
	if ((a->start) < (b->start)) return 0;
	
	if ((a->over) > (b->over)) return 1;
	return 0;
}


int search(struct node arr[] , int st ,int size , bool isa)
{
	int b = 0 , e = size-1;
	if (arr[e].start < st) return -1;
	int mid;
	while (b<e)
	{
		mid = (b+e)/2;
		if (arr[mid].start == st){e =mid; break;}
		else if (arr[mid].start < st) b = mid+1;
		else e = mid -1;
	}
	int loop = e;
	while (arr[loop].start < st) loop++;
	while (loop > 0 && arr[loop].start == arr[loop-1].start) loop--;
	if (isa)
	{
		while ( loop < size && !hasha[ arr[loop].id  ]) loop++;
	}
	else
	{
		while ( loop < size && !hashb[ arr[loop].id  ]) loop++;	
	}
	if (loop >= size) return -1;
	else return loop;
}

int doa(int pos)
{
	hasha[a[pos].id] = false;
	return search(b , a[pos].over+t , nb , false);
}
int dob(int pos)
{
	hashb[b[pos].id] = false;
	return search(a, b[pos].over+t, na, true);
}

int loop(bool isa , int next)
{
	do
	{
		if (isa)
		{
			next = doa(next);
			if (next == -1) break;
		}
		else 
		{
			next = dob(next);
			if (next == -1) break;
		}
		isa = !isa;
	}
	while (1);
	return 0;
}

int main ()
{
	freopen(inputfilename , "r" , stdin);
	freopen(outputfilename , "w" , stdout);

	int times , number;
	scanf("%d", & number);
	for (times = 0 ;times <  number ; times++)
	{

		scanf("%d" , &t);
		scanf("%d%d" , &na, &nb);
		int i;
		memset(hasha, true , sizeof(hasha));
		memset(hashb, true , sizeof(hashb));
		for (i = 0 ; i < na ; i++)
		{
			int t1,t2,t3,t4;
			scanf("%2d:%2d %2d:%2d" , &t1,&t2,&t3,&t4);
			a[i].start= t1*60+t2;
			a[i].over = t3*60+t4;
			a[i].id = i;
		}
		for (i = 0 ; i < nb ; i++)
		{
			int t1,t2,t3,t4;
			scanf("%2d:%2d %2d:%2d" , &t1,&t2,&t3,&t4);
			b[i].start= t1*60+t2;
			b[i].over = t3*60+t4;
			b[i].id =i;
		}
		qsort(a, na, sizeof(struct node), cmp);
		qsort(b, nb, sizeof(struct node), cmp);
		int pa=0 , pb=0;
		int ca = 0 , cb = 0;
		for (i =0 ; i<na+nb; i++)
		{
			bool isa;
			if (pa == na) isa  = false;
			else if (pb == nb ) isa = true;
			else isa = ((a[pa].start<b[pb].start)
			 || (a[pa].start==b[pb].start && a[pa].over < b[pb].over));
			
			if (isa)
			{
				if (!hasha[a[pa].id]) {pa++; continue;}
				loop(true ,pa);
				pa++;
				ca++;
			}
			else
			{
				if (!hashb[b[pb].id]){pb++; continue;}
				loop(false,pb);
				pb++;
				cb++;
			}
		}
		printf("Case #%d: %d %d\n" , times+1 , ca, cb);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}

 
