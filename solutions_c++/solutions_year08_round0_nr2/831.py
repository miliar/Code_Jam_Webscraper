#include <iostream>

using namespace std;

struct train
{
	int d1, d2, a1, a2, fl, done;
};

bool mysort(struct train p, struct train q){return ((p.d1<q.d1) || (p.d1==q.d1 && p.d2<q.d2)) || (p.d1==q.d1 && p.d2==q.d2 && p.a1<q.a1) || (p.d1==q.d1 && p.d2==q.d2 && p.a1==q.a1 && p.a2<q.a2);}

int main()
{
	int na, nb, ans[2], i, j, test, t, fl, t1, t2, tt;
	struct train A[202];
	scanf("%d", &t);
	for(test=1; test<=t; test++)
	{
		scanf("%d%d%d", &tt, &na, &nb);
		for(i=0; i<na; i++)
		{
			scanf("%d:%d %d:%d", &A[i].d1, &A[i].d2, &A[i].a1, &A[i].a2);
			A[i].fl=A[i].done=0;
		}
		for(i=na; i<na+nb; i++)
                {
                        scanf("%d:%d %d:%d", &A[i].d1, &A[i].d2, &A[i].a1, &A[i].a2);
			A[i].done=0;
			A[i].fl=1;
		}
		if(na==0 || nb==0)
		{
			printf("Case #%d: %d %d\n", test, na, nb);
			continue;
		}
		sort(A, A+na+nb, mysort);
		ans[0]=ans[1]=0;
		for(i=0; i<na+nb; i++)
		{
			if(A[i].done)
				continue;
			A[i].done=1;
			ans[A[i].fl]++;
			fl=A[i].fl;
			t1=A[i].a1;
			t2=A[i].a2+tt;
			t1+=t2/60;
			t2=t2%60;
			for(j=i+1; j<na+nb; j++)
			{
				if(A[j].done || A[j].fl==fl)
					continue;
				if(t1<A[j].d1 || (t1==A[j].d1 && t2<=A[j].d2))
				{
					A[j].done=1;
					t1=A[j].a1;
					t2=A[j].a2+tt;
					t1+=t2/60;
					t2=t2%60;
					fl=1-fl;
				}
			}
		}
		printf("Case #%d: %d %d\n", test, ans[0], ans[1]);
	}
	return 0;
}
